from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserCreateForm(UserCreationForm):
	class Meta:
		fields = ("email", "first_name", "last_name", "username", "display_name", "password1", "password2")
		model = get_user_model()

	def __init__(self, *args, **kwargs):	
		super().__init__(*args, **kwargs)
		self.fields["email"].label = "Email address"
		self.fields["first_name"].label = "First name"
		self.fields["last_name"].label = "Last name"
		self.fields["username"].label = "User name"
		self.fields["display_name"].label = "Nick name"
		
		