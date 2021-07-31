from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from beer_collector.core.views import get_obj_by_pk
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from beer_collector.beer.models.beer_style import BeerStyle, BeerStyleLike
from beer_collector.beer.forms.beer_style import BeerStyleCreateForm, BeerStyleCommentForm, BeerStyleEditForm


class CreateBeerStyleView(LoginRequiredMixin, CreateView):
    model = BeerStyle
    template_name = 'beer/beer_style/beer-style-create.html'
    form_class = BeerStyleCreateForm
    success_url = reverse_lazy('beer style list')
    object = None

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class EditBeerStyleView(UpdateView):
    model = BeerStyle
    form_class = BeerStyleEditForm
    template_name = 'beer/beer_style/beer-style-edit.html'

    def get_success_url(self):
        beer_style_id = self.kwargs['pk']
        return reverse_lazy('beer style details', kwargs={'pk': beer_style_id})


class DeleteBeerStyleView(DeleteView):
    model = BeerStyle
    template_name = 'beer/beer_style/beer-style-delete.html'

    def get_success_url(self):
        return reverse('beer style delete done')


class DeleteBeerStyleDoneView(TemplateView):
    template_name = 'beer/beer_style/beer-style-delete-done.html'


class BeerStyleListView(ListView):
    model = BeerStyle
    template_name = 'beer/beer_style/beer-style-list.html'
    context_object_name = 'beer_styles'
    paginate_by = 8


def beer_style_details(req, pk):
    beer_style = get_obj_by_pk(BeerStyle, pk)
    beer_style.likes_count = beer_style.beerstylelike_set.count()
    beer_style_comments = beer_style.beerstylecomment_set.all()
    is_owner = beer_style.user == req.user
    is_liked = beer_style.beerstylelike_set.filter(user_id=req.user.id).exists()
    beer_style_comment_form = BeerStyleCommentForm(
        initial={
            'obj_pk': pk,
        }
    )
    context = {
        'beer_style': beer_style,
        'beer_style_comments': beer_style_comments,
        'is_owner': is_owner,
        'is_liked': is_liked,
        'beer_style_comment_form': beer_style_comment_form,
    }

    return render(req, 'beer/beer_style/beer-style-details.html', context)


@login_required
def beer_style_like(req, pk):
    beer_style = get_obj_by_pk(BeerStyle, pk)
    like_by_user = beer_style.beerstylelike_set.filter(user_id=req.user.id).first()

    if like_by_user:
        like_by_user.delete()
    else:
        like = BeerStyleLike(
            beer_style=beer_style,
            user=req.user,
        )
        like.save()

    return redirect('beer style details', beer_style.id)


@login_required
def beer_style_comment(req, pk):
    comment_form = BeerStyleCommentForm(req.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = req.user
        comment.save()

    return redirect('beer style details', pk)
