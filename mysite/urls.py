from django.urls import path

from mysite import views
from django.urls import path, include

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   
   path('test/<str:asin>', views.index), 


   path('GetProduct/<int:id>', views.getproduct), 
    
   path('GetProductInfo/', views.send_json, name='send_json'),

   path('snippets/', login_required(views.YourView.as_view()), name='my_rest_view'),

]

