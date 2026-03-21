from django.db import models

# Create your models here.
class Comment(models.Model):
    post_date = models.DateTimeField("Date")
    comment_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.comment_text