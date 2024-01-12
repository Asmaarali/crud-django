from django.db import models


# Create your models here.
class userclass(models.Model):
    student_class = models.CharField(max_length=50)

    def __str__(self):
        return self.student_class


class userinfo(models.Model):
    name = models.CharField(max_length=50)
    userclass = models.ForeignKey(userclass, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
