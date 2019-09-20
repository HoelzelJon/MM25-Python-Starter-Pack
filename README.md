# MechMania25 Python Starter Pack

Here's all the code you need to get started with making a bot for MechMania in Python. Just do these steps:

* Pre-Setup -- install Java, Node, and the `mm` command line tools
* Setup -- Clone this repository and start running your bot!

# Pre-Setup
1. First, install Java. To do this, see [this guide](https://docs.oracle.com/en/java/javase/13/install/overview-jdk-installation.html#GUID-8677A77F-231A-40F7-98B9-1FD0B48C346A) for help.
    * Advice for Windows users:
        * Make sure to set the `JAVA_HOME` variable as a SYSTEM environment variable, rather than a user environment variable.
        * Make sure to NOT have `bin` at the end of your `JAVA_HOME` environment variable.
    * Check that the `JAVA_HOME` environment variable is set correctly.
        * For Windows, you can run `echo %JAVA_HOME%`. You should see a result similar to `C:\Program Files\Java\jdk1.8.0_171`. Note that this does NOT end with `\bin`.
        * For Mac users, you can run `echo $JAVA_HOME`. You should see a result similar to `/Library/Java/JavaVirtualMachines/jdk1.8.0_45.jdk/Contents/Home`.

2. Install Node. To do this, go [here](https://nodejs.org/en/download/) and download the appropriate installer for your operating system.
    * Run the installer with all the defaults.

3. Run `npm install -g mechmania`.  This gets the `mm` command line tools, which are used to run the game, test and submit bots for the tournament.

4. Run `mm download` to download required files.

5. Now install Python 3. To do this, see [this guide](https://realpython.com/installing-python/) for help.

5. For the python starter pack, you will have to set up pip
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

# Game API Information
You will be writing your code inside of the `Strategy.py` file. Note, that the `Strategy` class inherits the `Game` class from `API.py`, so all the instance methods for a `Game` object are available to you. You can find documentation for these methods in [API.py](https://github.com/HoelzelJon/MM25-Python-Starter-Pack/blob/master/API.py).
