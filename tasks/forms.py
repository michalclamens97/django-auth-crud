from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task #para que el formulario se base en el modelo de task, crea un formulario en base de mi tabla/modelo
        fields = ['title','description','important'] #eligo los campos del formulario en base a mi modelo
        widgets = {
            
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a task title'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter a description'}),
            'important': forms.CheckboxInput(attrs={'class':'form-check-input m-center'}),
            
            
            
            
        }