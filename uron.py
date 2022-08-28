from ursina import *
from ursina import curve
from player import Player
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina(borderless=False)
window.exit_button.enabled = True
window.cog_button.enabled = True
window.fps_counter.enabled = False
window.exit_button.text = ''
window.exit_button.color = color.gray
window.exit_button.texture = "sword"
window.cog_menu.enabled = False
window.title = 'Urono'
window.icon = 'duh.png'

Sky()

player = Player("cube", (0, 10, 0), "box")
player.SPEED = 3
player.jump_height = 0.5
ground = Entity(model='cube', texture='assets/hrllohrllo', collider='mesh', position=(
    0, 0, 0), scale=(7, 2, 7), shader=lit_with_shadows_shader)

FPC_POS = player.position

background = Audio(
    'audio/urono-cheerbeat-background',
    loop=True,
    autoplay=True
)

quM = Audio(
    'audio/quit',
    loop=False,
    autoplay=False
)

grappler = Entity(parent=camera.ui, model='assets/grappler.obj', position=(0.8, -0.4, 0), scale=(0.25, 0.25, 0.25),
                  color=color.red, texture="white_cube", rotation=(-10, -10, -10), shader=lit_with_shadows_shader)


class Grapple(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            model="cube",
            texture="assets/grappler_texture",
            collider="box",
            position=position,
            shader=lit_with_shadows_shader,
            scale=(10, 10, 10)
        )

        self.player = player

    def update(self):
        self.on_click = Func(self.player.animate_position,
                             self.position, duration=0.5, curve=curve.linear)

        ray = raycast(self.player.position, self.player.forward,
                      distance=0.5, ignore=[player, ])

        if ray.entity == self:
            self.player.y += 2


class Platform(Entity):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            model="cube",
            scale=(7, 2, 7),
            texture="grappler_texture",
            collider="box",
            position=position,
            shader=lit_with_shadows_shader
        )


class Portal(Entity):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            model="assets/portal.obj",
            scale=(2, 4, 2),
            texture="portal_texture",
            collider="box",
            position=position,
            shader=lit_with_shadows_shader
        )


FPC_POS_text = Text("", scale=2, x=0.2, y=0.2)
QUIT_WARN_text = Text("", scale=2, x=0.2, y=0.2)


Platform(Vec3(1, -1, -27.2754))
Platform(Vec3(0.0640625, 0.00125, -53.2754))
Platform(Vec3(0.169236, 14.3008, -33.3041))
Platform(Vec3(-0.886462, 7.42754, -73.0878))
Platform(Vec3(-1.10773, 12.6191, -90.2041))
Platform(Vec3(-1.3286, 19.5097, -107.289))
Platform(Vec3(-1.55644, 25.4606, -124.914))
Platform(Vec3(-2.07368, 25.0602, -164.926))
Platform(Vec3(-4.56876, 24.3813, -206.787))
Platform(Vec3(-6.55665, 36.2641, -210.516))
Platform(Vec3(-5.2145, 24.7415, -232.169))
Platform(Vec3(-8.12956, 19.0883, -313.253))
Grapple(Vec3(-7.73628, 24.0123, -262.297))
Platform(Vec3(-8.12433, 26.1495, -245.986))
Platform(Vec3(6.65358, 20.0725, -312.287))
Platform(Vec3(25.9705, 20.3887, -312.661))
Platform(Vec3(44.783, 20.6966, -313.026))
Platform(Vec3(63.9781, 21.0108, -313.399))
Platform(Vec3(106.336, 21.7041, -314.22))
Platform(Vec3(127.271, 22.0467, -314.626))
Platform(Vec3(140.357, 27.1054, -314.879))
Platform(Vec3(155.502, 31.5333, -315.172))
Platform(Vec3(183.088, 32.3551, -313.688))
Platform(Vec3(207.893, 32.8512, -313.688))
Platform(Vec3(272.206, 34.1376, -313.688))
Platform(Vec3(286.402, 40.7493, -313.687))
Platform(Vec3(279.467, 45.2291, -298.974))
Platform(Vec3(276.644, 47.8035, -247.383))
Platform(Vec3(275.481, 47.0466, -206.259))
Portal(Vec3(275.486, 52.046, -206.386))
Platform(Vec3(280.947, 52.4222, -273.657))
Platform(Vec3(-1.45974, 25.976, -178.793))
Platform(Vec3(-2.1425, 25.0246, -178.681))
Platform(Vec3(-1.51808, 25.5806, -140.103))
Platform(Vec3(-2.0098, 26.0397, -150))
Platform(Vec3(-2.38591, 26.2334, -191.67))
Platform(Vec3(91.2361, 32.216, -313.007))
Platform(Vec3(-9.097, 32.2579, -280.842))
Platform(Vec3(279.779, 52.2863, -288.757))
Platform(Vec3(277.064, 51.1692, -255.344))
Grapple(Vec3(274.925, 56.6227, -223.522))
Platform(Vec3(251.518, 40.172, -314.807))
Platform(Vec3(234.105, 33.5976, -314.413))
Platform(Vec3(225.337, 34.8861, -314.214))
Platform(Vec3(215.52, 33.2659, -316.504))


def update():
    if held_keys['i']:
        FPC_POS_text.text = f"{player.position}"
    else:
        FPC_POS_text.text = ' '

    if held_keys['escape']:
        if not quM.playing:
            quM.play()
        QUIT_WARN_text.text = 'Press "q" to quit'
    else:
        QUIT_WARN_text.text = ' '

    if held_keys['q']:
        quit()


PointLight(parent=camera, color=color.white, position=(0, 10, -1.5))
AmbientLight(color=color.rgba(100, 100, 100, 0.1))

app.run()
