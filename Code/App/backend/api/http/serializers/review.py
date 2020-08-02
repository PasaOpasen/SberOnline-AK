from rest_framework.serializers import ModelSerializer, CharField
from api.models import ReviewText

class ReviewSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ReviewText
