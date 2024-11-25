from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.home, name='home'), 
    path('', views.UserMixinClassGET.as_view()), 
    path('User/<int:pk>', views.UserMixinClassID.as_view()),
    path('auth/', include('rest_framework.urls')), 
]