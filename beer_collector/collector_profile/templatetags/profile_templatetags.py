from django import template
from beer_collector.collector_profile.models import CollectorProfile

register = template.Library()


@register.inclusion_tag('tags/profile-complete-notification.html', takes_context=True)
def profile_complete_notification(context):
    user_id = context.request.user.id
    profile = CollectorProfile.objects.get(pk=user_id)
    return {
        'is_complete': profile.is_complete,
    }


@register.inclusion_tag('tags/get-profile-username.html', takes_context=True)
def get_profile(context):
    user_id = context.request.user.id
    profile = CollectorProfile.objects.get(pk=user_id)
    return {
        'profile': profile
    }
