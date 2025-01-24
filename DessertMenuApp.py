from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class DessertMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text = 'Menu', font_size = 30, size_hint = (1, 0.1)))

        self.search_bar = TextInput(hint_text = "Search...", font_size = 30, size_hint = (1, 0.1))
        self.search_bar.bind(text = self.search_desserts)
        self.add_widget(self.search_bar)

        self.scroll_view = ScrollView(size_hint = (1, 0.7))
        self.menu = GridLayout(cols = 2, spacing = 10, size_hint_y = None)
        self.menu.bind(minimum_height = self.menu.setter('height'))

        self.desserts = [{"Name": "Black Forest", "image": "black_forest.jpg", "Price": "65 Bath"}, 
                         {"Name": "White Chocolate Cake", "image": "white_chocolate_cake.jpg", "Price": "65 Bath"}, 
                         {"Name": "Sour Cream Cheese Cake", "image": "sour_cream_cheese_cake.jpg", "Price": "70 Bath"}, 
                         {"Name": "Red Velvet", "image":"red_velvet_cake.jpg", "Price": "65 Bath"}, 
                         {"Name": "New York Cheese Cake", "image": "new_york_cheese_cake.jpg", "Price": "70 Bath"}, 
                         {"Name": "Macademia White Brownie", "image": "macademia_white_brownie.jpeg", "Price": "80 Bath"}, 
                         {"Name": "Lemon Cheese Pie", "image": "lemon_cheese_pie.jpg", "Price": "75 Bath"}, 
                         {"Name": "Green Tea Cake", "image": "green_tea_cake.jpg", "Price": "75 Bath"}, 
                         {"Name": "Cream Cheese Carrot Cake", "image":"cream_cheese_carrot_cake.jpg", "Price": "55 Bath"},
                         {"Name": "Banana Cake Cream Cheese", "image": "banana_cake_cream_cheese.jpg", "Price": "65 Bath"}, 
                         {"Name" : "Banoffee", "image": "banoffee.jpg", "Price": "65 Bath"}, 
                         {"Name": "Crepe Cake", "image": "crepe_cake.jpg", "Price": "65 Bath"}, 
                         {"Name": "Tiramisu", "image":"tiramisu.jpg", "Price": "80 Bath"}, 
                         {"Name": "Macarons", "image": "macarons.jpg", "Price": "40 Bath"}, 
                         {"Name": "Sugar Rush Donut", "image": "sugar_rush_donut.jpg", "Price": "35 Bath"}]
        
        self.buttons = []
        for dessert in self.desserts:
            dessert_layout = BoxLayout(orientation = 'vertical', size_hint_y = None, height = 200)

            img = Image(source = dessert["image"], size_hint = (1, 3))
            dessert_layout.add_widget(img)

            btn  = Button(text = f"{dessert['Name']}\n{dessert['Price']}", size = (1, 0.2))
            btn.bind(on_press = self.add_to_cart)
            dessert_layout.add_widget(btn)

            self.menu.add_widget(dessert_layout)
            self.buttons.append((btn, dessert["Name"], dessert["Price"]))

        self.scroll_view.add_widget(self.menu)
        self.add_widget(self.scroll_view)

        self.cart_label = Label(text = "Cart: 0 items", size_hint = (1, 0.1))
        self.add_widget(self.cart_label)

        self.checkout_button = Button(text = "Checkout", size_hint = (1, 0.1))
        self.checkout_button.bind(on_press = self.checkout)
        self.add_widget(self.checkout_button)

        self.reset_button = Button(text = "Reset Cart", size_hint = (1, 0.1))
        self.reset_button.bind(on_press = self.reset_cart)
        self.add_widget(self.reset_button)

        self.cart = []

    def search_desserts(self, instance, value):
        for btn, dessert_name in self.buttons:
            btn.parent.opacity = 1 if value.lower() in dessert_name.lower() else 0
        
    def add_to_cart(self, instance):
        dessert_name = instance.text
        if dessert_name:
            self.cart.append(dessert_name)
            self.update_cart_label()

    def update_cart_label(self):
        self.cart_label.text = f"Cart: {len(self.cart)} items"

    def checkout(self, instance):
        print("Checking out the following items: ")
        for item in self.cart:
            print(f"- {item}")
        self.cart = []
        self.update_cart_label()

    def reset_cart(self, instance):
        self.cart = []
        self.update_cart_label()

class DessertMenuApp(App):
    def build(self):
        return DessertMenu()
    
if __name__ == '__main__':
    DessertMenuApp().run()