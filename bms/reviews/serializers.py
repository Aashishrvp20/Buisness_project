from .models import *
from  rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= MyReview
        fields= "__all__"
        
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_msg(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Message must be at least 10 characters long.")
        return value

    def validate_rating(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError("Rating must be between 0 and 5.")
        return value

    def validate_brand_post(self, value):
        if not value.strip():
            raise serializers.ValidationError("Brand post cannot be empty.")
        return value