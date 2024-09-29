from django import forms
from employeeapp.models import Employee, Department, Gender

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fname', 'lname','picture', 'gender', 'birthdate', 'department', 'salary', 'address']  # Add 'address'

        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'picture': 'Picture',
            'gender': 'Gender',
            'birthdate': 'Birthdate',
            'department': 'Department',
            'salary': 'Salary',
            'address': 'Address',
        }

        widgets = {
            'address': forms.Textarea(attrs={'rows': '4'}),  # Make 'address' a textarea
            'gender': forms.RadioSelect(choices=Gender.choices),
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'department': forms.Select(choices=Department.choices),
        }
