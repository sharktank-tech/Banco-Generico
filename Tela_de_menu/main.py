from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file("layout.kv")

class TelaMenu_layout(Widget):
    def build(self):
        return Button
        return Label

class Banco_Arfly(App):
    def build(self):
        Window.clearcolor = (0,0,205)
        return TelaMenu_layout()


if __name__ == "__main__":
    Banco_Arfly().run()