def on_button_pressed_a():
    music.play(music.string_playable("B A G A G F A C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.ring_tone(261.63)
    basic.pause(500)
    music.ring_tone(329.63)
    basic.pause(500)
    music.ring_tone(392)
    basic.pause(500)
    music.ring_tone(523.25)
    basic.pause(500)
    music.ring_tone(392)
    basic.pause(500)
    music.ring_tone(329.63)
    basic.pause(500)
    music.ring_tone(261.63)
    basic.pause(500)
    music.ring_tone(523.25)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
