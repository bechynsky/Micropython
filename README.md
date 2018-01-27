# Micropython Tutorial for Wemos D1 Mini

All examples are for Wemos D1 Mini, [WS2812B RGB Shield (NeoPixel)](https://www.wemos.cc/product/ws2812b-rgb-shield.html) and [DHT Pro Shield](https://www.wemos.cc/product/dht-pro-shield.html).

# Student prerequisities

* Python knowledge
* Micro USB cable
* Python 3 installed
  * If you have Python 2 installed you can get into problems mixing Python versions. You must use Python 3. Check what is default version of Python on your system.
* Python IDE installed
  * https://code.visualstudio.com/
* Git client (optional)

# Lessons

## Computer setup

* Connect to internet
* Install serial terminal 
  * Windows: [Putty](http://www.putty.org/)
  * Linux, Mac: Use _screen_ tool 
* Install [ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/overview), [install instruction](https://github.com/adafruit/ampy)
  * Add _ampy_ to PATH
* Install drivers for CH340 (Mac, Windows < 8.1)
* Add user to _dioultout_ group on Linux

## Firmware update

First you need to upload Micropython to ESP8266 chip.

[Firmware for ESP8266](http://micropython.org/download#esp8266)

Windows: [NodeMCU Flasher](https://github.com/nodemcu/nodemcu-flasher)

### esptool.py

[Documentation and source code](https://github.com/espressif/esptool)

#### Instalation

```
pip install esptool
```

#### Example how to use it

It is important to erase flash first.

_Windows_

```
esptool.py.exe --port COM7 erase_flash

esptool.py.exe --port COM7 write_flash -fm dio 0x000000 esp8266-20170823-v1.9.2.bin
```

## First script

### Interactive prompt using serial terminal

Connect device using USB cable to your computer. Device will present as serial port. On Windows it will be _COMx_. On Linux and Mac it will be _/dev/ttyUSBx_. _x_ is number.

Open your serial communication appliction and connect to right serial port using baudrate (speed) _115200_. After you connect you will probably need to press enter to see promt _>>>_. No it works es Python interactive console on standard computer.

Control LED on ESP8266 chip. LED is connected on pin 2 to VCC. You control ground (0 - on, 1 - off). LED is located close antena.

```
import machine
pin = machine.Pin(2, machine.Pin.OUT)
pin.value(0)
pin.value(1)
```

#### Upload script using _ampy_

Scrip name: [101.py](101.py)

Close interactive prompt.

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

Connect to local Wi-Fi [wifi_connect.py](wifi_connect.py)

Download website [http_test.py](http_test.py) _Connect to Wi-Fi first!_

## ThingSpeak

Create [ThingSpeak Account](https://thingspeak.com/)

Create Channel

Send data from DHT11 to channel

## Server

### How to use Access point mode

Run this code to find _mac address_ of your board.

```
import network

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
print(":".join(map(lambda x: "%02x" % x, wlan.config('mac'))))
```

Open list of available Wi-Fi and connect to Wi-Fi named _MicroPython-xxxxxx_ where _xxxxxx_ is part of MAC address. Password is _micropythoN_. IP addres of board is _192.168.4.1_.

### Create webserver

__Important:__ There is bug in _ampy_ tool. It is recommended to upload code as _main.py_ using _put_ command instaed of to try run it using _run_ command. Do not forget restart ESP8266.

Create web server showing current temperature [weather_station.py](weather_station.py).

Crete web server controlling on board LED [server_led_control.py](server_led_control.py).
