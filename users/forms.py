from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#M Enterprises
#LightOne

class RegistrationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
        
class EditForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email','username',)