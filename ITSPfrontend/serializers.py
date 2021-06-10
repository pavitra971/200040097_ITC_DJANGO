from rest_framework import serializers
from .models import Info



class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('teamname', 'teamid', 'teamleadername', 'teamleaderphoneno', 'teamleaderemail', 'member1name', 'member1phoneno', 'member1email', 'member2name', 'member2phoneno', 'member2email', 'member3name', 'member3phoneno', 'member3email')

        def create(self, validated_data):
             return Info.objects.create(validated_data)
        
        
        
        def update(self, instance, validated_data):
             
             instance.teamname = validated_data.get('teamname', instance.teamname)
             instance.teamid = validated_data.get('teamid', instance.teamid)
             instance.teamleadername = validated_data.get('teamleadername', instance.teamleadername)
             instance.teamleaderphoneno = validated_data.get('teamleaderphoneno', instance.teamleaderphoneno)
             instance.teamleaderemail = validated_data.get('teamleaderemail', instance.teamleaderemail)
             instance.member1name = validated_data.get('member1name', instance.member1name)
             instance.member1phoneno = validated_data.get('member1phoneno', instance.member1phoneno)
             instance.member1email = validated_data.get('member1email', instance.member1email)
             instance.member2name = validated_data.get('member2name', instance.member2name)
             instance.member2phoneno = validated_data.get('member2phoneno', instance.member2phoneno)
             instance.member2email = validated_data.get('member2email', instance.member2email)
             instance.member3name = validated_data.get('member3name', instance.member3name)
             instance.member3phoneno = validated_data.get('member3phoneno', instance.member3phoneno)
             instance.member3email = validated_data.get('member3email', instance.member3email)
             instance.save()
             return instance