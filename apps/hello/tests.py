from datetime import date

from django.test import Client, TestCase
from django.core.urlresolvers import reverse


class TestMainView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_main_view(self):
        """
        test main view returning correct statuscode,
        using right template and having all necessary data in context
        """
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hello/index.html")
        self.assertIn("profile", response.context)

        profile = response.context["profile"]
        self.assertEqual(profile.name, "Yaroslav")
        self.assertEqual(profile.last_name, "Cheb")
        self.assertEqual(profile.birthdate, date(1992, 11, 6))
        self.assertEqual(profile.bio, "My short biography")
        self.assertEqual(profile.email, 'mail@mail.com')
        self.assertEqual(profile.jabber, 'jabber@jabber.com')
        self.assertEqual(profile.skype, 'skype_nick')
        self.assertEqual(profile.other_contacts, 'Other contacts')
