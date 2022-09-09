
from multiprocessing import managers
from pyexpat import model
from statistics import mode
from b2b.models import Agent
from rest_framework import serializers
from account.models import User

class AgentSerializer(serializers.ModelSerializer ):
        password = serializers.CharField(
            min_length = 4,
            write_only = True,
            required   = True,
            style      = {'input_type': 'password'}
        )

        class Meta:
            model = Agent
            fields = [
                "id",              
                "first_name",      
                "last_name",       
                "contact_no",      
                "email_id",
                "password",        
                "company_name",    
                "country",         
                "state",           
                "created_at",
                "company_license", 
                "passport",        
                "national_id",     
                "vat_number",      
             ]

class AgentLoginSerializer(serializers.ModelSerializer):
    email =  serializers.EmailField(max_length=255)
    class Meta:
        model = Agent
        fields = ['email','password']
        
    