from server.config import db
from server.app import app
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Mama's Pizza", address="123 Main Street")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Side Ave")

    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=12, pizza_id=p2.id, restaurant_id=r2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()