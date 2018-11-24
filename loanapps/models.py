from django.db import models


# Create your models here.
class LoanApp(models.Model):
    name = models.CharField(max_length=128, unique=True)
    logo = models.ImageField(upload_to='logo')
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    app_url = models.URLField(default='NULL')
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
