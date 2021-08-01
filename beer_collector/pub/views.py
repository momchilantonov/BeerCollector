from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView
from beer_collector.pub.forms import PubCreateForm, PubEditForm
from beer_collector.pub.models import Pub


class CreatePubView(LoginRequiredMixin, CreateView):
    model = Pub
    template_name = 'pub/pub-create.html'
    form_class = PubCreateForm
    success_url = reverse_lazy('home page')
    object = None

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class EditPubView(UpdateView):
    model = Pub
    form_class = PubEditForm
    template_name = 'pub/pub-edit.html'

    def get_success_url(self):
        pub_id = self.kwargs['pk']
        return reverse_lazy('beer details', kwargs={'pk': pub_id})


class DeletePubView(DeleteView):
    model = Pub
    template_name = 'pub/pub-delete.html'

    def get_success_url(self):
        return reverse('pub delete done')


class DeletePubDoneView(TemplateView):
    template_name = 'pub/pub-delete-done.html'


class PubListView(ListView):
    model = Pub
    template_name = 'pub/pub-list.html'
    context_object_name = 'pubs'
    paginate_by = 8
