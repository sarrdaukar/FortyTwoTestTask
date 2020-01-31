from datetime import date

from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.utils.dateformat import DateFormat

from apps.hello.models import Profile


class TestMainView(TestCase):
    fixtures = ["hello/fixtures/initial_data.json"]

    def setUp(self):
        self.client = Client()
        self.profile = Profile.load()

    def test_main_view(self):
        """
        test main view returning correct statuscode,
        using right template and having all necessary data in context and
        template
        """
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hello/index.html")
        self.assertIn("profile", response.context)

        profile = response.context["profile"]
        self.assertIsInstance(response.context["profile"], Profile)
        self.assertEqual(profile.name, self.profile.name)
        self.assertEqual(profile.last_name, self.profile.last_name)
        self.assertEqual(profile.birthdate, self.profile.birthdate)
        self.assertEqual(profile.bio, self.profile.bio)
        self.assertEqual(profile.email, self.profile.email)
        self.assertEqual(profile.jabber, self.profile.jabber)
        self.assertEqual(profile.skype, self.profile.skype)
        self.assertEqual(profile.other_contacts, self.profile.other_contacts)

        self.assertContains(response, self.profile.name)
        self.assertContains(response, self.profile.last_name)
        self.assertContains(
            response, DateFormat(self.profile.birthdate).format('d.m.Y')
        )
        self.assertContains(response, self.profile.bio)
        self.assertContains(response, self.profile.email)
        self.assertContains(response, self.profile.jabber)
        self.assertContains(response, self.profile.skype)
        self.assertContains(response, self.profile.other_contacts)


class TestProfileModel(TestCase):
    fixtures = ["hello/fixtures/initial_data.json"]

    def setUp(self):
        self.profile = Profile.load()

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
