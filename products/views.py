# pylint: disable=no-member
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.db.models.functions import Lower

from wishlist.models import WishlistItem
from rating.models import Rating
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm


def all_products(request):
    """ View for show all products """

    products = Product.objects.annotate(average_rating=Avg('ratings__value'))
    query = None
    categories = None
    sort = None
    direction = None

    for product in products:
        product.average_rating = product.ratings.aggregate(Avg('value')).get('value__avg', 0)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View for individual product """

    product = get_object_or_404(Product, pk=product_id)
    average_rating = product.ratings.aggregate(Avg('value')).get('value__avg', 0)
    reviews = Review.objects.filter(product=product)
    form = ReviewForm()

    if request.method == 'POST':
        if 'add_to_wishlist' in request.POST:
            if request.user.is_authenticated:
                wishlist_item = WishlistItem.objects.filter(
                    user=request.user, product=product).first()
                if not wishlist_item:
                    wishlist_item = WishlistItem.objects.create(
                        user=request.user, product=product)
                    messages.info(request, 'Product added to wishlist!')
                else:
                    messages.error(
                        request, 'Product is already in your wishlist.')
            return redirect('product_detail', product_id=product_id)

    context = {
        'product': product,
        'average_rating': average_rating,
        'reviews': reviews,
        'form': form,
    }

    return render(request, 'products/product_detail.html', context)


def review_submit(request, product_id):
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            User = get_user_model()
            user_profile = User.objects.get(username=request.user.username)

            review = Review.objects.filter(
                product=product, user=user_profile).first()

            if review:
                review.comment = form.cleaned_data['comment']
                review.date_modified = timezone.now()
                messages.info(request, 'Review edited!')
            else:
                review = form.save(commit=False)
                review.product = product
                review.user = user_profile
                messages.info(request, 'Review added!')

            review.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = ReviewForm()

    reviews = Review.objects.filter(product=product)

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'products/product_detail.html', context)


def all_reviews(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'products/all_reviews.html', context)    


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    # Save the product name before deleting
    product_name = product.name
    # Delete the product instance
    product.delete()
    # Show success message with the product name
    messages.success(request, f"Product '{product_name}' deleted!")
    return redirect(reverse("products"))
