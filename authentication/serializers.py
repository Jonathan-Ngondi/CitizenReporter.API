from rest_framework import serializers

from authentication.models import ReporterProfile


class ProfileCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    uid = serializers.CharField(required=True)
    profile_pic = serializers.CharField(required=True)

    class Meta:
        model = ReporterProfile
        fields = ('name', 'profile_pic', 'uid', 'fcm_token', 'location')

    def create(self, validated_data):
        name = validated_data.get('name')
        uid = validated_data.get('uid')
        profile_pic = validated_data.get('profile_pic')
        fcm_token = validated_data.get('fcm_token')

        return ReporterProfile.objects.create(
            name=name,
            uid=uid,
            profile_pic=profile_pic,
            fcm_token=fcm_token
        )


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporterProfile
        fields = ('name', 'profile_pic', 'uid', 'fcm_token', 'location')

    def create(self, validated_data):
        print validated_data


class ProfileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReporterProfile
        fields = ('name', 'profile_pic', 'uid', 'fcm_token', 'location')