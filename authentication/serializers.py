from rest_framework import serializers

from authentication.models import ReporterProfile


class ProfileCreateSerializer(serializers.ModelSerializer):
    """User Profile Serializer

    Serializes the user data from Facebook
    """
    name = serializers.CharField(required=True)
    fb_id = serializers.CharField(required=True)
    profile_pic = serializers.CharField(required=True)

    class Meta:
        """Model to be Serialized

        Specifies ReporterProfile as the model to be serialized as well as the relevant fields.
        """
        model = ReporterProfile
        fields = ('name', 'profile_pic', 'fb_id', 'fcm_token', 'location')

    def create(self, validated_data):
        name = validated_data.get('name')
        fb_id = validated_data.get('fb_id')
        profile_pic = validated_data.get('profile_pic')
        fcm_token = validated_data.get('fcm_token')

        return ReporterProfile.objects.create(
            name=name,
            fb_id=fb_id,
            profile_pic=profile_pic,
            fcm_token=fcm_token
        )


class UpdateSerializer(serializers.ModelSerializer):
    """
    This serializer re-serializes user data from the ReporterProfile model.
    """

    class Meta:
        model = ReporterProfile
        fields = ('name', 'profile_pic', 'fb_id', 'fcm_token', 'location')

    def create(self, validated_data):
        print validated_data


class ProfileListSerializer(serializers.ModelSerializer):
    """
    This class serializes a list of the users in the system.
    """
    class Meta:
        model = ReporterProfile
        fields = ('name', 'profile_pic', 'fb_id', 'fcm_token', 'location')
