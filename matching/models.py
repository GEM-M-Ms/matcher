from django.db import models
from django.contrib.auth import get_user_model


class Cohort(models.Model):
    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Mentor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Mentee(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Match(models.Model):
    APPROVED = "AP"
    PENDING = "PD"

    STATUS_CHOICES = [(APPROVED, "Approved"), (PENDING, "Pending")]

    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    mentee = models.ForeignKey(Mentee, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING)
    approver = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Matches"

    def __str__(self):
        return f"Match(Mentor={self.mentor}, Mentee={self.mentee})"


class Settings(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Settings"
