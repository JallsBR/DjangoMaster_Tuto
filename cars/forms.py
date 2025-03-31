from django import forms
from cars.models import Car, Brand

"""
class CarForms(forms.Form):
    brand = forms.ModelChoiceField(Brand.objects.all())
    model = forms.CharField(max_length=100)
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()
    
    def save(self):
        car = Car(
            model = self.cleaned_data["model"],
            brand = self.cleaned_data["brand"],
            factory_year = self.cleaned_data["factory_year"],
            model_year = self.cleaned_data["model_year"],
            value = self.cleaned_data["value"],
            plate = self.cleaned_data["plate"],
            photo = self.cleaned_data["photo"],
        )
        car.save()
        return car
"""
class CarModelForms(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
    def clean_value(self):
        value = self.cleaned_data['value']
        if value < 20000:
            self.add_error('value', 'Valor minimo de R$ 20.000,00')  
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data['factory_year']
        if factory_year < 1970:
            self.add_error('factory_year', 'Não é possível cadastrar carros com ano de fabricação anterior a 1970')
        return factory_year
    
        