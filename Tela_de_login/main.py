from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
#from kivy.uix.floatlayout import FloatLayout


Builder.load_file('float_layout.kv')


class BancoLayout(Widget):
    def build(self):
        return Button
        return Image
        return Label
        return TextInput



class BancoFodasse(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return BancoLayout()


if __name__ == '__main__':
    BancoFodasse().run()