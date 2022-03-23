from rest_framework import serializers
from PIL import Image, ImageDraw, ImageFont

from .models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('img', 'gender', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        try:
            img = Image.open(kwargs['data']['img'])
            width, height = img.size
            draw = ImageDraw.Draw(img)
            text = 'apptrix'
            font = ImageFont.truetype('arial.ttf', 36)
            textwidth, textheight = draw.textsize(text, font)
            margin = 10
            x = width - textwidth - margin
            y = height - textheight - margin
            draw.text((x, y), text, font=font)
            img.show()
            kwargs['data']['img'] = img
        except Exception as e:
            print(e)
        super(PersonSerializer, self).__init__(*args, **kwargs)
