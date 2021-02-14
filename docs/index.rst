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
- Active Buzzers
- PCF8591
- Potentiometers

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
-----------------

Wiring examples:

.. image:: schems/button_bb.jpg
  :width: 325
  :alt: breadboard
.. image:: schems/button_schem.jpg
  :width: 325
  :alt: schem

Class overview:

.. code-block:: python

    button = raspi_components.Button(pin)
    # This initiates the button class on the chosen pin.

    print(button.is_pressed())
    # Will return True if the button is pressed, otherwise will return False.

    raspi_components.ButtonTest.test(pin)
    # This is a test class, and will loop through, printing whether the button is
    # pressed or not every second.

The Led class:
--------------

Wiring examples:

.. image:: schems/led_bb.jpg
  :width: 325
  :alt: breadboard
.. image:: schems/led_schem.jpg
  :width: 325
  :alt: schem

Class overview:

.. code-block:: python

    led = raspi_components.Led(pin)
    # This initiates the LED on the chosen pin.

    led.on(100)
    # This turns the LED on and sets the brightness to 100%.
    # You can have any value between 0 and 100 here. If left
    # Blank the default value is 100.

    led.off()
    # This turns the LED off.

    led.dim(brightness)
    # This dims the LED. You can have any value from 0 to 100 here.

    raspi_components.LedTest.test(pin)
    # This is a test class, it will loop through turning the LED on and off,
    # and dimming it.

The RGBLed class:
-----------------

Wiring examples:

.. image:: schems/rgb_led_bb.jpg
  :width: 325
  :alt: breadboard
.. image:: schems/rgb_led_schem.jpg
  :width: 325
  :alt: schem

Class overview:

.. code-block:: python

    rgb_led = raspi_components.RGBLed(red_pin, green_pin, blue_pin)
    # This initiates the RGB LED, taking the input of the chosen pins for
    # red, green, and blue.

    rgb_led.on(red_val, green_val, blue_val)
    # This turns the RGB LED on. red_val, green_val, and blue_val are set to 0
    # by default, but this can be changed to change the color set when turned on.
    # These values can be between 0 and 100.

    rgb_led.set_color(red_val, green_val, blue_val)
    # This changes the color of the RGB LED. These values can be between 0 and 100.

    rgb_led.off()
    # This will turn the RGB LED off.

    raspi_components.RGBLedTest.test(red_pin, green_pin, blue_pin)
    # This is a test class, it will turn the RGB LED on and off, and randomly assign
    # it a color.

The Buzzer class:
-----------------

    Wiring examples:

    .. image:: schems/buzzer_bb.jpg
      :width: 300
      :alt: breadboard
    .. image:: schems/buzzer_schem.jpg
      :width: 325
      :alt: schem

    Class overview:

    .. code-block:: python

        buzzer = raspi_components.Buzzer(pin)
        # This initiates the buzzer class on the chosen pin.

        buzzer.on()
        # This will turn the buzzer on.

        buzzer.off()
        # This will turn the buzzer off.

        BuzzerTest.test(pin)
        # This is the test class for the buzzer. When initialized it will
        # turn the buzzer on for one second.


The ADC class:
-----------------

    Wiring examples:

    .. image:: schems/ADC_bb.jpg
        :width: 300
        :alt: breadboard
    .. image:: schems/ADC_schem.jpg
          :width: 325
          :alt: schem

    Class overview:

    .. code-block:: python

        adc = raspi_components.PCF()
        # This initiates the PCF class.

        adc.is_connected()
        # Checks to see if the adc is connected. Raises an error if it is not.

        adc.close()
        # Closes the adc connection.

        value = adc.read(channel)
        # Returns the value from a given channel.

        adc.write(channel, value)
        # Writes the specified value to the given channel.

The Potentiometer class:
-----------------

    Wiring examples:

    .. image:: schems/potentiometer_bb.jpg
        :width: 300
        :alt: breadboard
    .. image:: schems/potentiometer_schem.jpg
        :width: 325
        :alt: schem

    Class overview:

    .. code-block:: python

        potentiometer = raspi_components.Potentiometer(channel)
        # This initiates the Potentiometer class on the given channel.

        Value, Voltage = potentiometer.read_value()
        # Returns the value of the potentiometer as well as the voltage.

        potentiometer.close()
        # Closes the potentiometer.


Contribute
----------

- `Issue Tracker <https://github.com/Builder212/raspi_components/issues>`_
- `Source Code <https://github.com/Builder212/raspi_components/>`_
- `Documentation <https://raspi-components.readthedocs.io/en/latest/?#>`_
- `Package on PyPi <https://pypi.org/project/raspi-components/>`_

Support
-------

If you are having issues, or would like to request a feature,
please open an issue on the repository.

License
-------

This project is licensed under the MIT license.
