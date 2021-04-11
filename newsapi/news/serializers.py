from rest_framework import serializers
from .models import Headline


class HeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        #fields = '__all__' # importing all fields
        fields = (
            'id', 'title', 'category', 'url'
        )