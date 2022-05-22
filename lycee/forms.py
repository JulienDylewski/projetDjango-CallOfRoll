from django.forms.models import ModelForm
from django import forms
from .models import Student, Presence , ParticularPresence
from django.forms.widgets import CheckboxSelectMultiple

class StudentForm(ModelForm):
  class Meta:
    # modele
    model = Student
    fields =(
      'first_name',
      'last_name',
      'birth_date',
      'email',
      'phone',
      'cursus',
      'comments',
    )

class PresenceForm(ModelForm):
  class Meta:
    model = Presence
    fields = [
      'date',
      'student'
      ]

    widgets = {
        'student' : CheckboxSelectMultiple()
    }

class ParticularPresenceForm(ModelForm):
  class Meta:
    model = ParticularPresence
    fields = [
      'date',
      'isMissing',
      'reason',
      'student'
      ]
