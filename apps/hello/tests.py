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
        self.assertEqual(profile.email, "mail@mail.com")
        self.assertEqual(profile.jabber, "jabber@jabber.com")
        self.assertEqual(profile.skype, "skype_nick")
        self.assertEqual(profile.other_contacts, "Other contacts")


class TestProfileModel(TestCase):

    def setUp(self):
        profile = Profile(
            name="Yaroslav", last_name="Cheb", birthdate=date(1992, 11, 6),
            bio="My short biography", email="mail@mail.com",
            jabber="jabber@jabber.com", skype="skype_nick",
            other_contacts="Other contacts"
        )
        profile.save()
        self.profile = profile

    def test_profile_load(self):
        "Test Profile load method"
        profile = Profile.load()
        self.assertEqual(profile.id, Profile.INSTANCE_ID)
        self.assertEqual(profile.name, self.profile.name)
        self.assertEqual(profile.last_name, self.profile.last_name)
        self.assertEqual(profile.bio, self.profile.bio)
        self.assertEqual(profile.email, self.profile.email)
        self.assertEqual(profile.jabber, self.profile.jabber)
        self.assertEqual(profile.skype, self.profile.skype)
        self.assertEqual(profile.other_contacts, self.profile.other_contacts)

    def test_profile_model_has_only_one_object(self):
        "Test if Profile always has one db instance"
        profile_2 = Profile(
            name="John", last_name="Smith", birthdate=date(2000, 2, 22),
            bio="Bio of John Smith", email="johnsmith@mail.com",
            jabber="johnsmith@jabber.com", skype="johnsmith_skype",
            other_contacts="Contacts"
        )
        profile_2.save()
        # first profile object created in setUp
        self.assertEqual(Profile.objects.count(), 1)
