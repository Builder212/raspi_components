==============================================
Welcome to **raspi_components** documentation!
==============================================

This python library is designed to ease the process of working with
different components connected to the raspberry pi via its gpio.

Features
--------

This library can work with components such as:

- Buttons
- LEDs
- RGB LEDs

Installation
------------

To install raspi_components, run:

    pip install raspi_components

Working with the library
------------------------
To import the library, run:

.. code-block:: python

    import raspi_components

The Button class:

.. code-block:: python

    button = raspi_components.Button(pin)
    #This initiates the button class on the chosen pin.

    print(button.is_pressed())
    #Will return True if the button is pressed, otherwise will return False.

    raspi_components.ButtonTest.test(pin)
    #This is a test class, and will loop through, printing whether the button is
    #pressed or not every second.

The Led class:

.. code-block:: python

    led = raspi_components.Led(pin)
    #this initiates the LED on the chosen pin.

    led.on(100)
    #this turns the LED on and sets the brightness to 100%.
    #You can have any value between 0 and 100 here.

    led.off()
    #this turns the LED off.

    led.dim(brightness)
    #this dims the LED. You can have any value from 0 to 100 here.

    raspi_components.LedTest.test(pin)
    #This is a test class, it will loop through turning the LED on and off,
    #and dimming it.

The RGBLed class:

.. code-block:: python

    rgb_led = raspi_components.RGBLed(red_pin, green_pin, blue_pin)
    #This initiates the RGB LED, taking the input of the chosen pins for
    #red, green, and blue.

    rgb_led.on(red_val, green_val, blue_val)
    #This turns the RGB LED on. red_val, green_val, and blue_val are set to 0
    #by default, but this can be changed to change the color set when turned on.
    #These values can be between 0 and 100.

    rgb_led.set_color(red_val, green_val, blue_val)
    #This changes the color of the RGB LED. These values can be between 0 and 100.

    rgb_led.off()
    #This will turn the RGB LED off.

    raspi_components.RGBLedTest.test(red_pin, green_pin, blue_pin)
    #This is a test class, it will turn the RGB LED on and off, and randomly assign
    #it a color.


Contribute
----------

- `Issue Tracker <https://github.com/Builder212/raspi_components/issues>`_
- `Source Code <https://github.com/Builder212/raspi_components/>`_

Support
-------

If you are having issues, or would like to request a feature,
please open an issue on the repository.

License
-------

This project is licensed under the MIT license.
