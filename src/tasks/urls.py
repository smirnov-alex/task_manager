from django.urls import path
from .views import home, tasks, description, task_del, add_category, add_task


urlpatterns = [
    path('category/<str:category>/add_task', add_task, name='add_task'),
    path('category/<int:c_id>', tasks, name='tasks'),
    path('category/task/<int:task_id>/del', task_del, name='task_del'),
    path('category/task/<int:task_id>', description, name='description'),
    path('add_category', add_category, name='add_category'),
    path('', home, name='home'),
]
