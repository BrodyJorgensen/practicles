from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculate(self, number):
        miles = self.convert_to_number(self.number)
        self.update_result(miles)
        return number

    def handle_increment(self, number, change):
        miles = self.convert_to_number(self.number) + change
        self.root.ids.input_miles.text = str(miles)
        # Since the InputText.text has changed, its on_text event will fire and handle_calculate will be called

    def update_result(self, miles):
        self.output_km = str(miles * MILES_TO_KM)

    def convert_to_number(self.number):
    try:
        value = float(number)
        return value
    except ValueError:
        return 0


MilesConverterApp().run()
