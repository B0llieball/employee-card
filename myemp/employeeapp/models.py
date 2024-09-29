from django.db import models
from django.contrib.auth.models import User

class Gender(models.TextChoices):
    MALE = 'MALE', 'Male'
    FEMALE = 'FEMALE', 'Female'
    OTHER = 'OTHER', 'Other'

class Department(models.TextChoices):
    HR = 'HR', 'Human Resource'
    IT = 'IT', 'Information Technology'
    FINANCE = 'FINANCE', 'Finance'
    MARKETING = 'MARKETING', 'Marketing'
    SALES = 'SALES', 'Sales'
    CUSTOMER_SERVICE = 'CUSTOMER_SERVICE', 'Customer Service'
    SUPPORT = 'SUPPORT', 'Support'
    ADMIN = 'ADMIN', 'Admin'

class Employee(models.Model):
    fname = models.CharField(max_length=100)  # First name
    lname = models.CharField(max_length=100)  # Last name
    address = models.TextField(null=True, blank=True)  # Make 'address' optional
    gender = models.CharField(max_length=10,
                             choices=Gender.choices,
                             default=Gender.MALE)  # Gender
    birthdate = models.DateField()  # Birthdate
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    department = models.CharField(max_length=100,
                                 choices=Department.choices,
                                 default=Department.HR)  # Department
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # Salary
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employees', null=True)  # Allow null values

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Order(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user.username} for {self.employee.fname} {self.employee.lname}"
