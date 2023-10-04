from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

class StopwatchApp(App):
    def build(self):
        self.time = 0
        self.is_running = False

        self.layout = BoxLayout(orientation='vertical', spacing=10)
        self.label = Label(text='00:00.00', font_size=48, size_hint=(1, 0.7))
        self.reset_button = Button(text='Reset', size_hint=(1, 0.1))

        self.reset_button.bind(on_press=self.reset)
        self.layout.bind(on_touch_down=self.toggle_timer)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.reset_button)

        return self.layout

    def update_time(self, interval):
        if self.is_running:
            self.time += interval
        minutes, seconds = divmod(int(self.time), 60)
        milliseconds = int((self.time - int(self.time)) * 100)
        self.label.text = f'{minutes:02d}:{seconds:02d}.{milliseconds:02d}'

    def toggle_timer(self, instance, touch):
        if touch.button == 'left' and self.reset_button.collide_point(*touch.pos):
            # Check if the touch event is on the reset button
            self.reset(None)
        elif touch.button == 'left':
            # Toggle the timer on a left-click anywhere else on the screen
            self.is_running = not self.is_running
            if self.is_running:
                Clock.schedule_interval(self.update_time, 0.01)
            else:
                Clock.unschedule(self.update_time)

    def reset(self, instance):
        self.is_running = False
        self.time = 0
        self.label.text = '00:00.00'

if __name__ == '__main__':
    app = StopwatchApp()
    app.run()
