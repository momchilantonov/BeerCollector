from django.shortcuts import render, redirect


def get_obj_by_pk(obj, pk):
    return obj.objects.get(pk=pk)


def home_page_with_profile(req):
    return render(req, 'core/home-page-with-profile.html')


def home_page_without_profile(req):
    return render(req, 'core/home-page-without-profile.html')


def index(req):
    if not req.user.is_authenticated:
        return home_page_without_profile(req)
    return home_page_with_profile(req)
