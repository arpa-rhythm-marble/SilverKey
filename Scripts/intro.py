import arcade
from enum import Enum
from Scripts.login import LoginView


class IntroPhase(Enum):
    BEGIN = 0
    WAIT = 1
    END = 2


class IntroView(arcade.View):
    def __init__(self):
        super().__init__()
        self.phase = IntroPhase.BEGIN
        self.frame = 0
        self.logo = arcade.Sprite('Resources/BloppyHB.png', scale=0.4)
        self.logo.set_position(960, 540)
        self.logo.alpha = 0

    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

    def on_update(self, _delta_time):
        if self.phase == IntroPhase.BEGIN:
            self.frame += 2
            self.logo.alpha = min(self.frame, 255)
            if self.frame > 255:
                self.frame = 0
                self.phase = IntroPhase.WAIT
        if self.phase == IntroPhase.WAIT:
            self.frame += 2
            if self.frame == 120:
                self.frame = 255
                self.phase = IntroPhase.END
        if self.phase == IntroPhase.END:
            self.frame -= 2
            self.logo.alpha = max(self.frame, 0)
            if self.frame < 0:
                login_scene = LoginView()
                self.window.show_view(login_scene)

    def on_draw(self):
        self.clear()
        self.logo.draw()
