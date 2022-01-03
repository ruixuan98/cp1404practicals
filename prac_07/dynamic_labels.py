"""
CP1404 Practicals
Make a widget to add new names
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Initialize initial set of names and numbers"""
        super().__init__(**kwargs)
        self.names_and_numbers = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Main build of the kivy app"""
        self.title = ('Dynamic Labels')
        self.root = Builder.load_file('dynamic_labels.kv')
        self.show_labels()
        return self.root

    def show_labels(self):
        """Show dictionaries as labels"""
        for name in self.names_and_numbers:
            label_name = Label(text=name)
            self.root.ids.main.add_widget(label_name)

DynamicLabelsApp().run()