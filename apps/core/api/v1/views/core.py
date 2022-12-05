from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.commons.mixins.viewsets import ListCreateRetrieveViewSetMixin
from apps.core.models import Contact
from ..serializer.core import ContactSerializer


class ContactViewSet(ListCreateRetrieveViewSetMixin):
    queryset = Contact.objects.all()
    permission_classes = AllowAny,
    serializer_class = ContactSerializer
    lookup_field = 'uuid'
    lookup_kwarg = 'uuid'

