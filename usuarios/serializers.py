from rest_framework import serializers
from .models import PermissaoCustom


class PermissaoCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissaoCustom
        fields = '__all__'