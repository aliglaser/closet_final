from django.contrib.auth.models import(
	AbstractBaseUser,
	BaseUserManager,
	PermissionsMixin
)
from django.db import models
from django.utils import timezone
# Create your models here.



class UserManager(BaseUserManager):
	def create_user(self, email, first_name, last_name, username, display_name=None, password=None):
		if not email:
			raise ValueError("Users must have an email address")
		if not display_name:
			display_name = username

		user = self.model(
			email = self.normalize_email(email),
			first_name = first_name,
			last_name = last_name,
			username = username,
			display_name = display_name,
		)		

		user.set_password(password)
		user.save()
		return user


	def create_superuser(self, email, first_name, last_name, username, display_name, password):
		user = self.create_user(
			email,
			first_name,
			last_name,
			username,
			display_name,
			password
		)
		user.is_staff = True
		user.is_superuser = True
		user.save()
		return user


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	username = models.CharField(max_length=255, unique=True)
	display_name = models.CharField(max_length=140)
	bio = models.CharField(max_length=255, blank=True, default="")
	profile_pic = models.ImageField(blank=True, null=True, upload_to="closet/profile_pic")
	date_joined = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["first_name", "last_name", "username", "display_name"]

	def __str__(self):
		return "@{}".format(self.username)

	def get_full_name(self):
		return "{} {}".format(self.first_name, self.last_name)

	def get_short_name(self):
		return self.username








