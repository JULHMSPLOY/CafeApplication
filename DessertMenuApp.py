from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup

class DessertMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text = 'Menu', font_size = 30, size_hint = (1, 0.1)))

        self.search_bar = TextInput(hint_text = "Search...", font_size = 30, size_hint = (1, 0.1))
        self.search_bar.bind(text = self.search_desserts)
        self.add_widget(self.search_bar)

        self.recommendation_label = Label(text="Popular Desserts", font_size=20, size_hint=(1, 0.1))
        self.add_widget(self.recommendation_label)

        self.scroll_view = ScrollView(size_hint = (1, 0.7))
        self.menu = GridLayout(cols = 2, spacing = 10, size_hint_y = None)
        self.menu.bind(minimum_height = self.menu.setter('height'))

        self.desserts = [{"Name": "Black Forest", "image": "black_forest.jpg", "Price": "65.00 Bath", "stock": 5}, 
                         {"Name": "White Chocolate Cake", "image": "white_chocolate_cake.jpg", "Price": "65.00 Bath", "stock": 4}, 
                         {"Name": "Sour Cream Cheese Cake", "image": "sour_cream_cheese_cake.jpg", "Price": "70.00 Bath", "stock": 0}, 
                         {"Name": "Red Velvet", "image":"red_velvet_cake.jpg", "Price": "65.00 Bath", "stock": 6}, 
                         {"Name": "New York Cheese Cake", "image": "new_york_cheese_cake.jpg", "Price": "70.00 Bath", "stock": 1}, 
                         {"Name": "Macademia White Brownie", "image": "macademia_white_brownie.jpeg", "Price": "80.00 Bath", "stock": 0}, 
                         {"Name": "Lemon Cheese Pie", "image": "lemon_cheese_pie.jpg", "Price": "75.00 Bath", "stock": 3}, 
                         {"Name": "Green Tea Cake", "image": "green_tea_cake.jpg", "Price": "75.00 Bath", "stock": 0}, 
                         {"Name": "Cream Cheese Carrot Cake", "image":"cream_cheese_carrot_cake.jpg", "Price": "55.00 Bath", "stock": 2},
                         {"Name": "Banana Cake Cream Cheese", "image": "banana_cake_cream_cheese.jpg", "Price": "65.00 Bath", "stock": 4}, 
                         {"Name" : "Banoffee", "image": "banoffee.jpg", "Price": "65.00 Bath", "stock": 3}, 
                         {"Name": "Crepe Cake", "image": "crepe_cake.jpg", "Price": "65.00 Bath", "stock": 7}, 
                         {"Name": "Tiramisu", "image":"tiramisu.jpg", "Price": "80.00 Bath", "stock": 5}, 
                         {"Name": "Macarons", "image": "macarons.jpg", "Price": "40.00 Bath", "stock": 15}, 
                         {"Name": "Sugar Rush Donut", "image": "sugar_rush_donut.jpg", "Price": "35.00 Bath", "stock": 10}]
        
        self.buttons = []
        self.cart = []
        
        for dessert in self.desserts:
            dessert_layout = BoxLayout(orientation = 'vertical', size_hint_y = None, height = 250)

            img = Image(source = dessert["image"], size_hint = (1, 3))
            dessert_layout.add_widget(img)

            btn  = Button(text = f"{dessert['Name']}\n{dessert['Price']}", size = (2, 2))
            btn.bind(on_press = self.add_to_cart)
            if dessert["stock"] == 0:
                btn.disabled = True
            dessert_layout.add_widget(btn)

            count_spinner = Spinner(
                text='1', values=[str(i) for i in range(1, 11)], size_hint = (1, None), height = 35
            )
            count_spinner.bind(text = lambda spinner, value, dessert_name = dessert["Name"]: self.set_quantity(dessert_name, int(value)))
            dessert_layout.add_widget(count_spinner)

            self.menu.add_widget(dessert_layout)
            self.buttons.append((btn, dessert["Name"], dessert["Price"], count_spinner))

        self.scroll_view.add_widget(self.menu)
        self.add_widget(self.scroll_view)

        self.cart_label = Label(text = "Cart: 0 items", size_hint = (1, 0.1))
        self.add_widget(self.cart_label)

        self.total_label = Label(text = "Total: 0 Bath", size_hint = (1, 0.1))
        self.add_widget(self.total_label)

        self.checkout_button = Button(text = "Checkout", size_hint = (1, 0.1))
        self.checkout_button.bind(on_press = self.checkout)
        self.add_widget(self.checkout_button)

        self.reset_button = Button(text = "Reset Cart", size_hint = (1, 0.1))
        self.reset_button.bind(on_press = self.reset_cart)
        self.add_widget(self.reset_button)

        self.view_cart_botton = Button(text = "View Cart", size_hint = (1, 0.1))
        self.view_cart_botton.bind(on_press = self.view_cart)
        self.add_widget(self.view_cart_botton)

        self.confirm_button = Button(text="Confirm Order", size_hint=(1, 0.1))
        self.confirm_button.bind(on_press=self.confirm_order)
        self.add_widget(self.confirm_button)

        self.update_recommendations()

    def update_recommendations(self):
        popular_desserts = ["New York Cheese Cake", "Tiramisu", "Green Tea Cake"]
        recommended_text = "Popular Desserts: " + ", ".join(popular_desserts)
        self.recommendation_label.text = recommended_text

    def search_desserts(self, instance, value):
        for btn, dessert_name, _ in self.buttons:
            btn.parent.opacity = 1 if value.lower() in dessert_name.lower() else 0
        
    def add_to_cart(self, instance):
        for btn, dessert_name, dessert_price, count_spinner in self.buttons:
            if instance == btn:
                if btn.disabled:  
                    self.show_out_of_stock_message(dessert_name)
                    return
                price = float(dessert_price.split()[0])
                quantity = int(count_spinner.text)
                self.cart.append({"Name": dessert_name, "Price": price, "Quantity": quantity})
                self.update_cart_label()
                self.calculate_total_price()
                break

    def set_quantity(self, dessert_name, quantity):
        for item in self.cart:
            if item["Name"] == dessert_name:
                item["Quantity"] = quantity
                break
        else:
            price = float([d['Price'].split()[0] for d in self.desserts if d["Name"] == dessert_name][0])
            self.cart.append({"Name": dessert_name, "Price": price, "Quantity": quantity})
        self.update_cart_label()
        self.calculate_total_price()

    def update_cart_label(self):
        total_items = sum(item["Quantity"] for item in self.cart)
        self.cart_label.text = f"Cart: {total_items} items"

    def calculate_total_price(self):
        total_price = sum(float(item["Price"] * item["Quantity"]) for item in self.cart)
        self.total_label.text = f"Total: {total_price:.2f} Bath"

    def checkout(self, instance):
        print("Checking out the following items: ")
        for item in self.cart:
            print(f"- {item['Name']} x {item['Quantity']} - {item['Price']} Bath")
        total_price = sum(item["Price"] * item["Quantity"] for item in self.cart)
        print(f"Total amount: {total_price:.2f} Bath")
        self.cart = []
        self.update_cart_label()
        self.calculate_total_price()

    def reset_cart(self, instance):
        self.cart = []
        self.update_cart_label()
        self.calculate_total_price()

    def view_cart(self, instance):
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        for item in self.cart:
            content.add_widget(Label(
                text=f"{item['Name']} x {item['Quantity']} - {item['Price'] * item['Quantity']:.2f} Bath"
            ))
        total_price = sum(item["Price"] * item["Quantity"] for item in self.cart)
        content.add_widget(Label(text=f"Total: {total_price:.2f} Bath", bold=True))
        close_button = Button(text="Close", size_hint=(1, 0.2))
        content.add_widget(close_button)
        popup = Popup(title="Cart Items", content=content, size_hint=(0.8, 0.8))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def confirm_order(self, instance):
        print("Order confirmed!")

    def show_out_of_stock_message(self, dessert_name):
        popup = Popup(title="Out of Stock", content=Label(text=f"Sorry, {dessert_name} is out of stock!"), size_hint=(0.5, 0.5))
        popup.open()

class DessertMenuApp(App):
    def build(self):
        return DessertMenu()
    
if __name__ == '__main__':
    DessertMenuApp().run()