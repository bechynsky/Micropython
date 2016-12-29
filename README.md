# Micropython Tutorial for Wemos D1 Mini

All examples are for Wemos D1 Mini, [WS2812B RGB Shield (NeoPixel)] (https://www.wemos.cc/product/ws2812b-rgb-shield.html) and [DHT Pro Shield] (https://www.wemos.cc/product/dht-pro-shield.html).

# Lessons
## Computer setup

Connect to internet

Install [serial terminal] (http://www.putty.org/) for Windows

Install [ampy] (https://learn.adafruit.com/micropython-basics-load-files-and-run-code/overview)

Install drivers for CH340 (Mac, Windows < 8.1)

## First script

Interactive prompt using serial terminal

Blink LED on ESP8266 chip

Upload script using ESPlorer

File system

Startup scripts

## DHT22 (DHT11) and RGB LED

Using hardware drivers

How it works with pins

Read temperature and humidity

Control RGB LED

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

Create [ThingSpeak Account] (https://thingspeak.com/)

Create Channel

Send data from DHT11 to channel

## Server

How to use Access point mode

Create simple web server showing current temperature

Crete web server controlling RGB light

