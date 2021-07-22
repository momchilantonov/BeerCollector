from django.shortcuts import render, redirect


# from beer_collector.collector_profile.models import CollectorProfile
#
#
# def get_obj(obj):
#     return obj.objects.first()
#
#
# def get_all_objs(obj):
#     return obj.objects.all()
#
#
# def get_obj_by_pk(obj, pk):
#     return obj.objects.get(pk=pk)
#
#
# def show_form(req, temp, form):
#     context = {
#         'form': form,
#     }
#     return render(req, temp, context)
#
#
# def save_form(req, temp, red, form):
#     if form.is_valid():
#         form.save()
#         return redirect(red)
#     return show_form(req, temp, form)

def get_obj_by_pk(obj, pk):
    return obj.objects.get(pk=pk)


def index(req):
    return render(req, 'core/home-page.html')
