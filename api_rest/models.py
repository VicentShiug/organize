from django.db import models

class User(models.Model):
  nickname = models.CharField(max_length=100)
  name = models.CharField(max_length=150)
  email = models.EmailField()
  age = models.IntegerField()
  
  def __str__(self):
    return f'Nickname: {self.nickname} | E-mail: {self.email}'