from django import template

register = template.Library()

@register.simple_tag
def get_user_rating(product, user):
    try:
        return product.ratings.get(user=user).value
    except product.ratings.model.DoesNotExist:
        return None
