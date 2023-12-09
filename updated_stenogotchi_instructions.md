Install steps

0. Flash and configure the DietPi image as in step 1 of the stenogotchi install instructions

1. Install dependencies  
- ``apt-get install git xorg xserver-xorg-video-fbdev python3-pip python3-rpi.gpio python3-gi libtiff6 libopenjp2-7 bluez screen rfkill libdbus-1-dev libdbus-glib-1-dev build-essential python3-dev libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev python3-dbus -y``
- ``pip3 install file_read_backwards flask flask-wtf flask-cors evdev python-xlib pillow spidev jsonpickle dbus-python toml --break-system-packages``

2. Install plover (current continous release)
- ``wget https://github.com/openstenoproject/plover/releases/download/continuous/plover-4.0.0rc2+6.g53c416f-py3-none-any.whl``
- ``pip3 install plover-4.0.0rc2+6.g53c416f-py3-none-any.whl --break-system-packages``

3. Install the stenogotchi link
- ``git clone https://github.com/Anodynous/stenogotchi.git``
- ``cd stenogotchi/``
- ``git fetch --all``
- ``git reset --hard origin/dev``
- ``git checkout dev``
- ``cd ..``
- ``pip3 install ./stenogotchi/plover_plugin/ --break-system-packages``

4. Follow the [stenogotchi installation instructions from step 5](https://github.com/Anodynous/stenogotchi/blob/54da07d0d681f25f3c2f8d04e9423c1bbc31da8b/README.md#L52) - configure plover, run the stenogotchi installation script, and configure stenogotchi settings

Optional:
- install other plugins with pip e.g.
- ``pip3 install plover-python-dictionary --break-system-packages``

- add dictionaries
	- e.g. clone repo with dictionaries git clone url my_dicts
	- add dictionaries to plover by changing the plover.config file

To update plover download the python wheel of the new version and install with pip, this will automaticalle remove the old version before installing
