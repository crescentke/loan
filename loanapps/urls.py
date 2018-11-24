from django.urls import path

from loanapps.views import LoanAppList, Index, LoanAppDetail

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('apps/', LoanAppList.as_view(), name='apps'),
    path('apps/<slug>', LoanAppDetail.as_view(), name='app-detail'),
]
