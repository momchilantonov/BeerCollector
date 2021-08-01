from django import template
from beer_collector.core.views import get_obj_by_pk
from beer_collector.collector_profile.models import CollectorProfile

register = template.Library()


@register.inclusion_tag('tags/show-profile-complete-notification.html', takes_context=True)
def show_profile_complete_notification(context):
    user_id = context.request.user.id
    profile = get_obj_by_pk(CollectorProfile, user_id)
    return {
        'profile_id': user_id,
        'is_complete': profile.is_complete,
    }


@register.inclusion_tag('tags/show-profile-username.html', takes_context=True)
def show_profile_username(context):
    user_id = context.request.user.id
    profile = get_obj_by_pk(CollectorProfile, user_id)
    return {
        'profile_id': user_id,
        'profile': profile,
    }


@register.inclusion_tag('tags/show-progress-bar.html', takes_context=True)
def show_progress_bar(context):
    user_id = context.request.user.id
    profile = get_obj_by_pk(CollectorProfile, user_id)
    profile_credentials_list = [
        profile.username,
        profile.first_name,
        profile.last_name,
        profile.about,
        profile.image,
    ]
    percentage = 0
    for credential in profile_credentials_list:
        if credential is not None:
            percentage += 20

    return {
        'percentage': percentage
    }
