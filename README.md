## Pi Pico Based StepMania Sync Tester

*This is based off [TomoDesigns' "Super Easy Pico Keyboard"](https://www.instructables.com/The-Basic-Pico-Keyboard/)*

Everything you need to test the input sync stability of your StepMania (or other rhythm game engine) setup is provided here.

All you need is a Raspberry Pi Pico and a microUSB cable which does data. Use GitHub's "download as ZIP" feature to get everything you need easily.

The Pi Pico settles in at just about 625 BPM when you have it loop every 90ms and simulate a keypress. This is configured to send P2 Up, which is usually set by default to "8" on the number pad. A silent ogg file and .sm file containing 12 minutes of up arrow 16th notes at 156.25BPM is included.

The normal version `Main.py` can be controlled completely from your computer. The alternate version `Main-switched.py` assumes you connected a switch between **3V3** and **GP10** on your Pi Pico.


### Prerequisites
You will need something to run the software on the Pico. [Thonny](https://github.com/thonny/thonny) is a good option. The version provided here is tested and works, or it can be downloaded from Thonny's GitHub here: https://github.com/thonny/thonny/releases/download/v3.3.13/thonny-3.3.13.exe

### How to set up
1. Plug in the Pi Pico while holding down the BOOTSEL button. It should appear as a USB drive. Drag `adafruit-circuitpython-raspberry_pi_pico-nl-7.3.0.uf2` onto the Pico's storage. It will disconnect, reboot, and reconnect.
2. Copy the folder `adafruit_hid` to the Pico's storage.
3. Open **Thonny**. When it asks you if you want to use Normal or Raspberry Pi mode, stay on Normal mode. You may have to hit the "Stop" button (Stop/restart backend) to get your Pi Pico to be recognized.
4. Load `Main.py` in Thonny. When you are ready to send the input, press the start button (or toggle the switch if you loaded `Main-switched.py`)
5. Make a folder in your StepMania's `Songs` directory called anything you'd like to call it, and then put the folder "625bpm sync test" in there. It will show up in your song list as "625bpm sync test".