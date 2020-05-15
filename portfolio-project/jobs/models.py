from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')


    company = models.CharField(max_length=100, default='default', editable=True)
    title = models.CharField(max_length=100, default='default', editable=True)
    duration = models.CharField(max_length=100, default='default', editable=True)
    location = models.CharField(max_length=100, default='default', editable=True)
    summary  = models.CharField(max_length=400, default='default', editable=True)

    def __str__(self):
        return (self.title + ":" + self.company)


class Education(models.Model):
    #add date??
    logo = models.ImageField(upload_to='images/')
    school = models.CharField(max_length=100, default='default', editable=True)
    degree = models.CharField(max_length=100, default='default', editable=True)
    duration = models.CharField(max_length=100, default='default', editable=True)
    summary = models.CharField(max_length=400, default='default', editable=True)

    def __str__(self):
        return (self.degree+":"+self.school)


class Skills(models.Model):
    s_title = models.CharField(max_length=100, default='default', editable=True)
    def __str__(self):
        return (self.s_title)

class Tskills(models.Model):
    ts_title = models.CharField(max_length=100, default='default', editable=True)
    ts_level_duration =  models.CharField(max_length=200, default='default', editable=True)
    ts_summary = models.CharField(max_length=300, default='default', editable=True)
    def __str__(self):
        return (self.ts_title)

class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100, default='default', editable=True)
    link = models.CharField(max_length=300, default='default', editable=True)
    summary = models.CharField(max_length=500, default='default', editable=True)
    source = models.CharField(max_length=100, default='default', editable=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100, default='default', editable=True)
    link = models.CharField(max_length=300, default='default', editable=True)
    summary = models.CharField(max_length=500, default='default', editable=True)
    source = models.CharField(max_length=100, default='default', editable=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return 'Profile Photo'

class Profilefooter(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return 'Footer Photo'

class Introduction(models.Model):
    summary = models.CharField(max_length=500, default='default', editable=True)

    def __str__(self):
        return 'Intro'

class Summary(models.Model):
    topic = models.CharField(max_length=150, default='default', editable=True)

    def __str__(self):
        return self.topic

class WorkSummary(models.Model):
    summary = models.CharField(max_length=300, default='default', editable=True)
    title = models.CharField(max_length=100, default='default', editable=True)
    link = models.CharField(max_length=300, default='default', editable=True)
    company = models.CharField(max_length=100, default='default', editable=True)

    def __str__(self):
        return 'Currently Working @'

class Status(models.Model):
    status = models.CharField(max_length=200, default='default', editable=True)

    def __str__(self):
        return self.status
