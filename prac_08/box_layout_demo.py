"""Min Thiha Khine (#14686570)"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build and return the root widget for the application"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the greet button click event"""
        print("greet")
        self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle the clear button click event"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""
BoxLayoutDemo().run()
