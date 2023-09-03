# Audio Toggler

Toggles the default audio output from speakers to headphones and vice versa. Different outputs are customizable inside the python file
> Note: This script is only tested on Windows 11. It also downloads the [NirCmd](https://www.nirsoft.net/utils/nircmd.html) utility to switch audio devices.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Creating a shortcut

1. Download the MinGW compiler from [here](https://github.com/brechtsanders/winlibs_mingw/releases/download/13.2.0mcf-16.0.6-11.0.1-ucrt-r2/winlibs-i686-mcf-dwarf-gcc-13.2.0-llvm-16.0.6-mingw-w64ucrt-11.0.1-r2.zip)
2. Extract the zip file to C:\MinGW
3. Add C:\MinGW\bin to your PATH environment variable
4. Run `g++ run.cpp -o toggle-audio.exe "-Wl,-subsystem,windows"`
5. Create a shortcut to the executable and place it on your desktop

> This project was created for personal use. Feel free to use it however you want.
