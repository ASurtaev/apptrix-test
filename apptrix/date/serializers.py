from rest_framework import serializers

from  .models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('img', 'gender', 'first_name', 'last_name', 'email')