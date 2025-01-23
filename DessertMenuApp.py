from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class DessertMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text = 'Menu', font_size = 40, size_hint = (1, 0.1)))

        self.search_bar = TextInput(hint_text = "Search...", font_size = 30, size = (1, 0.1))
        self.search_bar.bind(text = self.search_desserts)
        self.add_widget(self.search_bar)

        self.scroll_view = ScrollView(size_hint = (1, 0.5))
        self.menu = GridLayout(cols = 1, spacing = 5, size_hint_y = None)
        self.menu.bind(minimum_height = self.menu.setter('height'))

        self.desserts = [{"Name": "Black Forest"}, 
                         {"Name": "White Chocolate Cake"}, 
                         {"Name": "Sour Cream Cheese Cake"}, 
                         {"Name": "Red Velvet"}, 
                         {"Name": "New York Cheese Cake"}, 
                         {"Name": "Macademia White Brownie"}, 
                         {"Name": "Lemon Cheese Pie"}, 
                         {"Name": "Green Tea Cake"}, 
                         {"Name": "Cream Cheese Carrot Cake"},
                         {"Name": "Banana Cake Cream Cheese"}, 
                         {"Name" : "Banoffee"}, 
                         {"Name": "Crepe Cake"}, 
                         {"Name": "Tiramisu"}, 
                         {"Name": "Macarons"}, 
                         {"Name": "Sugar Rush Donut"}]
        
        self.buttons = []
        for dessert in self.desserts:
            dessert_layout = BoxLayout(orientation = 'vertical', size_hint_y = None, height = 100)

            btn  = Button(text = dessert["Name"], size = (1, 0.2))
            btn.bind(on_press = self.add_to_cart)
            dessert_layout.add_widget(btn)

            self.menu.add_widget(dessert_layout)
            self.buttons.append((btn, dessert["Name"]))

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
        
    def add_to_cart(self, instance):
        dessert_name = instance.text
        if dessert_name and dessert_name not in self.cart:
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