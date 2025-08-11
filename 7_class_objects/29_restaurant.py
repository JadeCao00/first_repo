class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.restaurant_name.title()} serves {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name.title()} is open now.")

restaurant_01 = Restaurant("yummy yummy", "chinese cuisine")
restaurant_01.describe_restaurant()

restaurant_02 = Restaurant("Subway", "fast food")
restaurant_02.open_restaurant()