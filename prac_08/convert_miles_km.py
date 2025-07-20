from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

MILES_TO_KM_RATE = 1.60934


class MilesKMConverter(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def get_validated_miles(self):
        """get text input from text entry widget and convert to float, return 0 if error"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_conversion(self):
        """Convert validated miles value kilometres """
        value = self.get_validated_miles()
        kilometres = value * MILES_TO_KM_RATE
        self.root.ids.output_label.text = str(kilometres)



MilesKMConverter().run()
