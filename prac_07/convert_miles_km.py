"""
CP1404 Practicals
Program to convert miles into km
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesToKilometer(App):
    def build(self):
        """Initial build for kivy"""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculator(self):
        """Convert miles value to km"""
        value = self.determine_validity()
        result = value * MILES_TO_KM
        self.root.ids.output_km.text = str(result)

    def handle_increment(self, change):
        """Increase input and output by one depending on button press"""
        value = self.determine_validity() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculator()

    def determine_validity(self):
        try:
            """Determines if user input is a number or not to prevent crashing"""
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometer().run()
