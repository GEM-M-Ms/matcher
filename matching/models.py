from django.db import models
from django.contrib.auth import get_user_model


class Cohort(models.Model):
    title = models.CharField(max_length=200)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_on"]


class Mentor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    other_attributes = models.JSONField(null=True, blank=True)

    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Mentee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    other_attributes = models.JSONField(null=True, blank=True)

    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

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


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.BinaryField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MatchConfig(models.Model):
    mentee_column_name = models.CharField(max_length=200)
    mentor_column_name = models.CharField(max_length=200)
    weight = models.FloatField()

    def __str__(self):
        return f"{self.mentee_column_name} {self.mentor_column_name} {self.weight}"

    class Meta:
        verbose_name_plural = "MatchConfig"
