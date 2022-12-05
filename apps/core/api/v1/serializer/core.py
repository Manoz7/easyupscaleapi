from rest_framework import serializers
from apps.commons.serializers import DynamicFieldsModelSerializer
from ....models import Contact


class ContactSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Contact
        read_only_fields = ('uuid', 'created_at', 'updated_at')
        fields = read_only_fields + ('name', 'email', 'subject', 'message')
