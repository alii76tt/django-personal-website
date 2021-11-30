from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse

from ckeditor.fields import RichTextField

# Create your models here.


class Social(models.Model):
    name = models.CharField(max_length=200, blank=True)
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=200, blank=True)
    subTitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=300, blank=True)
    date = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=200, blank=True)
    subTitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=300, blank=True)
    date = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class Skills(models.Model):
    title = models.CharField(max_length=200, blank=True)
    workflow = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Interest(models.Model):
    content = RichTextField(max_length=300, blank=True)

    def __str__(self):
        return self.content[:100]


class AwardAndCertifica(models.Model):
    title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Home(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )
    name = models.CharField(max_length=200)
    surName = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    shortLament = RichTextField()
    description = RichTextField()
    links = models.ManyToManyField(Social, blank=True)
    experiences = models.ManyToManyField(Experience, blank=True)
    educations = models.ManyToManyField(Education, blank=True)
    skills = models.ManyToManyField(Skills, blank=True)
    interest = models.ManyToManyField(Interest, blank=True)
    awardsandcertificates = models.ManyToManyField(
        AwardAndCertifica, blank=True)
    image = models.ImageField(blank=True, upload_to='home/')
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="100"/>'.format(self.image.url))

    def get_delete_url(self):
        return reverse('home:delete_profile', kwargs={'id': self.id})

    image_tag.short_description = "Image"
    image_tag.allow_tags = True


class Contact(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed')
    )

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=300)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    ip = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS, default="New")
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact Form Message"
        verbose_name_plural = "Contact Form Messages"


class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    icon = models.ImageField(blank=True, upload_to='settings/')
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
