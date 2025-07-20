from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesKMConverter(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

MilesKMConverter().run()
