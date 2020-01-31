from django.shortcuts import render

from apps.hello.models import Profile


def main(request):
    profile = Profile.load()
    return render(request, 'hello/index.html', locals())
