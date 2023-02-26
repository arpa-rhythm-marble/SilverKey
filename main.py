import arcade
from Scripts import intro


class MainWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, style='borderless')
        self.set_location(0, 0)

        self.set_mouse_visible(False)
        self.cursor = arcade.Sprite('Resources/cursor_hand.png', scale=2)
        self.cursor_pos = (0, 0)

    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor_pos = (x, y)
        self.cursor.set_position(x + 30, y - 30)

    def on_draw(self):
        self.cursor.draw()


def main():
    window = MainWindow(1920, 1081, '백은열쇠')
    intro_scene = intro.IntroView()
    window.show_view(intro_scene)
    arcade.run()


if __name__ == '__main__':
    main()
