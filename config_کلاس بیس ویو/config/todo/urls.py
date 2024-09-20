from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.todo_detail_view),    # مشخص کردن شماره id   به صورت داینامیک در انتهای لینک
    path('cbv/', views.TodosListApiView.as_view()),  
    path('cbv/<int:todo_id>', views.TodosDetailApiView.as_view()),
]