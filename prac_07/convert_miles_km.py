from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


MILES_TO_KM = 1.60934


class MilesToKilometer(app):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculator(self):
        try:
            result = float(input)
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass
