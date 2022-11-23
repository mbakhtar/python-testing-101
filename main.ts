input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Umbrella)
    pump.startDuration(Pump.LEFT, 60, 4)
    basic.clearScreen()
})
