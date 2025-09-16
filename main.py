from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class SimpleChatApp(App):
    def build(self):
        self.chat_log = Label(size_hint_y=None, markup=True)
        self.chat_log.bind(texture_size=self.update_height)

        scroll = ScrollView()
        scroll.add_widget(self.chat_log)

        self.input_box = TextInput(size_hint_y=None, height=40, multiline=False)
        send_btn = Button(text="Send", size_hint_y=None, height=40)
        send_btn.bind(on_press=self.send_message)

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(scroll)
        layout.add_widget(self.input_box)
        layout.add_widget(send_btn)
        return layout

    def update_height(self, *args):
        self.chat_log.height = self.chat_log.texture_size[1]

    def send_message(self, instance):
        msg = self.input_box.text.strip()
        if msg:
            self.chat_log.text += f"[b]You:[/b] {msg}\n"
            self.input_box.text = ""

if __name__ == "__main__":
    SimpleChatApp().run()
