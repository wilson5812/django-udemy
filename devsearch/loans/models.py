from django.db import models
import uuid
import datetime
import pandas as pd
# Create your models here.
def date_dropdown():
    date_list = pd.date_range(datetime.date.today(), periods=21, freq='D')
    choice_set = []
    for index in date_list.strftime('%Y-%d-%m'):
        choice_set.append(tuple((index, index)))

    drop_list = tuple(choice_set)
    return drop_list


class Loans(models.Model):
    STATUS_TYPE = (
        ('Current', 'Current Loan'),
        ('Returned', 'Returned Loan'),
    )
    RECORD_TYPE = (
        ('FromPS', 'Loaned from PS'),
        ('ToPS', 'Loaned to PS'),
        ('FromPods', 'Loaned from Autopods'),
        ('ToPods', 'Loaned to Autopods'),
        ('RMA', 'RMA Device'),
    )
    #LOAN_DATES = date_dropdown()
    record_type = models.CharField(max_length=20, choices=RECORD_TYPE, default='FromPS', blank=True)
    eitms = models.CharField(max_length=35,null=True,blank=True)
    ot6_case = models.CharField(max_length=75,null=True,blank=True)
    lyons_case = models.CharField(max_length=75,null=True,blank=True)
    loan_status = models.CharField(max_length=75, choices=STATUS_TYPE, default="Current", blank=True)
    loan_return_date = models.DateField(null=True,blank=True)
    returned_date = models.DateTimeField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                      unique=True, editable=False)

    def __str__(self):
        return self.eitms