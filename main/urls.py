import debug_toolbar
from django.urls import include, path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path("<int:roomid>", views.index, name='index'),
    path('home/', views.home, name='home'),
    path('__debug__/', include(debug_toolbar.urls)),

]