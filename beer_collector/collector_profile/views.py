from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView
from beer_collector.collector_profile.forms import CollectorProfileForm
from beer_collector.collector_profile.models import CollectorProfile


class ProfileDetailsView(DetailView):
    model = CollectorProfile
    template_name = 'profiles/profile-details.html'
    context_object_name = 'profile'


class ProfileEditView(UpdateView):
    model = CollectorProfile
    form_class = CollectorProfileForm
    template_name = 'profiles/profile-edit.html'

    def get_success_url(self):
        collector_profile_id = self.kwargs['pk']
        return reverse_lazy('profile details', kwargs={'pk': collector_profile_id})
