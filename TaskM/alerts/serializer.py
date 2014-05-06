from rest_framework import serializers
from .models import Alert
class AlertSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Alert
