from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    web_link = models.CharField(max_length=200, default="")

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class RepeatingTask(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    days = models.CharField(max_length=7, default="0000000")
    initial_date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
