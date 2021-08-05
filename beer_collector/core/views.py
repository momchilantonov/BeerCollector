from django.shortcuts import render


def home_page_with_profile(req):
    return render(req, 'core/home-page-with-profile.html')


def home_page_without_profile(req):
    return render(req, 'core/home-page-without-profile.html')


def index(req):
    if not req.user.is_authenticated:
        return home_page_without_profile(req)
    return home_page_with_profile(req)
