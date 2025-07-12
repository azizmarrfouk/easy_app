from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        
        self.label = Label(text="Hello World!", font_size=24)
        button = Button(text="Click Here", size_hint=(0.5, 0.3))
        button.bind(on_press=self.update_label)
        
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def update_label(self, instance):
        self.label.text = "Button Clicked Successfully!"

if __name__ == '__main__':
    MyApp().run()
