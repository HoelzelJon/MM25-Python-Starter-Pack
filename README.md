# MechMania25 Python Starter Pack

Here's all the code you need to get started with making a bot for MechMania in Python. Just do these steps:

* Pre-Setup -- install Node and the `mm` command line tools
* Setup -- Clone this repository and start running your bot!

# Pre-Setup

1. First, install Python. To do this, see [this guide](https://realpython.com/installing-python/) for help.

2. Install Node. To do this, go [here](https://nodejs.org/en/download/) and download the appropriate installer for your operating system.
    * Run the installer with all the defaults.

3. Run `npm install -g mechmania`.  This gets the `mm` command line tools, which are used to run the game, test and submit bots for the tournament.

4. Run `mm download` to download required files.

5. For the python starter pack, you will have to set up pip
    * To set up pip, you can follow [this guide](https://pip.pypa.io/en/stable/installing/) .
    * You will also need [Flask](https://pypi.org/project/Flask/), which you can get via the command line by running `pip install Flask` (or `pip3 install Flask` if you have pip3)

# Setup

1. Clone this repo (or fork it or download it somewhere as a ZIP)
2. Modify the script at `Strategy.py`.
    * Write your code in the `do_turn` method and `get_setup` method.
    * You may also add other files or dependencies. If you have any questions about this, we're here to help!

4. Run `mm play .`
    * This will build the bot in the given directory (`.`) and then starts a game in which your bot fights against itself.
5. To run two different bots against each other, run `mm play bot1_directory bot2_directory`.
6. To submit your bot, run `mm push .`

Use `mm help` for more information!

# Game API Information
You will be writing your code inside of the `Strategy.py` file. Note, that the `Strategy` class inherits the `Game` class from `API.py`, so all the instance methods for a `Game` object are available to you. You can find documentation for these methods in [API.py](https://github.com/HoelzelJon/MM25-Python-Starter-Pack/blob/master/API.py).
