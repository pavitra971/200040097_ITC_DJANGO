from django import forms

class InnfoForm(forms.Form):
   teamname = forms.CharField(label='teamname' ,max_length=122),
   teamid = forms.CharField(label='teamid' ,max_length=122),
   teamleadername = forms.CharField(label='teamleadername' ,max_length=122),
   teamleaderphoneno = forms.CharField(label='teamleaderphoneno' ,max_length=122),
   teamleaderemail =forms.CharField(label='teamleaderemail' ,max_length=122),
   member1name = forms.CharField(label='member1name' ,max_length=122),
   member1phoneno = forms.CharField(label='member1phoneno' ,max_length=122),
   member1email = forms.CharField(label='member1email' ,max_length=122),
   member2name =forms.CharField(label='member2name' ,max_length=122),
   member2phoneno = forms.CharField(label='member2phoneno' ,max_length=122),
   member2email =forms.CharField(label='member2email' ,max_length=122),
   member3name = forms.CharField(label='member3name' ,max_length=122),
   member3phoneno =forms.CharField(label='member3phoneno' ,max_length=122),
   member3email =forms.CharField(label='member3email' ,max_length=122),
  

