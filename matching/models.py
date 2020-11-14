from django.db import models


class Cohort(models.Model):
    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Mentee(models.Model):
    MenteeId = models.IntegerField()
    FName = models.TextField()
    LName = models.TextField()
    Pairing = models.ForeignKey("Mentor", on_delete=models.SET_NULL, null=True)

class Mentor(models.Model):
    MentorId = models.IntegerField()
    FName = models.TextField()
    LName = models.TextField()
    Industry = models.IntegerField()
    Pairing = models.ForeignKey("Mentee", on_delete=models.SET_NULL, null=True)
