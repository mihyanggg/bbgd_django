from django.db import models
from user.models import User

class Post(models.Model):
    # 'on_delete=models.CASCADE' means that when a user is deleted, their posts will also be deleted 
    ## If you use 'SET_NULL' instead of 'CASCADE', it means that you want to keep the post but leave the user null.
    ### If you use SET_NULL, you must also use null=True.
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User is user_id (pk value)
    title = models.CharField(max_length=100)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True) # regist data # auto_now_add adds the creation time.
    img_url = models.URLField(null=True) # 'null=True' means that the image may or may not be received.

    class Meta():
        # If no table name is specified, the 'app_model' will be the table name (e.g. 'board_post').
        db_table="post"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="comment"
