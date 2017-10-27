from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    content = models.CharField(max_length=800,null=True,blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    belong_to = models.ForeignKey(to=Article, related_name='under_comments', null=True, blank=True)
    best_commnet = models.BooleanField(default=False )
    def __str__(self):
        return self.content
