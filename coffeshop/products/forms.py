from django import forms
from coffeshop.products.models import Product



class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # widgets = {
        #     'product_image': forms.FileInput(attrs={'class': 'form-control-file'}),
        # }




class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'




class ProductDeleteForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.__set_disabled_fields()
    #
    # def save(self, commit=True):
    #     if commit:
    #         self.instance.delete()
    #
    #     return self.instance
    #
    # def __set_disabled_fields(self):
    #     for _, field in self.fields.items():
    #         field.widget.attrs['readonly'] = 'readonly'