# pylint: disable=no-member
from django import forms
from .widgets import CustomClearableFileInput
from django.core.validators import MaxLengthValidator
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):
    """
    Creates the Product form information
    """
    class Meta:
        model = Product
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choices = friendly_names
        for field_name, field in self.fields.items():
            if field_name != "description":
                field.widget.attrs["class"] = "category-badge text-black \
                    text-decoration-none border border-dark rounded-pill"
            else:
                field.widget.attrs["class"] = "border-black rounded"


class ReviewForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        validators=[MaxLengthValidator(250)]
    )

    class Meta:
        model = Review
        fields = ['comment']
