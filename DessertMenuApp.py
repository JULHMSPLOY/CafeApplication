from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class DessertMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

class DessertMenuApp(App):
    def build(self):
        return DessertMenu()
    
if __name__ == '__main__':
    DessertMenuApp().run()