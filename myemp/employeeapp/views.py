from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from employeeapp.forms import EmployeeForm
from employeeapp.models import Employee, Order  # Import Order model
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST  # Add this import


def index(request):
    all_employee = Employee.objects.all()
    return render(request, 'index.html', {'all_employee': all_employee})

def employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save(commit=False)  # Don't save to the database yet
            employee.created_by = request.user  # Set the user who created the employee
            employee.save()  # Now save the employee
            messages.success(request, 'Employee added successfully!')
            return redirect('/')  # Redirect to avoid resubmission on refresh
    else:
        form = EmployeeForm()
    return render(request, 'employee.html', {'form': form})

def edit(request, id, emp_id):
    employee = get_object_or_404(Employee, id=id)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully!')
            return redirect('index')
    else:
        form = EmployeeForm(instance=employee)
        
    return render(request, 'edit_employee.html', {'form': form})

def delete(request, emp_id):
    emp = Employee.objects.get(pk=emp_id)
    emp.delete()
    messages.error(request, "ลบข้อมูลเรียบร้อย")
    return redirect(reverse('index'))

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after login
    return render(request, 'login.html')  # Render login template

def index_view(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = user.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, 'Registration successful!')
        return redirect('login')  # Redirect to login after registration
    return render(request, 'register.html')  # Render registration template

def user_employee_list(request):
    users = User.objects.all()  # Fetch all users
    employees = Employee.objects.all()  # Fetch all employees
    return render(request, 'user_employee_list.html', {'users': users, 'employees': employees})

def user_employee_list_by_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    employees = Employee.objects.filter(user=user)
    return render(request, 'user_employee_list_by_user.html', {'user': user, 'employees': employees})

def employee_list_by_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    employees = Employee.objects.filter(user=user)
    return render(request, 'employee_list_by_user.html', {'user': user, 'employees': employees})    

def employee_list_by_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    users = User.objects.filter(employee=employee)
    return render(request, 'employee_list_by_employee.html', {'employee': employee, 'users': users})

def admin_view(request):
    return render(request, 'admin.html')

def admin_employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'admin_employee_list.html', {'employees': employees})

def admin_employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'admin_employee_detail.html', {'employee': employee})

def admin_employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee created successfully!')
            return redirect('admin_employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'admin_employee_create.html', {'form': form})

def admin_employee_update(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)          
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully!')
            return redirect('admin_employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'admin_employee_update.html', {'form': form})    

def admin_employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    messages.success(request, 'Employee deleted successfully!')
    return redirect('admin_employee_list')

def order_employee(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    
    if request.user.is_authenticated:
        # Create an order record
        Order.objects.create(employee=employee, user=request.user)
        messages.success(request, f'Order placed for {employee.fname} {employee.lname}!')
    else:
        messages.error(request, 'You need to be logged in to place an order.')

    return redirect('user_employee_list')  # Redirect to the user employee list

# Add User View
def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, f'User {user.username} has been added successfully.')
        return redirect('user_employee_list')
    return render(request, 'user_employee_list.html')

# Edit User View
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        messages.success(request, f'User {user.username} has been updated successfully.')
        return redirect('user_employee_list')
    return render(request, 'edit_user.html', {'user': user})

# Delete User View
@require_POST
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, f'User {user.username} has been deleted successfully.')
    return redirect('user_employee_list')

