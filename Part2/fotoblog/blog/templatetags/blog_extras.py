from django import template
from django.utils import timezone

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR

register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__

@register.filter
def get_posted_at_display(posted_at):
    seconds_ago = (timezone.now() - posted_at).total_seconds()

    if seconds_ago < MINUTE:
        return 'Publié il y a moins d\'une minute.'
    elif 0 < seconds_ago < HOUR:
        minutes = int(seconds_ago // MINUTE)
        return f'Publié il y a {minutes} minute{"s" if minutes != 1 else ""}.'
    elif seconds_ago <= DAY:
        hours = int(seconds_ago // HOUR)
        return f'Publié il y a {hours} heures'
    else:
        return f'Publié le {posted_at.strftime("%d %b %y à %Hh%M")}'


@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    if user == context['user']:
        return 'vous'
    return user.username
