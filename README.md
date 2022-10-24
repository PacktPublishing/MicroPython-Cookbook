# MicroPython Cookbook

<a href="https://www.packtpub.com/in/application-development/micropython-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781838649951 "><img src="https://www.packtpub.com/media/catalog/product/cache/e4d64343b1bc593f1c5348fe05efa4a6/1/2/1234_b13911.png" alt="MicroPython Cookbook" height="256px" align="right"></a>

This is the code repository for [MicroPython Cookbook](https://www.packtpub.com/in/application-development/micropython-cookbook?utm_source=github&utm_medium=repository&utm_campaign=), published by Packt.

**Build practical solutions to control LEDs, make music and read sensor data using popular microcontrollers such as Adafruit Circuit Playground, ESP8266, and the BBC Micro Bit**

## What is this book about?
MicroPython is an open source implementation of Python 3 that runs in embedded environments. With MicroPython, you can write clean and simple Python code to control hardware instead of using complex low-level languages such as C and C++. This book guides you through all the major applications of the MicroPython platform to build and program projects that use microcontrollers.

This book covers the following exciting features:
* Execute code without any need for compiling or uploading using REPL (read-evaluate-print-loop)
* Program and control LED matrix and NeoPixel drivers to display patterns and colors
* Build projects that make use of light, temperature, and touch sensors
* Configure devices to create Wi-Fi access points and use network modules to scan and connect to existing networks
* Use Pulse Width Modulation to control DC motors and servos
* Build an IoT device to display live weather data from the internet at the touch of a button

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1838649956) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter01.

The code will look like the following:
```
from adafruit_circuitplayground.express import cpx
import time

cpx.pixels[0] = (255, 0, 0) # set first NeoPixel to the color red
time.sleep(60)
```

**Following is what you need for this book:**
This book aims to help people apply the power and ease of use of the Python language to the versatility of microcontrollers. Prior knowledge of Python is expected in order to understand this book.

With the following software and hardware list you can run all code files present in the book (All chapters).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| All | Mu Text Editor 1.x | Windows, Linux, or macOS |
| All | Screen terminal emulator | Windows, Linux, or macOS |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://www.packtpub.com/sites/default/files/downloads/9781838649951_ColorImages.pdf).

### Related products
* Artificial Intelligence for Robotics [[Packt]](https://www.packtpub.com/in/hardware-and-creative/artificial-intelligence-robotics?utm_source=github&utm_medium=repository&utm_campaign=) [[Amazon]](https://www.amazon.com/dp/1788835441)

* Learn Robotics Programming [[Packt]](https://www.packtpub.com/hardware-and-creative/learn-robotics-programming?utm_source=github&utm_medium=repository&utm_campaign=) [[Amazon]](https://www.amazon.com/dp/1789340748)

## Get to Know the Author
**Marwan Alsabbagh**
has been coding in some form or other since before the web existed and has continued to develop software, with a particular passion for Python, his preferred programming language, for over a decade. He has been a speaker at a number of global Python conferences, where he has been known to present microcontroller projects with a healthy dose of humor and stage theatrics. The snow globe intruder alert system, which he created with his creative and curious daughters, was one of his favorite MicroPython projects. His research interests include software engineering, microcontrollers, and 3D printing.

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSdy7dATC6QmEL81FIUuymZ0Wy9vH1jHkvpY57OiMeKGqib_Ow/viewform) if you have any feedback or suggestions.
### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781838649951">https://packt.link/free-ebook/9781838649951 </a> </p>