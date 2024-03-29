from django.db import models

class ModelApi(models.Model):
    Name          = models.CharField(max_length=150, null=True, blank=True)
    City          = models.CharField(max_length=150, null=True, blank=True)
    State         = models.CharField(max_length=10, null=True, blank=True)
    Zip           = models.IntegerField(null=True, blank=True)
    Bank          = models.CharField(max_length=150, null=True, blank=True)
    BankState     = models.CharField(max_length=10, null=True, blank=True)
    NAICS         = models.IntegerField(null=True, blank=True)
    ApprovalDate  = models.DateField(null=True, blank=True)
    ApprovalFY    = models.DateField(null=True, blank=True)
    Term          = models.IntegerField(null=True, blank=True)
    NoEmp         = models.IntegerField(null=True, blank=True)
    NewExist      = models.IntegerField(null=True, blank=True)
    CreateJob     = models.IntegerField(null=True, blank=True)
    RetainedJob   = models.IntegerField(null=True, blank=True)
    DiffJobs      = models.IntegerField(null=True, blank=True)
    FranchiseCode = models.IntegerField(null=True, blank=True)
    UrbanRural    = models.IntegerField(null=True, blank=True)
    RevLineCr     = models.CharField(max_length=1, null=True, blank=True)
    LowDoc        = models.CharField(max_length=1, null=True, blank=True)
    GrAppv        = models.FloatField(null=True, blank=True)
    SBA_Appv      = models.FloatField(null=True, blank=True)
    MIS_Status    = models.BooleanField(null=True, blank=True)
    process_location = models.BooleanField(null=True, blank=True)
    process_bank = models.BooleanField(null=True, blank=True)
    process_activity = models.BooleanField(null=True, blank=True)
    process_bank_loan = models.BooleanField(null=True, blank=True)
    process_guaranteed_amount_requested = models.BooleanField(null=True, blank=True)
    process_sba_approuval = models.BooleanField(null=True, blank=True)
    process_status = models.IntegerField(null=True, blank=True, default='1')

    def __str__(self):
        return f'{self.Name}'