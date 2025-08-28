from django import template

register = template.Library()

@register.filter
def mult(value, arg):
    """ضرب کردن مقدار در آرگومان"""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return ''
