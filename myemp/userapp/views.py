from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import UserRole
from django.contrib.auth.models import User
from employeeapp.models import Employee
from employeeapp.views import employee

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        checkpassword = request.POST['checkpassword']
        if username =="" or password == "" or checkpassword == "":
            messages.warning(request, "กรุณากรอกข้อมูลให้ครบถ้วน")
            return redirect(reverse('register'))
        else:
            if password == checkpassword:
                if User.objects.filter(username=username).exists():
                    messages.warning(request, "ชื่อผู้ใช้นี้มีผู้ใช้งานแล้ว")
                    return redirect(reverse('register'))
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    messages.success(request, "สมัครสมาชิกสำเร็จ")
                    return redirect(reverse('login'))
            else:
                messages.warning(request, "รหัสผ่านไม่ตรงกัน")
                return redirect(reverse('register'))
    else:
        return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == "" or password == "":
            messages.warning(request, "กรุณากรอกข้อมูลให้ครบถ้วน")
            return redirect(reverse('login'))
        else:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(reverse('index'))
            else:
                messages.warning(request, "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
                return redirect(reverse('login'))
    else:
        return render(request, 'login.html')
    
def user_logout(request):
    auth.logout(request)
    return redirect(reverse('index'))

def logout_view(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to the index page after logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to home after login
    return render(request, 'login.html')  # Render login template for GET requests

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, 'Registration successful!')
        return redirect('login')  # Redirect to login after registration
    return render(request, 'register.html')  # Render registration template for GET requests

def home_view(request):
    return render(request, 'index.html')  # Ensure this matches the template name

def index_view(request):
    return render(request, 'index.html')  # Ensure this matches the template name

def logout_landing_view(request):
    return render(request, 'logout_landing.html')  # Ensure this matches the template name

def add_employee_view(request):
    return render(request, 'add_employee.html')  # Ensure this matches the template name

def employee_list_view(request):
    return render(request, 'employee_list.html')  # Ensure this matches the template name

def update_employee_view(request):
    return render(request, 'update_employee.html')  # Ensure this matches the template name

def delete_employee_view(request):
    return render(request, 'delete_employee.html')  # Ensure this matches the template name

def employee_details_view(request):
    return render(request, 'employee_details.html')  # Ensure this matches the template name

def employee_delete_view(request):
    return render(request, 'employee_delete.html')  # Ensure this matches the template name

def employee_update_view(request):
    return render(request, 'employee_update.html')  # Ensure this matches the template name

def employee_create_view(request):
    return render(request, 'employee_create.html')  # Ensure this matches the template name

def employee_list_view(request):
    return render(request, 'employee_list.html')  # Ensure this matches the template name

def employee_detail_view(request):
    return render(request, 'employee_detail.html')  # Ensure this matches the template name

def employee_delete_view(request):
    return render(request, 'employee_delete.html')  # Ensure this matches the template name

def employee_update_view(request):
    return render(request, 'employee_update.html')  # Ensure this matches the template name

def employee_create_view(request):
    return render(request, 'employee_create.html')  # Ensure this matches the template name

def employee_list_view(request):
    return render(request, 'employee_list.html')  # Ensure this matches the template name

def employee_detail_view(request):
    return render(request, 'employee_detail.html')  # Ensure this matches the template name

def role_list(request):
    roles = UserRole.objects.all()
    return render(request, 'role_list.html', {'roles': roles})

def add_role(request):
    if request.method == 'POST':
        role_name = request.POST['name']
        UserRole.objects.create(name=role_name)
        messages.success(request, 'Role added successfully.')
        return redirect('role_list')
    return render(request, 'add_role.html')

def edit_role(request, role_id):
    role = get_object_or_404(UserRole, id=role_id)
    if request.method == 'POST':
        role.name = request.POST['name']
        role.save()
        messages.success(request, 'Role updated successfully.')
        return redirect('role_list')
    return render(request, 'edit_role.html', {'role': role})

def delete_role(request, role_id):
    role = get_object_or_404(UserRole, id=role_id)
    role.delete()
    messages.success(request, 'Role deleted successfully.')
    return redirect('role_list')

def user_employee_list(request):    
    users = User.objects.all()
    employees = Employee.objects.all()
    return render(request, 'user_employee_list.html', {'users': users, 'employees': employees})















