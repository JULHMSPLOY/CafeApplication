from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class DessertMenu(BoxLayout):
    pass

class DessertMenuApp(App):
    def build(self):
        return DessertMenu()
    
if __name__ == '__main__':
    DessertMenuApp().run()