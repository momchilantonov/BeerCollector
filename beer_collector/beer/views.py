from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from beer_collector.beer.forms import BeerStyleCreateForm, BeerStyleEditForm
from beer_collector.beer.models import BeerStyle
from beer_collector.core.views import get_obj_by_pk


class CreateBeerStyleView(CreateView):
    model = BeerStyle
    template_name = 'beer/create-beer-style.html'
    form_class = BeerStyleCreateForm
    success_url = reverse_lazy('home page')
    object = None

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class BeerStyleListView(ListView):
    model = BeerStyle
    template_name = 'beer/beer-style-list.html'
    context_object_name = 'beer_styles'
    paginate_by = 8

#     if req.POST:
#         form = BeerStyleCreateForm(
#             req.POST,
#         )
#         if form.is_valid():
#             form.save()
#             return redirect('home page')
#     else:
#         form = BeerStyleCreateForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(req, 'beer/create-beer-style.html', context)
#
#
# @login_required
# def edit_beer_style(req, pk):
#     beer_style = get_obj_by_pk(BeerStyle, pk)
#
#     if req.POST:
#         form = BeerStyleEditForm(
#             req.POST,
#             instance=beer_style,
#         )
#         if form.is_valid():
#             form.save()
#             return redirect('home page')
#     else:
#         form = BeerStyleEditForm(
#             instance=beer_style.__dict__,
#         )
#
#     context = {
#         'form': form,
#     }
#
#     return render(req, 'beer/edit-beer-style.html', context)
#
#
# @login_required
# def delete_beer_style(req, pk):
#     beer_style = get_obj_by_pk(BeerStyle, pk)
#
#     if req.POST:
#         beer_style.delete()
#         return redirect('home page')
#
#     context = {
#         'beer_style': beer_style,
#     }
#
#     return render(req, 'beer/delete-beer-style.html', context)
#
#
# def beer_style_details(req, pk):
#     beer_style = get_obj_by_pk(BeerStyle, pk)
#     context = {
#         'beer_style': beer_style,
#     }
#     return render(req, 'beer/beer-style-details.html', context)
#
#
# def create_beer(req):
#     pass
#
#
# def edit_beer(req, pk):
#     pass
#
#
# def delete_beer(req, pk):
#     pass
#
#
# def beer_details(req, pk):
#     pass
