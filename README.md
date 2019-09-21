# MechMania25 Python Starter Pack

Here's all the code you need to get started with making a bot for MechMania in Python. Just do these steps:

* Pre-Setup -- install Java, Node, and the `mm` command line tools
* Setup -- Clone this repository and start running your bot!

# Pre-Setup
1. Follow the Pre-setup instructions on the wiki [here](https://github.com/HoelzelJon/MechMania-25-Wiki/wiki#pre-setup)

2. Now install Python 3. To do this, see [this guide](https://realpython.com/installing-python/) for help.

3. For the python starter pack, you will have to set up pip
    * To set up pip, you can follow [this guide](https://www.makeuseof.com/tag/install-pip-for-python/) .
    * You will also need [Flask](https://pypi.org/project/Flask/), which you can get via the command line by running `pip install flask` (or `pip3 install flask` if you have pip3)
    * If you get a `no module named [insert module name here]` error while running your scripts, you can run `pip install [insert module name here]`

# Setup

1. Clone this repo (or fork it or download it somewhere as a ZIP)
2. Modify the script at `Strategy.py`.
    * Write your code in the `do_turn` method and `get_setup` method.
    * You may also add other files or dependencies. If you have any questions about this, we're here to help!

4. Run `mm play .`
    * This will build the bot in the given directory (`.`) and then starts a game in which your bot fights against itself.
5. To run two different bots against each other, run `mm play bot1_directory bot2_directory`.
6. To submit your bot, run `mm push .`

Use `mm help` for more help or `mm play` for information about the different options/flags you can use while running a game!

# What's this `ImportError: No module named queue`?

If you're getting this error, you most likely have python 2 running instead of python 3. To fix this, change `python` to `python3` in the `mm.json` file.

# Game API Information
You will be writing your code inside of the `Strategy.py` file. Note, that the `Strategy` class inherits the `Game` class from `API.py`, so all the instance methods for a `Game` object are available to you. You can find documentation for these methods in [API.py](https://github.com/HoelzelJon/MM25-Python-Starter-Pack/blob/master/API.py).

Most of the game state data is stored in the `.game` field of a Game object, which is a dictionary. This dictionary contains fields like `["turnsTaken"]`, the turn index, and `["units"]` an 
