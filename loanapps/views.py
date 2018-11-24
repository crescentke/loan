from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from rest_framework import mixins, generics

from loanapps.models import LoanApp
from loanapps.serializers import LoanAppSerializer


class Index(View):
    def get(self, request):
        return HttpResponse('Loan Apps in Kenya')


class LoanAppList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = LoanApp.objects.all()
    serializer_class = LoanAppSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LoanAppDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    lookup_field = 'slug'
    queryset = LoanApp.objects.all()
    serializer_class = LoanAppSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
