import arcade
from Scripts.intro import IntroView


def main():
    window = arcade.Window(1920, 1081, '백은열쇠', style='borderless')
    window.set_location(0, 0)
    intro_scene = IntroView()
    window.show_view(intro_scene)
    arcade.run()


if __name__ == '__main__':
    main()
