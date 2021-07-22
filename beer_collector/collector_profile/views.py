from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from beer_collector.collector_profile.forms import CollectorProfileForm
from beer_collector.collector_profile.models import CollectorProfile


@login_required
def profile_details(req):
    user_id = req.user.id
    profile = CollectorProfile.objects.get(pk=user_id)
    context = {
        'profile': profile,
    }

    return render(req, 'profiles/profile-details.html', context)


@login_required
def profile_edit(req):
    user_id = req.user.id
    profile = CollectorProfile.objects.get(pk=user_id)
    if req.POST:
        form = CollectorProfileForm(
            req.POST,
            req.FILES,
            instance=profile,
        )
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = CollectorProfileForm(
            instance=profile,
        )

    context = {
        'form': form,
    }

    return render(req, 'profiles/profile-edit.html', context)
