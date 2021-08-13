from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, DetailView
from beer_collector.beer.forms.beer import BeerCreateForm, BeerEditForm, BeerCommentForm
from beer_collector.beer.models.beer import Beer, BeerLike
from beer_collector.beer.models.beer_style import BeerStyle
from beer_collector.core.utilities import get_obj_by_pk


class CreateBeerView(LoginRequiredMixin, CreateView):
    model = Beer
    template_name = 'beer/beer/beer-create.html'
    form_class = BeerCreateForm
    success_url = reverse_lazy('beer list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form()
        form.fields['type'].queryset = BeerStyle.objects.filter(user=self.request.user)
        return form


class EditBeerView(UpdateView):
    model = Beer
    form_class = BeerEditForm
    template_name = 'beer/beer/beer-edit.html'

    def get_success_url(self):
        beer_id = self.kwargs['pk']
        return reverse_lazy('beer details', kwargs={'pk': beer_id})


class DeleteBeerView(DeleteView):
    model = Beer
    template_name = 'beer/beer/beer-delete.html'
    success_url = reverse_lazy('beer delete done')

    def post(self, request, *args, **kwargs):
        if "No" in request.POST:
            return redirect('beer list')
        else:
            return super(DeleteBeerView, self).post(request, *args, **kwargs)


class DeleteBeerDoneView(TemplateView):
    template_name = 'beer/beer/beer-delete-done.html'


class BeerListView(ListView):
    model = Beer
    template_name = 'beer/beer/beer-list.html'
    context_object_name = 'beers'
    paginate_by = 8


class BeerUserListView(ListView):
    model = Beer
    template_name = 'beer/beer/beer-user-list.html'
    context_object_name = 'beers'
    paginate_by = 8

    def get_queryset(self):
        q_set = super().get_queryset()
        user = self.request.user
        return q_set.filter(user=user)


class BeerDetails(DetailView):
    model = Beer
    template_name = 'beer/beer/beer-details.html'
    context_object_name = 'beer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        beer = context['beer']
        beer.likes_count = beer.beerlike_set.count()
        beer_comments = beer.beercomment_set.all()
        is_owner = beer.user == self.request.user
        is_liked = beer.beerlike_set.filter(user_id=self.request.user.id).exists()
        beer_comment_form = BeerCommentForm(
            initial={
                'obj_pk': self.object.pk,
            }
        )

        context['beer_comments'] = beer_comments
        context['is_owner'] = is_owner
        context['is_liked'] = is_liked
        context['beer_comment_form'] = beer_comment_form

        return context


@login_required
def beer_like(req, pk):
    beer = get_obj_by_pk(Beer, pk)
    like_by_user = beer.beerlike_set.filter(user_id=req.user.id).first()

    if like_by_user:
        like_by_user.delete()
    else:
        like = BeerLike(
            beer=beer,
            user=req.user,
        )
        like.save()

    return redirect('beer details', beer.id)


@login_required
def beer_comment(req, pk):
    beer_comment_form = BeerCommentForm(req.POST)

    if beer_comment_form.is_valid():
        comment_beer = beer_comment_form.save(commit=False)
        comment_beer.user = req.user
        comment_beer.save()
    return redirect('beer details', pk)
