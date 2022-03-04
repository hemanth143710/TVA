from django.urls import path ,include
from api import views

urlpatterns = [
	path('User',views.UserList.as_view(),name='UserList'),
	path('User/<int:id>',views.UserDetail.as_view()),
]