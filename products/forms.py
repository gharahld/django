from django import forms

from .models import Product





class ProductForm(forms.ModelForm):
    tittle = forms.CharField(label='',
                             widget=forms.TextInput(attrs={"placeholder": "Your tittle"}))
    #email  = forms.EmailField()

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 10,
                "cols": 120

            }
        )
    )
    price = forms.DecimalField(initial=1.99)

    class Meta:
        model = Product
        fields = [
            'tittle',
            'description',
            'price'
        ]

    #
    # def clean_tittle(self,*args,**kwargs):
    #     tittle = self.cleaned_data.get("tittle")
    #     if not "CFE" in tittle:
    #         raise forms.ValidationError("This is not a valid tittle")
    #         return tittle
    #
    #
    #
    #
    #
    #
    # def clean_email(self,*args,**kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("This is not a valid email")
    #         return email


class RawProductForm(forms.Form):
    tittle         = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder": "Your tittle"}))
    description    = forms.CharField(
                           required=False,
                           widget=forms.Textarea(
                               attrs={
                                   "class": "new-class-name two",
                                   "id": "my-id-for-textarea",
                                   "rows":10,
                                   "cols":120

                               }
                           )
    )
    price          = forms.DecimalField(initial=1.99)