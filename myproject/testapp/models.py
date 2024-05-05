from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=1000)
    description=models.CharField(max_length=100)
    date_published=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
