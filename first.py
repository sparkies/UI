import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties    import ObjectProperty
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.uix.button import Button


class XbeeGridLayout(FloatLayout):
    layout_content=ObjectProperty(None)
    global sound
    sound = SoundLoader.load('Antonio_vivaldi_Summer.mp3')

    def __init__(self, **kwargs):
        super(XbeeGridLayout, self).__init__(**kwargs)
        self.layout_content.bind(minimum_height=self.layout_content.setter('height'))
    
    def populate(self, g):
        for x in range(1, 101):
            g.add_widget(Button(text='Xbee ' + str(x)))
            g.add_widget(Label(text= 'Xbee ' + str(x) + ' description.'))

    def add_btn_pressed(self):
        sound.play()

    def rmv_btn_pressed(self):
        sound.stop()

    def read_btn_pressed(self):
        pass

class XbeeListApp(App):
    
    def build(self):
        return XbeeGridLayout()

xbeeApp = XbeeListApp()
xbeeApp.run()