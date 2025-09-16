from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Example Screens
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Welcome to My App", font_size=40))
        btn = Button(text="Go to Screen 1", size_hint=(1, 0.2))
        btn.bind(on_press=lambda x: self.manager.current = 'screen1')
        layout.add_widget(btn)
        self.add_widget(layout)

class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="This is Screen 1", font_size=30))
        btn = Button(text="Back to Home", size_hint=(1, 0.2))
        btn.bind(on_press=lambda x: self.manager.current = 'home')
        layout.add_widget(btn)
        self.add_widget(layout)

# Screen Manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(Screen1(name='screen1'))

# Main App
class MyNewApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyNewApp().run()
