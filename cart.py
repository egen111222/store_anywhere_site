# Додати товар
# Очистити корзину
# Вирахувати вартість
# Дізнатись кількість товарів
# Створити замовлення
from store_models import Order
from datetime import date

class Cart:
    def __init__(self):
        self.items = []
        
    def add_item(self,item):
        last_ids_items = [item.id for item in self.items]
        if item.id not in last_ids_items:
            self.items.append(item)
        
    def clear(self):
        self.items.clear()
        
    def get_price(self):
        price = 0
        for item in self.items:
            price += item.price
        return price

    
    def get_count(self):
        return len(self.items)
    
    def create_order(self,form_data):

        order = Order(name=form_data.get("name"),
                      phone=form_data.get("phone"),
                      price=self.get_price(),
                      date=date.today())
        for item in self.items:
            order.items.append(item)
        return order


def set_cart(session):
    if "cart" not in session:
        session["cart"] = Cart()





        
