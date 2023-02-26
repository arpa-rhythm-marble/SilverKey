import arcade

BLACK = arcade.color.BLACK
LOGIN = arcade.Sprite('Resources/login.png')


class LoginView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear()
        LOGIN.set_position(960, self.window.height - LOGIN.height / 2)
        LOGIN.draw()
