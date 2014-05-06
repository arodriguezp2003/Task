from rest_framework import serializers
from .models import Organization, OrganizationUser

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Organization


class OrganizationUserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = OrganizationUser

