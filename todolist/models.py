from django.db import models
from django.utils import timezone

category_choices = [
    (1,'Select a Category'),
    (2,'Reminder'),
    (3,'Task'),
    (4,'Assignment'),
    (5,'Exam')
]

class Task(models.Model):
    category = models.IntegerField(choices=category_choices, default=None)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    def __str__(self):
        return self.title
