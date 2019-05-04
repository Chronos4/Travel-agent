from travel.models import Adventure
from rest_framework import serializers


class AdventureListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='travel_api:detail',
        lookup_field='unique_id'
    )

    class Meta:
        model = Adventure
        fields = [
            'unique_id',
            'users',
            'author',
            'country',
            'town',
            'start',
            'end',
            'url',
            'timestamp',
            'image'
        ]
