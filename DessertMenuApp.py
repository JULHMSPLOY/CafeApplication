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

        self.desserts = [
            {"name": "Chocolate Cake"},
            {"name": "Strawberry Tart"},
            {"name": "Blueberry Muffin"},
            {"name": "Ice Cream Sundae"},
            {"name": "Apple Pie"},
            {"name": "Lemon Cheesecake"},
            {"name": "Brownies"},
            {"name": "Pancakes"},
            {"name": "Macarons"},
            {"name": "Cupcakes"},
        ]
        
class DessertMenuApp(App):
    def build(self):
        return DessertMenu()
    
if __name__ == '__main__':
    DessertMenuApp().run()