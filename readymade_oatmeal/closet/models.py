from django.conf import settings
from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField


# Create your models here.

CATEGORY_CHOICES = (
	('coat', 'coat'),
	('jacket', 'jacket'),
	('blazer', 'blazer'),
	('vest', 'vest'),
	('dress', 'dress'),
	('jumpsuit', 'jumpsuit'),
	('shirt/blouse', 'shirt/blouse'),
	('t-shirt', 't-shirt'),
	('tank top', 'tank top'),
	('bodysuit', 'bodysuit'),
	('sweatshirt', 'sweatshirt'),
	('sweater', 'sweater'),
	('cardigan', 'cardigan'),
	('pants', 'pants'),
	('jeans', 'jeans'),
	('leggings', 'leggings'),
	('shorts', 'shorts'),
	('skirt', 'skirt'),
	('shoes', 'shoes'),
	('bag', 'bag'),
	('accessory', 'accessory'),
	('etc', 'etc'),
)

SEASON_CHOICES = (
	('spring', 'spring'),
	('summer', 'summer'),
	('fall', 'fall'),
	('winter', 'winter'),
	('etc', 'etc'),
)

COLOR_CHOICES = (
	('black', 'black'),
	('grey', 'grey'),
	('white', 'white'),
	('beige', 'beige'),
	('brown', 'brown'),
	('metallic', 'metallic'),
	('purple', 'purple'),
	('blue', 'blue'),
	('green', 'green'),
	('yellow', 'yellow'),
	('orange', 'orange'),
	('pink', 'pink'),
	('off-white', 'off-white'),
	('red', 'red'),
	('neon', 'neon'),
	('etc', 'etc'),
)

PATTERN_CHOICES = (
	('animal print', 'animal print'),
	('camouflage', 'camouflage'),
	('floral', 'floral'),
	('gingham', 'gingham'),
	('plaid', 'plaid'),
	('polka dot', 'polka dot'),
	('solid', 'solid'),
	('striped', 'striped'),
)


class Photo(models.Model):
	file = models.ImageField(width_field='width_field', height_field='height_field', blank=True, null=True, upload_to="temp/", )
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)


class Clothes(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=255, default="")
	#description = models.CharField(max_length=255, default="")
	category = MultiSelectField(choices=CATEGORY_CHOICES)
	season = MultiSelectField(choices=SEASON_CHOICES)
	color = MultiSelectField(choices=COLOR_CHOICES)
	pattern = MultiSelectField(choices=PATTERN_CHOICES)
	photoid = models.IntegerField(default=0)
	photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="image")
	created_at = models.DateTimeField(auto_now_add=True)


	def get_absolute_url(self):
		return reverse('closet:detail', kwargs={"pk":self.id})

