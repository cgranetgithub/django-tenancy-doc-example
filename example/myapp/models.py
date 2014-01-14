from django.db import models
from tenancy.models import AbstractTenant, TenantModel

class MyTenantModel(AbstractTenant):
   name = models.CharField(max_length=50)
   # other fields
   def natural_key(self):
      return (self.name, )

class Project(TenantModel):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=300, blank=True, null=True)

class Report(TenantModel):
  name = models.CharField(max_length=50)
  content = models.CharField(max_length=300, blank=True, null=True)
