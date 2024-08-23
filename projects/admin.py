from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Employee, Project, Assignment, Department, TestScript


admin.site.register(Assignment)
admin.site.register(Department)

class TestScriptInline(admin.TabularInline):
    model = TestScript
    extra = 0
    fields = ('name', 'description', 'employees', 'testscript_status', 'comments', 'attachment', 'pass_rate')

class TestScriptAdmin(admin.ModelAdmin):
    list_display = ('name', 'employees', 'attachments', 'testscript_status')
    list_filter = ('testscript_status',)  # Add any fields you want to filter by
    search_fields = ('name', 'testscript_status')  # Add any 

    
@admin.register(TestScript)
class TestScriptAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'testscript_status')
    list_filter = ('project', 'testscript_status')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TestScriptInline]
    actions = ['add_test_script']

    def add_test_script(self, request, queryset):
        for project in queryset:
            TestScript.objects.create(project=project)
        self.message_user(request, f"{len(queryset)} test scripts were added.")
    add_test_script.short_description = 'Add Test Script'

    list_display = ('title', 'department', 'project_status', 'num_test_scripts')
    list_filter = ('department', 'budget')
    search_fields = ('title', 'department')

    def num_test_scripts(self, obj):
        return obj.test_scripts.count()
    num_test_scripts.short_description = 'Number of Test Scripts'
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'employee_role', 'department')
    search_fields = ('name', 'email' , 'department')
    list_filter = ('employee_role',)
    
