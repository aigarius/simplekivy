from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.widget import Widget
from kivy.graphics import Line

from plyer.utils import platform

if platform == 'android':
    from jnius import autoclass


class Painter(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))
        if platform == 'android':
            PythonActivity = autoclass('org.renpy.android.PythonActivity')
            activity = PythonActivity.mActivity
            Context = autoclass('android.content.Context')
            vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)
            vibrator.vibrate(100)

    def on_touch_move(self, touch):
        touch.ud["line"].points += [touch.x, touch.y]


class MainScreen(Screen):
    pass


class AnotherScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("main.kv")


class MainApp(App):

    def build(self):
        return presentation

if __name__ == "__main__":
    MainApp().run()
