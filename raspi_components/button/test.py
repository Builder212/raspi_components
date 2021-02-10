if __name__ == "__main__":
    from button import button as button

    pin = input("What pin is your button going to be operated from? ")
    print("\n")
    button = button(pin)

    try:
        while True:
            pressed = button.is_pressed()
            print(pressed)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
