from django.db import models
from django.contrib.auth.models import AbstractUser # 기본유저모델 가져오기 #AbstractBaseUser 

# Get the AbstractUser class and customizes it.
# In the AbstractUser class have many field. So if you want just id&password than you inherit from AbstractBaseUser.
class User(AbstractUser): 
    nickname = models.CharField(max_length=30) # Add a nickname to AbstractUser. Max_length is 30.
    
    class Meta:
        db_table="user" # I make the table name "user".

