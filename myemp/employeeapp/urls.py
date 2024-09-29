from django.urls import path
from employeeapp import views
from django.conf import settings
from django.conf.urls.static import static
from employeeapp.views import login_view, register_view, admin_employee_list, admin_employee_detail, admin_employee_create, admin_employee_update, admin_employee_delete
from .views import add_user, edit_user, delete_user

urlpatterns = [
    path('login/', login_view, name='login'),  # Ensure this matches the login view
    path('register/', register_view, name='register'),  # Add this line
    path('', views.index, name='index'),
    path('employee', views.employee, name='employee'),
    path('user_employee_list/', views.user_employee_list, name='user_employee_list'),
    path('user_employee_list/<int:user_id>/', views.user_employee_list, name='user_employee_list_by_user'),
    path('employee_list_by_user/<int:user_id>/', views.employee_list_by_user, name='employee_list_by_user'),
    path('employee_list_by_employee/<int:employee_id>/', views.employee_list_by_employee, name='employee_list_by_employee'),
    path('admin_employee_list/', admin_employee_list, name='admin_employee_list'),
    path('admin_employee_detail/<int:employee_id>/', admin_employee_detail, name='admin_employee_detail'),
    path('admin_employee_create/', admin_employee_create, name='admin_employee_create'),
    path('admin_employee_update/<int:employee_id>/', admin_employee_update, name='admin_employee_update'),
    path('admin_employee_delete/<int:employee_id>/', admin_employee_delete, name='admin_employee_delete'),
    path('admin_employee_list/<int:employee_id>/', admin_employee_list, name='admin_employee_list_by_employee'),
    path('admin_employee_detail/<int:employee_id>/', admin_employee_detail, name='admin_employee_detail_by_employee'),
    path('admin_employee_create/<int:employee_id>/', admin_employee_create, name='admin_employee_create_by_employee'),
    path('admin_employee_update/<int:employee_id>/', admin_employee_update, name='admin_employee_update_by_employee'),
    path('admin_employee_delete/<int:employee_id>/', admin_employee_delete, name='admin_employee_delete_by_employee'),
    path('order/<int:emp_id>/', views.order_employee, name='order'),
    path('add_user/', add_user, name='add_user'),
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
]