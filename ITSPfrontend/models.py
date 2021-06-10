from django.db import models

# Create your models here.
class Info(models.Model):
   teamname = models.CharField(max_length=122, blank=True,null=True,default='enter')
   teamid= models.CharField(max_length=122, blank=True,null=True,default='enter')
   teamleadername = models.CharField(max_length=122, blank=True,null=True,default='enter')
   teamleaderphoneno = models.CharField(max_length=12, blank=True,null=True,default='enter')
   teamleaderemail = models.CharField(max_length=122, blank=True,null=True,default='enter')
   member1name = models.CharField(max_length=122, blank=True,null=True,default='enter')
   member1phoneno = models.CharField(max_length=12, blank=True,null=True,default='enter')
   member1email = models.CharField(max_length=122,blank=True,null=True,default='enter')
   member2name = models.CharField(max_length=122, blank=True,null=True,default='enter')
   member2phoneno = models.CharField(max_length=12, blank=True,null=True,default='enter')
   member2email = models.CharField(max_length=122, blank=True,null=True,default='enter')
   member3name = models.CharField(max_length=122, blank=True,null=True,default='enter')
   member3phoneno = models.CharField(max_length=12, blank=True,null=True,default='enter')
   member3email = models.CharField(max_length=122, blank=True,null=True ,default='enter')
   

   def __str__(self):
      return self.teamid


      

   
  


            
  

