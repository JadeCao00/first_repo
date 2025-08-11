class CoffeeMenu:
  def __init__(self):
    self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }
  def get_price(self, item_name):
    return self.menu[item_name]

  def add_item(self, item_name, price):
    if item_name in self.menu:
        raise ValueError(f"{item_name} is already in the menu")
    self.menu[item_name] = price
    return price

  def item_exists(self, item_name):
    return item_name in self.menu


