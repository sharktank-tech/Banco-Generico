from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.textinput import TextInput



Builder.load_file('layout.kv')


class TelaLogin_layout(Widget):
    def build(self):
        return Button
        return Image
        return Label
        return TextInput



class Banco_Arfly(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return TelaLogin_layout()


if __name__ == '__main__':
    Banco_Arfly().run()