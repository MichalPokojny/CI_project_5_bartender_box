from django import template

register = template.Library()

@register.simple_tag
def get_user_rating(product, user):
    try:
        # Retrieve the rating for the given product and user
        # If the rating exists, return its value
        return product.ratings.get(user=user).value
    except product.ratings.model.DoesNotExist:
        # If the rating does not exist, return None
        return None
