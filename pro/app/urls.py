from django.urls import path
from . import views

urlpatterns = [

    path('', views.add_member, name='add_member'),
    path('withdraw/', views.withdraw, name='withdraw'),
    # path('', views.add_member, name='add_member'),
    # other patterns


    path('add_money/', views.add_money, name='add_money'),
]
