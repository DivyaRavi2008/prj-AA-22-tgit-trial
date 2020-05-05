from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    dept = serializers.CharField(max_length=20)
    dob = serializers.DateField()
    join = serializers.SerializerMethodField(read_only = True)

    def get_join(self, team):
        join = "yes"
        return join
    
    
    class Meta:
        model = Team
        fields = ('id','name','dept','dob','moto','join')
