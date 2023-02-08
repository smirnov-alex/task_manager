from django.urls import path
from .views import home, tasks, description, task_del


urlpatterns = [
    path('category/<int:c_id>', tasks, name='tasks'),
    path('category/task/<int:task_id>/del', task_del, name='task_del'),
    path('category/task/<int:task_id>', description, name='description'),
    path('', home, name='home'),
]
