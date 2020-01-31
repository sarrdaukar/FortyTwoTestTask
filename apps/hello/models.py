from django.db import models


class SingletonModel(models.Model):
    INSTANCE_ID = 1

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = SingletonModel.INSTANCE_ID
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=SingletonModel.INSTANCE_ID)
        return obj


class Profile(SingletonModel):
    name = models.CharField(max_length=100, verbose_name=u"Name")
    last_name = models.CharField(max_length=100, verbose_name=u"Last name")
    birthdate = models.DateField(verbose_name=u"Birth date")
    bio = models.TextField(verbose_name=u"Bio")
    email = models.EmailField(max_length=255, verbose_name=u"Email")
    jabber = models.EmailField(max_length=255, verbose_name=u"Jabber")
    skype = models.CharField(max_length=255, verbose_name=u"Skype")
    other_contacts = models.TextField(verbose_name=u"Other contacts")

    class Meta:
        verbose_name = u"Profile"
        verbose_name_plural = u"Profile"

    def __unicode__(self):
        return u"Profile"
