import debug_toolbar
from django.urls import include, path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home, name='home'),
    path("<int:roomid>", views.index, name='index'),
    path('__debug__/', include(debug_toolbar.urls)),
    
    path('register/',views.registerUser, name='register'),
    path('login/', views.loginPage, name='login'),
    

]