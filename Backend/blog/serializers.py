from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =
        fields = ['url', 'username', 'email', 'is_staff']