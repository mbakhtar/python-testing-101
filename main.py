def on_button_pressed_a():
    basic.show_icon(IconNames.UMBRELLA)
    pump.start_duration(Pump.LEFT, 60, 4)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)