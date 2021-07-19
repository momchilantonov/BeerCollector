from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from beer_collector.collector_profile.forms import CollectorProfileForm
from beer_collector.collector_profile.models import CollectorProfile


@login_required
def profile_details(req):
    profile = CollectorProfile.objects.get(pk=req.user.id)
    user = req.user.id
    if req.POST:
        form = CollectorProfileForm(req.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CollectorProfileForm(instance=profile)

    context = {
        'form': form,
        'user': user,
    }

    return render(req, 'profiles/details.html', context)
