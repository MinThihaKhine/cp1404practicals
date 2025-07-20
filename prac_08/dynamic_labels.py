from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Creates Labels from a list of names"""

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ["Alex", "Alice", "Wendy", "Grace"]

    def build(self):
        """ Build the Kivy app from the kv file"""
        self.title = "Dynamic Label Generator"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            self.root.ids.main.add_widget(Label(text=name))
        return self.root


DynamicLabelsApp().run()