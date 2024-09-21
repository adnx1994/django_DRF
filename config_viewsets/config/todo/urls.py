from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter  # برای استفاده از ویوستها

router = DefaultRouter()  # برای استفاده از ویوستها
router.register('', views.TodosViewSetApiView)   # برای استفاده از ویوستها


urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.todo_detail_view),    # مشخص کردن شماره id   به صورت داینامیک در انتهای لینک
    path('cbv/', views.TodosListApiView.as_view()),    # همان ساختار به صورت کلاس بیس ویو
    path('cbv/<int:todo_id>', views.TodosDetailApiView.as_view()),    # همان ساختار به صورت کلاس بیس ویو
    path('mixins/', views.TodosListMixinApiView.as_view()),
    path('mixins/<pk>', views.TodosDetailMixinApiView.as_view()),
    path('generics/', views.TodosGenericApiView.as_view()),
    path('generics/<pk>', views.TodosGenericDetailView.as_view()),
    path('viewsets/', include(router.urls)),  # برای استفاده از ویوستها
]