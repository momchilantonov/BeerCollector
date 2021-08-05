from django import template
from beer_collector.beer.models.beer import Beer
from beer_collector.beer.models.beer_style import BeerStyle
from beer_collector.collector_profile.models import CollectorProfile
from beer_collector.core.utilities import get_obj_by_pk
from beer_collector.pub.models import Pub

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


@register.inclusion_tag('tags/show-profile-progress-bar.html', takes_context=True)
def show_progress_bar(context):
    user_id = context.request.user.id
    profile = get_obj_by_pk(CollectorProfile, user_id)
    profile_credentials_list = [
        profile.username,
        profile.first_name,
        profile.last_name,
        profile.about,
        str(profile.image),
    ]
    percentage = 100

    for credential in profile_credentials_list:
        if credential is None or credential == '':
            percentage -= 20

    return {
        'percentage': percentage
    }


@register.inclusion_tag('tags/show-profile-stats.html', takes_context=True)
def show_profile_stats(context):
    user = context.request.user

    beer_styles = BeerStyle.objects.all().filter(user=user)
    beer_styles_count = beer_styles.count()
    beer_styles_likes_count = 0
    for beer_style in beer_styles:
        beer_styles_likes_count += beer_style.beerstylelike_set.count()

    beers = Beer.objects.all().filter(user=user)
    beers_count = beers.count()
    beer_likes_count = 0
    for beer in beers:
        beer_likes_count += beer.beerlike_set.count()

    pubs = Pub.objects.all().filter(user=user)
    pubs_count = pubs.count()
    pub_likes_count = 0
    for pub in pubs:
        pub_likes_count += pub.publike_set.count()

    return {
        'beer_styles_count': beer_styles_count,
        'beers_count': beers_count,
        'pubs_count': pubs_count,
        'beer_styles_likes_count': beer_styles_likes_count,
        'beer_likes_count': beer_likes_count,
        'pub_likes_count': pub_likes_count,
    }
