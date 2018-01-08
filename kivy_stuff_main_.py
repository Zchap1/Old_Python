from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line


class Painter(Widget):

    def on_touch_down(self, touch):
            with self.canvas:
                touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self,touch):
        touch.ud["line"].points += [touch.x, touch.y]
    

class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class newboard(Screen):
    pass



presentation = Builder.load_file("kivy_stuff.kv")

class MainApp(App):
    def build(self):
        return presentation

MainApp().run()
