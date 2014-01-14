from django import forms
from django.contrib import admin
from myapp.models import MyTenantModel, Project, Report

admin.site.register(MyTenantModel)
admin.site.register(Project)
admin.site.register(Report)

def register_models_for_tenant(tenant):
    admin.site.register(Project.for_tenant(tenant))
    admin.site.register(Report.for_tenant(tenant))

# register all tenant specific at startup
for i in MyTenantModel.objects.all():
    register_models_for_tenant(i)

	
