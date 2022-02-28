from django.db import models
from users.models import CustomUser


CHOICES = (
    ('Beginner','Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced','Advanced'))



class Skill(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sk = models.CharField(verbose_name="Skill", max_length=50)
    percent = models.CharField(verbose_name="How good are you?", max_length=30, choices=CHOICES, default='intermediate') 

    def __str__(self):
        return f'{self.sk} - {self.percent}'

class Language(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lg = models.CharField(verbose_name="Language", max_length=50)
    percent = models.CharField(verbose_name="How good are you?", max_length=30, choices=CHOICES, default='intermediate')

    def __str__(self):
        return f'{self.sk} - {self.percent}'


class About(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(max_length=1500)

    def __str__(self):
        return f'{self.description}'


class Work(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50) 
    work_description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField(verbose_name="End date(leave empty for current position)",null=True, blank=True)
    current = models.BooleanField(default=False)
    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f'{self.position} - {self.company} - {self.location}'

class Education(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    graduation_year = models.DateField()
    description = models.TextField(max_length=1500)
    class Meta:
        ordering = ['-graduation_year']

    def __str__(self):
        return f'{self.institution_name} - {self.degree} - {self.location}'

class Objective(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(max_length=1500)

    def __str__(self):
        return f'{self.description}'

