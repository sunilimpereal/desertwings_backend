from django.db import models

# Create your models here.


class Agent(models.Model):
    id              = models.AutoField(primary_key=True)
    first_name      = models.CharField(max_length=255)
    last_name       = models.CharField(max_length=255)
    password        = models.CharField(max_length=255,default="asd")
    contact_no      = models.CharField(max_length=255)
    email_id        = models.CharField(max_length=255,unique=True)
    company_name    = models.CharField(max_length=255)
    country         = models.CharField(max_length=255)
    state           = models.CharField(max_length=255)
    created_at      = models.DateTimeField()
    is_approved     = models.BooleanField(default=False)
    company_license = models.FileField(upload_to="company_license/", null=True)
    passport        = models.FileField(upload_to="passport/", null=True)
    national_id     = models.FileField(upload_to="national_id/", null=True)
    vat_number      = models.FileField(upload_to="vat_number/", null=True)
    def __str__(self):
        return self.first_name
