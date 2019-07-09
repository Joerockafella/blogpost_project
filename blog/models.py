
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # This redirect the user at post detail page after creating a new post
    #if you want it to redirect to home just set an attribute in create view called success_url and set it to home page
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

