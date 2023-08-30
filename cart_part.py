from flask import (Blueprint,
                   render_template,
                   session,
                   url_for,
                   redirect)

from store_models import Item
from cart import set_cart

cart_app = Blueprint('cart_app', __name__,
                     template_folder='templates')


@cart_app.route("/add_to_cart/<int:item_number>")
def add_to_cart(item_number):
    set_cart(session)
    cart = session.get("cart")
    item = Item.query.filter(Item.id == item_number).first()
    if item:
        cart.add_item(item)
        return redirect(url_for("cart_app.view_cart"))
    return redirect(url_for("cart_app.view_cart"))

@cart_app.route("/cart")
def view_cart():
    set_cart(session)
    cart = session.get("cart")
    return render_template("cart.html",
                           cart=cart)


@cart_app.route("/clear_cart")
def clear_cart():
   set_cart(session)
   cart = session.get("cart")
   cart.clear()
   return redirect(url_for("cart_app.view_cart"))
