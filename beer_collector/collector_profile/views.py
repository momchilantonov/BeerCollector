from django.contrib.auth.decorators import login_required
from beer_collector.core.views import get_obj_by_pk
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DetailView, TemplateView
from beer_collector.collector_profile.forms import CollectorProfileForm
from beer_collector.collector_profile.models import CollectorProfile


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = CollectorProfile
    template_name = 'profiles/profile-details.html'
    context_object_name = 'profile'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CollectorProfile
    form_class = CollectorProfileForm
    template_name = 'profiles/profile-edit.html'
    success_url = reverse_lazy('profile edit done')


class ProfileEditDoneView(TemplateView):
    template_name = 'profiles/profile-edit-done.html'

# FBV VIEWS
# @login_required
# def profile_details(req):
#     user_id = req.user.id
#     current_profile = get_obj_by_pk(CollectorProfile, user_id)
#     context = {
#         'profile': current_profile,
#     }
#
#     return render(req, 'profiles/profile-details.html', context)
#
#
# @login_required
# def profile_edit(req):
#     user_id = req.user.id
#     current_profile = get_obj_by_pk(CollectorProfile, user_id)
#     if req.POST:
#         form = CollectorProfileForm(
#             req.POST,
#             req.FILES,
#             instance=current_profile,
#         )
#         if form.is_valid():
#             form.save()
#             return redirect('profile details')
#     else:
#         form = CollectorProfileForm(
#             instance=current_profile,
#         )
#
#     context = {
#         'form': form,
#     }
#
#     return render(req, 'profiles/profile-edit.html', context)
