from django.urls import path
from . import views

app_name='myapp'
urlpatterns = [
	path('',views.index, name='index'),
	# myapp/post/id
	path('post/<int:pk>/', views.detail, name='detail'),
	path('P<pk>[0-9]/$', views.detail, name='detail'),
]