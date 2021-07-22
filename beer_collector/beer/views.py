from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from beer_collector.beer.forms import BeerStyleCreateForm, BeerStyleEditForm
from beer_collector.beer.models import BeerStyle
from beer_collector.core.views import get_obj_by_pk


@login_required
def create_beer_style(req):
    if req.POST:
        form = BeerStyleCreateForm(
            req.POST,
        )
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = BeerStyleCreateForm()

    context = {
        'form': form,
    }

    return render(req, 'beer/create-beer-style.html', context)


@login_required
def edit_beer_style(req, pk):
    beer_style = get_obj_by_pk(BeerStyle, pk)

    if req.POST:
        form = BeerStyleEditForm(
            req.POST,
            instance=beer_style,
        )
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = BeerStyleEditForm(
            instance=beer_style.__dict__,
        )

    context = {
        'form': form,
    }

    return render(req, 'beer/edit-beer-style.html', context)


@login_required
def delete_beer_style(req, pk):
    beer_style = get_obj_by_pk(BeerStyle, pk)

    if req.POST:
        beer_style.delete()
        return redirect('home page')

    context = {
        'beer_style': beer_style,
    }

    return render(req, 'beer/delete-beer-style.html', context)


def beer_style_details(req, pk):
    beer_style = get_obj_by_pk(BeerStyle, pk)
    context = {
        'beer_style': beer_style,
    }
    return render(req, 'beer/beer-style-details.html', context)


def create_beer(req):
    pass


def edit_beer(req, pk):
    pass


def delete_beer(req, pk):
    pass


def beer_details(req, pk):
    pass
