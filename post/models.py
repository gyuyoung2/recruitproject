from django.db import models

# Create your models here.


class Recruit(models.Model):
    name = models.CharField(max_length = 100)
    age=models.CharField(max_length = 100)
    gedner_male = "남자"
    gedner_female = "여자"
    gender_choices = (
        (gedner_male, "남자"),
        (gedner_female, "여자"),
    )
    gender = models.CharField(("성별"), max_length=80, choices=gender_choices, null=True)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    
    image = models.ImageField(upload_to="post_img/")