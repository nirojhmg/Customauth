from customauth.models import MyUser
from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'})

    class Meta:
        model = MyUser()
        fields = ('email', 'password', 'FirstName', 'MiddleName','LastName','is_student')
        write_only_fields = ('password')
        read_only_fields = ('is_student')

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user