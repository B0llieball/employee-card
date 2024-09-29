from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from employeeapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('employeeapp.urls')),
    path('admin/', admin.site.urls),
    path('userapp/', include('userapp.urls')),
    path('user_employee_list/', views.user_employee_list, name='user_employee_list'),
    path('employee/', views.employee, name='employee'),
    path('edit/<int:id>/<int:emp_id>/', views.edit, name='edit'),
    path('delete/<emp_id>/', views.delete, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
