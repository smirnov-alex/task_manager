from django.urls import path
from .views import home, tasks, description, task_del, add_category, add_task, category_del, done_tasks, backup_task, \
    delete_done_tasks


urlpatterns = [
    path('category/<str:category>/add_task', add_task, name='add_task'),
    path('category/<int:c_id>', tasks, name='tasks'),
    path('category/task/<int:task_id>/del', task_del, name='task_del'),
    path('category/task/<int:task_id>', description, name='description'),
    path('add_category', add_category, name='add_category'),
    path('category/<int:c_id>/del', category_del, name='category_del'),
    path('done_tasks/<int:task_id>/backup_task', backup_task, name='backup_task'),
    path('done_tasks/delete', delete_done_tasks, name='delete_done_tasks'),
    path('done_tasks', done_tasks, name='done_tasks'),
    path('', home, name='home'),
]
