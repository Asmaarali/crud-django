from django.forms import ModelForm
from .models import userinfo


class Userinfo(ModelForm):
    class Meta:
        model = userinfo
        fields = "__all__"
