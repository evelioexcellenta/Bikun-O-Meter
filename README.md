# Bikun-O-Meter

## Overview
Our project aims to develop a web-based, battery-powered system for monitoring and analyzing crowd density at bus stops. Using ESP32CAM to capture images, the data is sent to a server to measure parameters such as headcount and stop area density. This system used a TensorFlow lite library and Real-time results are displayed on the website. 


## Concept
This system is divided into three parts: Electrical and Mechanical hardware, Image Recognition processing, and a Website. The microprocessor used is an ESP-32CAM, which connects to a WiFi Modem capable of transmitting captured pictures to Firebase Storage. The pictures are then downloaded by a Raspberry Pi 3B server and processed using an Image Recognition Algorithm from the TensorFlow Lite library to identify the number of people and buses at the bus stop. The processed data is then uploaded to a website in real-time via the Firebase Realtime Database. For the power source, this system used a 5V battery module consisting of 2 18650 batteries connected in series and the voltage supply passes through a step-down buck converter.

The system provides a user-friendly web interface for accessing real-time data and includes a feature for storing historical data to observe crowd trends over time. With innovative technology and battery energy, this adaptable system can be installed at various bus stop locations without relying on external power sources.

## Battery Calculation
This system is aimed to operate without being connected to external power sources for at least a week. Therefore, we can estimate the required power. The system is set to turn on for 10 seconds and then go into DeepSleep mode for 50 seconds. So, it will be on for approximately 1.833 hours per day. If we want it to run for 7 days, it will be on for a total of 12.833 hours. Assuming an ESP32-CAM consumes 260mA of power, the battery capacity needed to power the system for 7 days is 3336.667 mAh. We use two Sony VCT6 batteries with a capacity of 3500mAh each, connected in series. We chose batteries with a capacity of 3500mAh to provide backup power so that the system could last for a week without shutting down immediately. Additionally, the batteries are connected in series to obtain a voltage of 7.4V - 8.4V, which will then be reduced to 5V using a buck converter module to be connected to the ESP32CAM.

## Result
Based on the assembly and testing stages, the results show that the tool is capable of sending information about the situation and crowd levels at the Faculty Bus Stop. The graph indicates that the crowd situation at the stop increases at certain times, namely during class schedules. Additionally, a decrease in the graph indicates that the  bus is present to transport passengers.
<img width="275" alt="download 1" src="https://github.com/evelioexcellenta/Bikun-O-Meter/assets/70692957/c980207b-189a-4aa0-8746-e6d1dde00798">




 ## Visit our website at: 
 https://bikun-o-meter.netlify.app/
 or scan the QR code:

![Screenshot 2024-01-26 at 18 11 22](https://github.com/evelioexcellenta/Bikun-O-Meter/assets/106600068/fc5a05f8-fc74-4853-800e-14b35886ce95)
