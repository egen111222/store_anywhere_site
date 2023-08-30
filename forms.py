from wtforms_alchemy import ModelForm
from auth_models import User
from store_models import Order


class UserForm(ModelForm):
    class Meta:
        model = User


class OrderForm(ModelForm):
    class Meta:
        model = Order
        only = ['name','phone']
