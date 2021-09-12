from django.urls import path
from .views import HomeageView

urlpatterns=[
    path('',HomeageView.as_view(),name='home')
]