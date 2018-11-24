from rest_framework import serializers

from loanapps.models import LoanApp


# LoanApp
class LoanAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApp
        fields = ('id', 'name', 'rating', 'app_url', 'logo', 'description', 'slug',)
