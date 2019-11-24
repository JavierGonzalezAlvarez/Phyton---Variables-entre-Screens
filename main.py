__version__ = "1.0"

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

class ScreenManagement(ScreenManager):
    pass

class Manual_insert(Screen):
    name_x = StringProperty('')
    #room = StringProperty('')

    def update_info(self):
        self.name_x = self.ids.full_name.text
        print(self.name_x)

class First_room(Screen):
    names = StringProperty('')

    def on_pre_enter(self, *args):
        self.names = "Hola " + self.manager.ids.manual_insert.name_x # + ", - Your assigned room is: " + self.manager.ids.manual_insert.room


class Welcome(Screen):
    pass


class MainApp(App):
    def build(self):
        return ScreenManagement()


if __name__ == "__main__":
    MainApp().run()