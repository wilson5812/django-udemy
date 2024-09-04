from django.db import models
import uuid
import datetime
import pandas as pd
# Create your models here.


class Loans(models.Model):
    STATUS_TYPE = (
        ('Current', 'Current Loan'),
        ('Returned', 'Returned Loan'),
    )
    LOAN_FROM_TYPE = (
        ('FromPS', 'Loaned from PS'),
        ('FromTS', 'Loaned from TS'),
        ('FromPods', 'Loaned from Autopods'),
        ('FromTeams', 'Loaned from Teamgear'),
    )
    LOAN_TO_TYPE = (
        ('ToPS', 'Loaned to PS'),
        ('ToTS', 'Loaned to TS'),
        ('ToPods', 'Loaned to Autopods'),
        ('ToTeams', 'Loaned to Teamgeear'),
    )
    RMA_TYPE = (
        ('RMA', 'RMA Device'),
    )

    loaned_from = models.CharField(max_length=50, choices=LOAN_FROM_TYPE, default='FromPS', blank=True)
    loaned_to = models.CharField(max_length=50, choices=LOAN_TO_TYPE, default='ToTS', blank=True)
    device_rma = models.CharField(max_length=20, choices=RMA_TYPE, blank=True)
    eitms = models.CharField(max_length=35,null=True,blank=True)
    ot6_case = models.CharField(max_length=75,null=True,blank=True)
    lyons_case = models.CharField(max_length=75,null=True,blank=True)
    loan_status = models.CharField(max_length=75, choices=STATUS_TYPE, default="Current")
    loan_return_date = models.CharField(max_length=50, null=True,blank=True)
    returned_date = models.CharField(max_length=50, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                      unique=True, editable=False)

    def __str__(self):
        return self.eitms