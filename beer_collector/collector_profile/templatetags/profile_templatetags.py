from django import template
from beer_collector.core.views import get_obj_by_pk
from beer_collector.collector_profile.models import CollectorProfile

register = template.Library()


@register.inclusion_tag('tags/profile-complete-notification.html', takes_context=True)
def profile_complete_notification(context):
    user_id = context.request.user.id
    profile = get_obj_by_pk(CollectorProfile, user_id)
    return {
        'profile_id': user_id,
        'is_complete': profile.is_complete,
    }


@register.inclusion_tag('tags/get-profile-username.html', takes_context=True)
def get_profile(context):
    user_id = context.request.user.id
    profile = get_obj_by_pk(CollectorProfile, user_id)
    return {
        'profile_id': user_id,
        'profile': profile,
    }
