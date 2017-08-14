from django import  forms
from .models import Registrado


class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre","email"]

	def clean_email(self):
		email =self.cleaned_data.get("email")
		email_base,proveedor = email.split("@")
		dominio,extension= proveedor.split(".")
		if not extension == "edu":
			raise forms.ValidationError("Por favor utiliza una extension valida .edu")
		return email


class ContactForm(forms.Form):
	"""docstring for RegForm"""
	nombre = forms.CharField(required=False)
	email = forms.EmailField()
	mensaje = forms.CharField(widget = forms.Textarea)

	