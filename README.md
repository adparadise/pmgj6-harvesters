# Harvesters
A game made for Purple Monkey Game Jam IV.

Designed to run on a Raspberry Pi B+!

## Prerequisites

* Rasbpian
* Python 2.7 (which is the default)
* [kivy.org](http://kivy.org) I recommend following the [manual instructions](http://kivy.org/docs/installation/installation-rpi.html)

**NOTE** Kivy was patched to account for Raspbian's representing both ALT keys as the same. Patch forthcoming ;)

## Playing the game

The goal of the game is to score as many points as possible in 30 seconds. 2 players 
must coordinate to harvest blue squares and avoid harvesting red squares. To harvest,
both players must press the same buttons at the same time.

The Keyboard layout is taken from the MAME defaults:

Player 1:
 
 * arrow keys to move
 * ALT - button 1
 * CTRL - button 2
 
Player 2:

* RDFG to move (think WASD but over 2)
* A - button 1
* S - button 2

**NOTE** The game has no audio. It was made for a game jam after all ;)
