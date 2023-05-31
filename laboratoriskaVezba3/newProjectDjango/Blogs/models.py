from django.contrib.auth.models import User
from django.db import models


class User_New(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def str(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User_New, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=255)
    file = models.FileField(upload_to='file/')
    date_created = models.DateField()
    last_edited = models.DateField()

    def str(self):
        return f"{self.title} - {self.user.name}"


class Comment(models.Model):
    comment_user = models.ForeignKey(User_New, on_delete=models.CASCADE, null=True)
    comment_description = models.TextField()
    date_comment_created = models.DateField()

    def str(self):
        return self.comment_user.name


class Comment_on_Post(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Block_User(models.Model):
    blocking_user = models.ForeignKey(User_New, on_delete=models.CASCADE, related_name="blog_user_blocker")
    blocked_user = models.ForeignKey(User_New, on_delete=models.CASCADE, related_name="blog_user_blocked")

    def str(self):
        return f"{self.blocking_user} blocked {self.blocked_user}"