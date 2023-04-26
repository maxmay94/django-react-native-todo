from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.ToDoListCreateAPIView.as_view(), name='todo_list_create'),
    path('todos/<int:pk>/', views.ToDoRetrieveUpdateDestroyAPIView.as_view(), name='todo_retrieve_update_destroy'),
    path('api-auth/', include('rest_framework.urls'))
]