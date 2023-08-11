from django.contrib.auth.models import User
from django.db import models
from django.template import defaultfilters

class Category(models.Model):
    title = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('title',)
        verbose_name = verbose_name_plural = 'カテゴリー'


class Job(models.Model):
    category = models.ForeignKey(Category, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    position_salary = models.CharField(max_length=255)
    position_location = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    company_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = verbose_name_plural = '案件'

    def created_at_formatted(self):
        return defaultfilters.date(self.created_at, 'M d, Y')