# Micropython Tutorial for Wemos D1 Mini

All examples are for Wemos D1 Mini, [WS2812B RGB Shield (NeoPixel)](https://www.wemos.cc/product/ws2812b-rgb-shield.html) and [DHT Pro Shield](https://www.wemos.cc/product/dht-pro-shield.html).

# Student prerequisities

* Python knowledge
* Micro USB cable
* Python 3 installed
* Python IDE installed
  * https://code.visualstudio.com/
* Git client (optional)

# Lessons

## Computer setup

* Connect to internet
* Install serial terminal 
  * Windows: [Putty](http://www.putty.org/)
* Install [ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/overview)
  * Add _ampy_ to PARH
* Install drivers for CH340 (Mac, Windows < 8.1)

## First script

### Interactive prompt using serial terminal

Baudrate: 115200

Control LED on ESP8266 chip. LED is connected on pin 2 to VCC. You control ground (0 - on, 1 - off).

```
import machine
pin = machine.Pin(2, machine.Pin.OUT)
pin.value(0);
pin.value(1);
```

#### Upload script using _ampy_

Scrip name: [101.py](101.py)

Close interactive prompt

Example for Windows. Use your serial port number.

```
ampy --port COM14 run 101.py
```

Example for Linux and Mac. Do not forget to use full path to your serial port.

```
ampy --port /dev/ttyUSB0 run 101.py
```

### File system

[Documentation ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/file-operations)

Startup scripts
* boot.py
* main.py - runs automatically after start

```
ampy --port COM4 put main.py
```

```
ampy --port /dev/ttyUSB0 put main.py
```

## DHT22 (DHT11) and RGB LED

Using hardware drivers

How it works with pins

Read temperature and humidity [dht.py](dht.py)

What is it Neopixel LED and how it works

Control Neopixel RGB LED [neopixel.py](neopixel.py)

Create simple thermometer using RGB LED and DHT11 - temperature is showed using colors (for example red hot, blue cold)

## HTTP protocol

How it works

GET vs POST

HTTP Headers

SSL

## Internet

Explain Wi-Fi modes - access point vs. client

Connect to local Wi-Fi

Download website

## ThingSpeak

Create [ThingSpeak Account](https://thingspeak.com/)

Create Channel

Send data from DHT11 to channel

## Server

How to use Access point mode

Create simple web server showing current temperature

Crete web server controlling RGB light

