
# The KSPEC GFA Camera Controller
- The Controller communicate with Basler Guide cameras for guiding and focusing processes.
- The Controller use the [pypylon](https://github.com/basler/pypylon) library as the middleware for the communication.

# Getting Started

If you test this controller, you should acces the KSPEC PC connected with GFA Cameras.
Refer to KSPEC_PC_Access_Manual.txt

 * Install [pylon](https://www.baslerweb.com/pylon)
   This is strongly recommended but not mandatory. See [known issues](#known-issues) for further details.
 * Install pypylon: ```pip3 install pypylon```
   For more installation options and the supported systems please read the [Installation](#Installation) paragraph.
 * Clone this repository. ```git clone https://mmingyeong@bitbucket.org/mmmingyeong/gfa_controller.git```
 * Look at test.py or use the following snippet:

```python
import controller

gfa_init = controller.gfa_init()
gfa_init.gfa_init_connect_camera()
gfa_init.gfa_init_exposure(1000) # put the exposure time you want to grab
```