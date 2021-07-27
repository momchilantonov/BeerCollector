from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from beer_collector.collector_profile.forms import CollectorProfileForm
from beer_collector.collector_profile.models import CollectorProfile
from beer_collector.core.views import get_obj_by_pk


@login_required
def profile_details(req):
    user_id = req.user.id
    current_profile = get_obj_by_pk(CollectorProfile, user_id)
    context = {
        'profile': current_profile,
    }

    return render(req, 'profiles/profile-details.html', context)


@login_required
def profile_edit(req):
    user_id = req.user.id
    current_profile = get_obj_by_pk(CollectorProfile, user_id)
    if req.POST:
        if not req.FILES:
            current_profile.image.delete()
        form = CollectorProfileForm(
            req.POST,
            req.FILES,
            instance=current_profile,
        )
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = CollectorProfileForm(
            instance=current_profile,
        )

    context = {
        'form': form,
    }

    return render(req, 'profiles/profile-edit.html', context)
