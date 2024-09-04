from django.forms import ModelForm
import datetime
import pandas as pd

from django import forms
from .models import Loans


def date_dropdown():
    date_list = pd.date_range(datetime.date.today(), periods=21, freq='D')
    choice_set = []
    for index in date_list.strftime('%b-%d-%Y'):
        choice_set.append(tuple((index, index)))
    date_data = choice_set[6], choice_set[13], choice_set[20]
    drop_list = tuple(date_data)
    return drop_list


class LoansForm(ModelForm):
    class Meta:
        model = Loans
        fields = ['loaned_from','loaned_to',
                  'device_rma','eitms','loan_status',
                  'lyons_case', 'ot6_case', 'loan_return_date',
                 ]
        widgets = {
            'loaned_from': forms.RadioSelect(),
            'loaned_to': forms.RadioSelect(),
            'device_rma': forms.RadioSelect(),
            'loam_status': forms.CheckboxSelectMultiple(),
            'loan_return_date': forms.Select(choices=date_dropdown())
        }

    def __init__(self, *args, **kwargs):
        super(LoansForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

    def clean(self):
        super(LoansForm, self).clean()

        lions_case = self.cleaned_data['lyons_case']
        ot6_case = self.cleaned_data['ot6_case']

        match lions_case:
            case _ as length if len(lions_case) != 6:
                self._errors['lyons_case'] = self.error_class(['Lions Case number must be 6 digits'])
            case _ as digit if not digit.isdigit():
                self._errors['lyons_case'] = self.error_class(['Lions Case number must be all numbers'])

        return self.cleaned_data
