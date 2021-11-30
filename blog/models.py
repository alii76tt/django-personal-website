from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.urls import reverse

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, editable=False,
                            max_length=130)

    def __str__(self):
        return self.name

    def get_absoulte_url(self):
        return reverse('post:category', kwargs={'slug': self.slug, 'id': self.id})

    def get_create_url(self):
        return reverse('post:add_category')

    def get_update_url(self):
        return reverse('post:update_category', kwargs={'slug': self.slug, 'id': self.id})

    def get_delete_url(self):
        return reverse('post:delete_category', kwargs={'slug': self.slug, 'id': self.id})

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Category.objects.filter(slug=unique_slug):
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Category, self).save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.name

    def get_absoulte_url(self):
        return reverse('post:tag', kwargs={'slug': self.slug, 'id': self.id})

    def get_create_url(self):
        return reverse('post:add_tag')

    def get_update_url(self):
        return reverse('post:update_tag', kwargs={'slug': self.slug, 'id': self.id})

    def get_delete_url(self):
        return reverse('post:delete_tag', kwargs={'slug': self.slug, 'id': self.id})

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Tag.objects.filter(slug=unique_slug):
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Tag, self).save(*args, **kwargs)


class Post(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Author',
                             related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name="Title")
    content = RichTextField(verbose_name="Content")
    publishing_date = models.DateTimeField(
        verbose_name="Publishing Date", auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='blog/')
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=200)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="100"/>'.format(self.image.url))

    image_tag.short_description = "Image"
    image_tag.allow_tags = True

    def get_absoulte_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('post:create')

    def get_update_url(self):
        return reverse('post:update', kwargs={'slug': self.slug, 'id': self.id})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'slug': self.slug, 'id': self.id})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug):
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publishing_date', 'id']


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    ip = models.CharField(blank=True, max_length=20)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
