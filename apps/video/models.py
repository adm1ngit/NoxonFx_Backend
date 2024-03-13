from django.db import models
from apps.users.models import User


class ModulClass(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Modul'
        verbose_name_plural = 'Moduls'
        ordering = ('created_at',)


class VideoApp(models.Model):
    modul = models.ForeignKey(ModulClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos', blank=True)
    description = models.TextField(blank=True)
    comment = models.ManyToManyField('Comment', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    marked_view = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.modul} - {self.name}"

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        ordering = ('created_at',)


class Comment(models.Model):
    commented_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True)
    commented_on = models.DateTimeField(auto_now_add=True)
