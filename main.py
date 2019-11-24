__version__ = "1.0"

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

class ScreenManagement(ScreenManager):
    pass

class Manual_insert(Screen):
    name_x = StringProperty('')

    def update_info(self):
        self.name_x = self.ids.full_name.text
        print(self.name_x)

class Greetings(Screen):
    names = StringProperty('')
    def on_pre_enter(self, *args):
        self.names = "Hola " + self.manager.ids.manual_insert.name_x 

class MainApp(App):
    def build(self):
        return ScreenManagement()

if __name__ == "__main__":
    MainApp().run()