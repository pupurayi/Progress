import uuid
from django.db import models
from django.utils import timezone
from django.contrib import admin

class Department(models.Model):
    dept_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    ROLE_CHOICES = (
         ('manager', 'Manager'),
        ('team_lead', 'Team Lead'),
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('tester', 'Tester'),
        ('product_owner', 'Product Owner'),
        ('business_analyst', 'Business Analyst'),
        ('technical_architect', 'Technical Architect'),
        ('project_manager', 'Project Manager'),
        ('hr_specialist', 'HR Specialist'),
    )
    employee_role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Tester')
    role = models.CharField(max_length=100, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


class Project(models.Model):
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
    )
    project_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'department','project_status','test_script.num')
    list_filter = ('department', 'budget')  # Add any fields you want to filter by
    search_fields = ('title', 'department')  # Add any fields you want to search by
    
class TestScript(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    description = models.TextField()
    employees = models.ManyToManyField(Employee)
    STATUS_CHOICES = (
        ('IN PROGRESS', 'In Progress'),
        ('OPEN', 'Open'),
        ('PASSED', 'Passed'),
        ('FAILED', 'Failed'),
        ('CLOSED', 'Closed'),
    )
    testscript_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CLOSED')
    comments = models.TextField(blank=True, null=True)
    attachment = models.FileField(upload_to='test_scripts', blank=True, null=True)
    pass_rate = models.IntegerField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='test_scripts')

    def start_testing(self):
        self.testscript_status = 'In Progress'
        self.save()

    def complete_testing(self, pass_rate):
        self.testscript_status = 'Closed'
        self.pass_rate = pass_rate
        self.save()      


class Assignment(models.Model):
    assignment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, blank=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, blank=False)
    role = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee.name} - {self.project.title}"