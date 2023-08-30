from flask import (Blueprint,
                   render_template,
                   session,
                   url_for,
                   redirect,
                   request)

from store_models import Item
from store_models import db
from cart import set_cart
from forms import OrderForm
from mail_lib import send_mail

store_app = Blueprint('store_app',__name__,
                      template_folder='templates')

@store_app.route("/items")
def view_items():
    items = db.paginate(Item.query,per_page=16)
    return render_template("items.html",
                           items=items)


@store_app.route("/items/<int:item_number>")
def view_item(item_number):
    item = Item.query.filter(Item.id==item_number).first()
    return render_template("item.html",
                           item=item)


@store_app.route("/create_order",methods=["GET","POST"])
def create_order():
    set_cart(session)
    cart = session.get("cart")
    form = OrderForm()
    if request.method == "POST":
        form_data = request.form
        order = cart.create_order(form_data)
        db.session.add(order)
        db.session.commit()
        send_mail("Замовлення на сайті",
                  order.create_message_text(),
                  recipients=["egen13@ukr.net"])
        cart.clear()
        return "Замовлення було створене"
    return render_template("order.html",
                           form=form,
                           cart=cart)






    
