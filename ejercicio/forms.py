from django import forms
from django.core.exceptions import ValidationError
import re
from .models import Universidad


class UniversidadForm(forms.ModelForm):

    class Meta:
        model = Universidad
        fields = [
            "nombre_completo",
            "matricula",
            "correo",
            "telefono",
            "rfc",
            "contra"
        ]

        widgets = {

            "nombre_completo": forms.TextInput(attrs={
                'class': 'form-control',
                'pattern': '^[A-Za-zÁÉÍÓÚáéíóúÑñ ]{10,}$',
                'title': 'Solo letras y espacios. Mínimo 10 caracteres'
            }),

            "matricula": forms.TextInput(attrs={
                'class': 'form-control',
                'pattern': '^[0-9]{5}[A-Za-z]{2}[0-9]{3}$',
                'title': 'Formato: 5 dígitos, 2 letras y 3 dígitos (ej. 12345AB678)'
            }),

            "correo": forms.EmailInput(attrs={
                'class': 'form-control',
                'pattern': '^[a-zA-Z0-9._%+-]+@utez\\.edu\\.mx$',
                'title': 'Debe terminar en @utez.edu.mx'
            }),

            "telefono": forms.TextInput(attrs={
                'class': 'form-control',
                'pattern': '^[0-9]{10}$',
                'title': 'Debe contener exactamente 10 dígitos'
            }),

            "rfc": forms.TextInput(attrs={
                'class': 'form-control',
                'pattern': '^[A-Z]{4}[0-9]{6}[A-Z0-9]{3}$',
                'title': 'RFC en mayúsculas: 4 letras, 6 números y 3 alfanuméricos'
            }),

            "contra": forms.PasswordInput(attrs={
                'class': 'form-control',
                'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$',
                'title': 'Mínimo 8 caracteres, una mayúscula, una minúscula, un número y un símbolo'
            }),
        }

    # ================= VALIDACIONES BACKEND =================

    def clean_nombre_completo(self):
        data = self.cleaned_data['nombre_completo']
        if not re.fullmatch(r'[A-Za-zÁÉÍÓÚáéíóúÑñ ]{10,}', data):
            raise ValidationError(
                "El nombre solo puede contener letras y espacios (mínimo 10 caracteres)."
            )
        return data

    def clean_matricula(self):
        data = self.cleaned_data['matricula']
        if not re.fullmatch(r'[0-9]{5}[A-Za-z]{2}[0-9]{3}', data):
            raise ValidationError(
                "La matrícula debe tener el formato: 5 dígitos, 2 letras y 3 dígitos."
            )
        return data

    def clean_correo(self):
        data = self.cleaned_data['correo']
        if not re.fullmatch(r'[a-zA-Z0-9._%+-]+@utez\.edu\.mx', data):
            raise ValidationError(
                "El correo debe ser institucional y terminar en @utez.edu.mx."
            )
        return data

    def clean_telefono(self):
        data = self.cleaned_data['telefono']
        if not re.fullmatch(r'[0-9]{10}', data):
            raise ValidationError(
                "El teléfono debe contener exactamente 10 dígitos."
            )
        return data

    def clean_rfc(self):
        data = self.cleaned_data['rfc']
        if not re.fullmatch(r'[A-Z]{4}[0-9]{6}[A-Z0-9]{3}', data):
            raise ValidationError(
                "El RFC debe estar en mayúsculas y tener el formato correcto."
            )
        return data

    def clean_contra(self):
        data = self.cleaned_data['contra']
        if not re.fullmatch(
            r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}', data
        ):
            raise ValidationError(
                "La contraseña debe tener mínimo 8 caracteres, una mayúscula, "
                "una minúscula, un número y un símbolo."
            )
        return data