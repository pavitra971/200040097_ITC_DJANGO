from django.db import models

# Create your models here.
class Info(models.Model):
   teamname = models.CharField(max_length=122, blank=True,null=True)
   teamid= models.CharField(max_length=122, blank=True,null=True)
   teamleadername = models.CharField(max_length=122, blank=True,null=True)
   teamleaderphoneno = models.CharField(max_length=12, blank=True,null=True)
   teamleaderemail = models.CharField(max_length=122, blank=True,null=True)
   member1name = models.CharField(max_length=122, blank=True,null=True)
   member1phoneno = models.CharField(max_length=12, blank=True,null=True)
   member1email = models.CharField(max_length=122,blank=True,null=True)
   member2name = models.CharField(max_length=122, blank=True,null=True)
   member2phoneno = models.CharField(max_length=12, blank=True,null=True)
   member2email = models.CharField(max_length=122, blank=True,null=True)
   member3name = models.CharField(max_length=122, blank=True,null=True)
   member3phoneno = models.CharField(max_length=12, blank=True,null=True)
   member3email = models.CharField(max_length=122, blank=True,null=True)
   

   def __str__(self):
      return self.teamid


      

   
  


            
  

