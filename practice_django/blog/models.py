from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    CATEGORY = (
        ('art', 'Art'),
        ('sport', 'Sport'),
        ('music', 'Music'),
        ('economy', 'Economy'),
        ('beauty', 'beauty'),
        ('science', 'science'),
    )

    # additional options
    class Meta:
        verbose_name = 'Create Post'
        verbose_name_plural = 'Create Posts'

    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField(max_length=5000, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(max_length=100)
    category = models.CharField(
        max_length=32,
        choices=CATEGORY,
        default='art',
        verbose_name='Category'
    )
    likes = models.ManyToManyField(User, related_name='postcomment', blank=True)
    reply = models.ForeignKey('self', null=True, related_name='reply_ok', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
