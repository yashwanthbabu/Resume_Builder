from django.db import models

# Create your models here.

class Name(models.Model):
    Full_name = models.CharField(max_length=35,null=False,blank=False)
    Email_id = models.EmailField(max_length=35,null=False,blank=False)
    Crt_date = models.DateField(auto_now=True)
    Upt_date = models.DateField(auto_now=True)
    
        
    def __unicode__(self):
        return u'%s' % (self.Full_name)

class Profession(models.Model):
    Job_Type = models.CharField(max_length=15,null=True,blank=True)
    Total_Experience_in_months = models.IntegerField(null=True,blank=True)
    Current_Industry = models.CharField(max_length=15,null=True,blank=True)
    Functional_Area = models.CharField(max_length=15,null=True,blank=True)
    Key_Skills = models.TextField(max_length=40,null=True,blank=True)
    prof = models.ForeignKey(Name,null=True,blank=True)
    Crt_date = models.DateField(auto_now=True)
    Upt_date = models.DateField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.Job_Type)


class Education(models.Model):
    Qualification = models.CharField(max_length=35,null=False,blank=False)
    University = models.CharField(max_length=35,null=False,blank=False)
    Year_of_Passing = models.IntegerField(null=False,blank=True)
    Aggrigation = models.IntegerField(null=True,blank=True)
    edn = models.ForeignKey(Name,null=True,blank=True)
    Crt_date = models.DateField(auto_now=True)
    Upt_date = models.DateField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' % (self.Qualification, self.University)


