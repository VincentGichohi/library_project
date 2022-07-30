
from django.urls import path
from .views BookAPIView

urlpatterns  =[
    path('', BookAPIView.as_view()),

]