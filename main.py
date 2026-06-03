def on_button_pressed_a():
    bitbot.led_rainbow(True, BBArms.BOTH)
    music.play(music.string_playable("E A B A G D A F ", 401),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    bitbot.goms(BBDirection.FORWARD, 100, 400)
    basic.pause(500)
    bitbot.rotatems(BBRobotDirection.LEFT, 60, 400)
    basic.pause(500)
    bitbot.goms(BBDirection.REVERSE, 100, 400)
    bitbot.rotatems(BBRobotDirection.LEFT, 120, 5000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.pause(500)
    bitbot.led_rotate(True, BBArms.BOTH)
basic.forever(on_forever)
