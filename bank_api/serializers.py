from rest_framework import serializers
from .models import *


class bankSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = banks
        fields = '__all__'


class branchSerializer(serializers.ModelSerializer):
    bank_name = serializers.SerializerMethodField()

    class Meta:
        model = branches
        fields = ['bank_name', 'ifsc', 'branch', 'address', 'city', 'district', 'state']

    def get_bank_name(self, obj):
        return obj.bank.name


class ifsc_branchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = branches
        fields = ['ifsc']


class bank_city_branchSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city', label='City (In Capitals)')
    
    class Meta:
        model = branches
        fields = ['bank', 'city_name']

