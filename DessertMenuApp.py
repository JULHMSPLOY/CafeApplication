from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class DessertMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text = 'Menu', font_size = 40, size_hint = (1, 0.1)))
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
        
class DessertMenuApp(App):
    def build(self):
        return DessertMenu()
    
if __name__ == '__main__':
    DessertMenuApp().run()