from django.forms import ModelForm, DateInput
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        
        #work around to make date time fields show up on HTML5 input
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        #input formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-dT%H:%M')