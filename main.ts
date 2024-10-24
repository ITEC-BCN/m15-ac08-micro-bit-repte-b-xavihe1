input.onButtonPressed(Button.A, function () {
    music.play(music.stringPlayable("B A G A G F A C5 ", 120), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    music.ringTone(261.63)
    basic.pause(500)
    music.ringTone(329.63)
    basic.pause(500)
    music.ringTone(392)
    basic.pause(500)
    music.ringTone(523.25)
    basic.pause(500)
    music.ringTone(392)
    basic.pause(500)
    music.ringTone(329.63)
    basic.pause(500)
    music.ringTone(261.63)
    basic.pause(500)
    music.ringTone(523.25)
})
basic.forever(function () {
	
})
