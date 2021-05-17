from rest_framework import serializers
from .models import BranchInfo


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchInfo
        #fields = ['ifsc','bank_id','branch','address','city','district','state','bank_name']

        fields = '__all__'


