from django import forms
# from bootstrap_datepicker.widgets import DatePicker


# class CountryForm(forms.Form):
#     OPTIONS = (
#         ("AUT", "Austria"),
#         ("DEU", "Germany"),
#         ("NLD", "Neitherlands"),
#     )
#     Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file', help_text='max. 42 megabytes')


class DateInput(forms.DateInput):
    input_type = 'date'


class ExampleForm(forms.Form):
    my_date_field = forms.DateField(widget=DateInput)

# class DateInput(DatePicker):
#     def __init__(self):
#         DatePicker.__init__(self,format="%Y-%m-%d")
#
#
class ExampleModelForm(forms.Form):
    class Meta:
        widgets = {
            'my_date_field': DateInput(),  # datepicker
            # 'creation_date': DateInput(), # datepicker
        }
        # fields = ("other fields", "date_of_birth", "creation_date", "other fields",)
        # model = get_user_model()
#
