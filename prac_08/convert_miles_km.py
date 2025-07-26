"""Min Thiha Khine (#14686570)"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_RATE = 1.60934


class MilesKMConverter(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    output_km = StringProperty('54.71756')
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
        self.output_km = str(kilometres)   # Use the StringProperty instead

    def handle_increment(self, change):
        """Adjust the miles input by +1 or -1 when Up/Down buttons are clicked."""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_conversion()

MilesKMConverter().run()
