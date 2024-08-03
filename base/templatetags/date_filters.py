from django import template
from django.utils import timezone
from datetime import datetime, timedelta

register = template.Library()


@register.filter
def custom_date_display(value):
    if not isinstance(value, datetime):
        return value

    now = timezone.now()
    delta = now - value
    minutes = delta.seconds // 60
    hours = delta.seconds // 3600
    day = delta.days

    if delta < timedelta(minutes=60):
        return f"{minutes}m" if minutes > 0 else "Just now"
    elif delta < timedelta(hours=23):
        return f'{hours}h'
    elif delta < timedelta(days=7):
        return f"{day}d"
    elif delta < timedelta(days=365):
        return value.strftime("%d %B")
    else:
        return value.strftime("%d %B %Y")
