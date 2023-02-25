import arcade

BLACK = arcade.color.BLACK


class LoginView(arcade.View):
    def __init__(self):
        super().__init__()
        self.dt = 0.1

    def on_update(self, delta_time):
        self.dt = delta_time

    def on_draw(self):
        self.clear()
        arcade.draw_text('Hello World!', 12, 1045, BLACK, 24)
        arcade.draw_text(f"{round(1 / self.dt, 1)} FPS", 12, 1021, BLACK, 24)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            self.window.close()
