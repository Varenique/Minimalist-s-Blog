from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    class Meta:
        db_table = 'posts'
    pub_date = models.DateTimeField('date published')
    title = models.CharField(default='default title', max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='media/images', height_field=None, width_field=None, null=True, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comments(models.Model):
    class Meta:
        db_table = 'comments'

    comment_text = models.TextField(verbose_name="")
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_date = models.DateField(u'date', auto_now=True)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)



class Like(models.Model):
    class Meta:
        db_table = 'likes'

    post_number = models.IntegerField()
    name_of_user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
