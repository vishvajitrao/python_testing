from django.db import models
from django.db.models import base
from simple_history.models import HistoricalRecords
from socket import gethostname, gethostbyname

# Create your models here.


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


# getting the ipaddress of the machine
hostname = gethostname()
ip = gethostbyname(hostname)


# Maintain History

class Poll(models.Model):
    question = models.CharField(max_length=200)
    question_type = models.CharField(max_length=200, blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    history = HistoricalRecords()

    def __str__(self):
        return self.question
    
    @property
    def get_id(self):
        return self.id


# Adding the extra fields in ChoiceHistory table

class ChoiceHistory(models.Model):
    ip_address = models.GenericIPAddressField(('IP address'), default=ip)
    
    class Meta:
        abstract = True


class Choice(models.Model):
    poll = models.ForeignKey(Poll, default=Poll.get_id, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    history = HistoricalRecords(bases=[ChoiceHistory, ])

    def __str__(self):
        return self.choice_text




    





