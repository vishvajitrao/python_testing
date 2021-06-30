from django.db import models


# from django.db.models import base
# from simple_history.models import HistoricalRecords
# from field_history.tracker import FieldHistoryTracker


# simple django model with relationship .


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline


# end .......


# django model history using django simple history....

class Poll(models.Model):
    question = models.CharField(max_length=200)
    question_type = models.CharField(max_length=200, blank=True, null=True)
    pub_date = models.DateTimeField('date published')

    # history = HistoricalRecords()

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # history = HistoricalRecords()

    def __str__(self):
        return self.choice_text


# end django simple history


# Django model with constraints

class Student(models.Model):
    first_name = models.CharField("Student's first name:- ", max_length=20)
    last_name = models.CharField("Student's last name:- ", max_length=20)
    email = models.CharField("Students's email:- ", max_length=70)
    age = models.IntegerField("Students's age:- ")
    roll_no = models.IntegerField()

    class Meta:
        db_table = "Student"
        verbose_name = "student"
        verbose_name_plural = "students"
        constraints = [models.CheckConstraint(check=models.Q(age__gte=18), name="age__gte_18"),
                       models.UniqueConstraint(fields=['email'], name="unique_email")]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class College(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField("College name:- ", max_length=50)
    address = models.CharField("Address of college:- ", max_length=60)
    course = models.CharField("Courses :- ", max_length=60, blank=True, null=True)

    def __str__(self):
        return self.name
