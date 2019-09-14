# Instructions

1. run the server for the first strategy with: `python Server.py <Strategy> <port number>`
2. run the server for the second strategy with: `python Server.py <Strategy 2> <different port number>`
3. run game engine using command line arguments including the two port numbers

1. edit rum-game.sh
  a. replace GAMEID with a integer game id
  b. replace playerOne & playerTwo with appropriate names
  c. make sure port number on line 1 & 2 matches the port number on line 3
2. run ./run-game.sh

Installation
- "ImportError: No module named flask"
  pip3 install flask

Checking
- run ps
➜  MM25-Python-Starter-Pack git:(master) ✗ ps
  PID TTY          TIME CMD
    5 pts/0    00:00:03 zsh
 1727 pts/0    00:00:00 python3
 1728 pts/0    00:00:00 python3
 1768 pts/0    00:00:00 python3
 1769 pts/0    00:00:00 python3
 1783 pts/0    00:00:00 ps
➜  MM25-Python-Starter-Pack git:(master) ✗ kill 1727 1728 1768 1769
