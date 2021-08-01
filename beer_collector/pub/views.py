from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView

from beer_collector.core.views import get_obj_by_pk
from beer_collector.pub.forms import PubCreateForm, PubEditForm, PubCommentForm
from beer_collector.pub.models import Pub, PubLike


class CreatePubView(LoginRequiredMixin, CreateView):
    model = Pub
    template_name = 'pub/pub-create.html'
    form_class = PubCreateForm
    success_url = reverse_lazy('pub list')
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
        return reverse_lazy('pub details', kwargs={'pk': pub_id})


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


def pub_details(req, pk):
    pub = get_obj_by_pk(Pub, pk)
    pub.likes_count = pub.publike_set.count()
    pub_comments = pub.pubcomment_set.all()
    is_owner = pub.user == req.user
    is_liked = pub.publike_set.filter(user_id=req.user.id).exists()
    pub_comment_form = PubCommentForm(
        initial={
            'obj_pk': pk,
        }
    )
    context = {
        'pub': pub,
        'pub_comments': pub_comments,
        'is_owner': is_owner,
        'is_liked': is_liked,
        'pub_comment_form': pub_comment_form,
    }

    return render(req, 'pub/pub-details.html', context)


@login_required
def pub_like(req, pk):
    pub = get_obj_by_pk(Pub, pk)
    like_by_user = pub.publike_set.filter(user_id=req.user.id).first()

    if like_by_user:
        like_by_user.delete()
    else:
        like = PubLike(
            pub=pub,
            user=req.user,
        )
        like.save()

    return redirect('pub details', pub.id)


@login_required
def pub_comment(req, pk):
    pub_comment_form = PubCommentForm(req.POST)

    if pub_comment_form.is_valid():
        comment_pub = pub_comment_form.save(commit=False)
        comment_pub.user = req.user
        comment_pub.save()
    return redirect('pub details', pk)
