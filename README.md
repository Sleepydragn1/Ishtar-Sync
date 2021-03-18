# Ishtar Sync

This is a project whipped up *very* quickly for a *very* specific purpose: to help me and my group of friends exploit [the 12-man raid glitch in Destiny 2.](https://www.polygon.com/2021/3/1/22307682/destiny-2-raid-12-player-glitch-nightfall-dungeon) It shined gloriously for a single day on the eve of [the patch that fixed this glitch,](https://www.bungie.net/en/Explore/Detail/News/50186) and now it is utterly useless.

Because this project was only used for a day, and will likely never be used again, consider it to be distributed **as is** with no future improvements or fixes planned.

## Why?

The timing for joining the host is difficult to get down consistently, and varies wildly depending on the networking conditions of the host and joiner, their fireteam, and even their respective fireteam size. While certain techniques can widen the "window" of the timing (in particular, having the host and joiner be geographically distant) my friend group and I (who all live fairly close) found it difficult to do. Thus, this program.

## How It Works

The program uses a host/client model where the host creates a server with a specified port and password, and the client connects using that port and authenticates using the password. The host is meant to be the host of the Destiny 2 lobby, who is starting the activity, while the client is the player who joins the host and has, in their fireteam, the remainder of the players. Both the host and client have a ready button, while the client also has the ability to set a delay in seconds, and a step amount in seconds as well. The ready button has a key binding, and there are additional key bindings for the client that allow them to increment or decrement the delay by the step amount. Once both the host and client are ready, the program on the host's machine clicks with the left mouse button, which starts the activity on that machine, and it sends a signal to the client. The client's program receives the signal, waits for time specified by the delay, and then presses enter, triggering them to join.

## Features
* Networking *(wow!)*
* Multithreading *(amazing!)*
* Password authentication *(outstanding!)*
* A user interface *(incredible!)*
* Key bindings so you don't have to alt-tab *(I can't believe it!)*

## Issues
* Really poor error handling
* No user feedback whatsoever
* Almost no input validation
* A blocking of user input until the host and client connect

## Tips
If, for some incredibly specific reason you want to use this program (perhaps in the future Bungie will screw up and accidentally re-implement the bug?) here's some tips:
* Running the Python version **(not the executable)** with the flag ```-l=INFO``` will give you *some* amount of insight into what the program is doing, and what the state of the network connection is.
* You can tell that the program is connected if when the "Ready" button is pressed, it greys out and is unable to be pressed again.
* Hosting will likely require port forwarding, and both hosting and joining may require you to turn off your firewall or create an exception for the program.
* **All input boxes need to be filled out.** The default text that's present is a hint text, and does not represent actual input for the program.
* Before both parties ready up, the host should be at the start screen for the activity with their mouse hovering over the "LAUNCH" button. The joiner should have pressed "Join Fireteam" on the host, and be at the screen that asks them if they want to bring their Fireteam with them.
* If you're building a standalone executable using PyInstaller (and perhaps other methods as well) the executable will require the platforms and styles folders from PySide6's site-packages to be present in the same directory as the executable. Also, PyInstaller doesn't play nice with the latest version of pynput, so v1.6.8 can be used in its place.

## Key Bindings

### Host
|Action|Key|
|--|--|
|Ready|Home|

### Joiner
|Action|Key|
|--|--|
|Ready|Home|
|Increment|Page Up|
|Decrement|Page Down|

## Dependencies

* [Python 3.9](https://www.python.org/downloads/release/python-390/)
* [Qt for Python (PySide6)](https://www.qt.io/qt-for-python) under [LGPL v3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html)
* [pynput 1.6.8](https://pynput.readthedocs.io/en/latest/) under [LGPL v3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html)

The Windows executable was built using [PyInstaller.](https://www.pyinstaller.org/)

## Why Even Post This Thing?

Why not?