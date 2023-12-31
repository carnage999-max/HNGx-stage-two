from rest_framework import serializers
from base.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        
    def validate_name(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("name must be a string.")
        return value
