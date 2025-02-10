from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High')
]


class Case(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField('Tag')
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='cases')
    complexity = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self):
        return self.title


class Tag(models.Model):

    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)
    order = models.IntegerField(null=True)
    image = models.FileField(upload_to='icons/', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['order']


class Solution(models.Model):
    case = models.ForeignKey(
        Case, related_name='solutions', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = HTMLField()
    steps = HTMLField()
    video_url = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    is_selected = models.BooleanField(default=False)


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        # Ensure only one solution is selected per case
        if self.is_selected:
            Solution.objects.filter(case=self.case).exclude(pk=self.pk).update(is_selected=False)
        super().save(*args, **kwargs)