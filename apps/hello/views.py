from collections import namedtuple
from datetime import date

from django.shortcuts import render

Profile = namedtuple(
    'Profile',
    [
        'name', 'last_name', 'birthdate', 'bio', 'email', 'jabber', 'skype',
        'other_contacts'
    ]
)


def main(request):
    profile = Profile(
        'Yaroslav', 'Cheb', date(1992, 11, 6), 'My short biography',
        'mail@mail.com', 'jabber@jabber.com', 'skype_nick', 'Other contacts'
    )
    return render(request, 'hello/index.html', locals())
