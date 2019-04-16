from travel.models import Adventure
from rest_framework import serializers




class AdventureListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Adventure
		fields = [
			'users',
			'author',
			'country',
			'town',
			'start',
			'end',
			'timestamp',
			'image'
		]

