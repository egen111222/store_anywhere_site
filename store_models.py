from models import db

category_item_table = db.Table("category_item_table",
                               db.Column("item_id",db.ForeignKey("items.id")),
                               db.Column("category_id",db.ForeignKey("categories.id")))

order_item_table = db.Table("order_item_table",
                            db.Column("item_id",db.ForeignKey("items.id")),
                            db.Column("order_id",db.ForeignKey("orders.id")))


class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(250))
    price = db.Column(db.Float())
    categories = db.relationship("Category",
                                 secondary=category_item_table,
                                 back_populates="items")
    img = db.Column(db.String(150))

    def __str__(self):
        return self.name

    def create_message_text(self):
        return f"""Назва товару - {self.name}
Ціна товару - {self.price}"""


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(250))
    items = db.relationship("Item",
                                 secondary=category_item_table,
                                 back_populates="categories")
    img = db.Column(db.String(150))
    
    def __str__(self):
        return self.name


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(150))
    phone = db.Column(db.String(50))
    price = db.Column(db.Float)
    date = db.Column(db.Date)
    items = db.relationship("Item",
                            secondary=order_item_table)

    def create_message_text(self):
        text = f"""Замовлення оформлене {self.name}
З Телефоном {self.phone}
Було виконано  {self.date}
Загальна ціна: {self.price}"""
        text += f"\n{'-'*35}\n"
        for item in self.items:
            text += item.create_message_text()
            text += f"\n{'-'*35}\n"
        return text
    
    

