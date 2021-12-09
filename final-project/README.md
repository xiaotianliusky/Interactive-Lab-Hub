# Welcome to the Creepy Game!

Final Project for Interactive Device Design, INFO5345/CS5424/ECE5413

by Jiejun Tian (tj587), Xiaotian Liu (xl467)

## Overview

At start, the game will begin with a normal mode (normal Snake Game). A certain phrase of easily recognized music (e.g. a scale of Do, Re, Mi, Fa, So) will tune in and repeat. When it comes to the end of the 3rd repeat, the mode will be switched to a Creepy Mode! In the creepy mode, the player should operate in a conversed way, that is, to press UP for going down, press LEFT for going right, etc.

## Prep

Parts we need:  

a) A Raspberry Pi for central control  
b) A joystick sensor to pivot the direction  
c) A webcam to play the music  
d) A LED display to show the game  
e) An OLED display for in-game timer (optional)  
f) A live music player and a musical instrument  

## Timeline

Project plan - November 22  
Prototype and design of the project - November 23  
Finish programming implementation - November 25  
Testing and optimization based on feedback from users - November 27  
Functional check-off - November 30  
Final Project Presentations - December 7  
Write-up and documentation due - December 13  

## Design

Paper Prototype and System Diagram

![image](https://github.com/xiaotianliusky/Interactive-Lab-Hub/blob/Fall2021/final-project/paper_proto.jpeg)
![image](https://github.com/xiaotianliusky/Interactive-Lab-Hub/blob/Fall2021/final-project/diag.png)

## Demo Video



## Ideation, Backup Plan and Reflection

Initially, we are going to build up an interactive game - Creepy Game. Inspired by the prototype of Flappy Bird, we would love to make the interactive control a little tricky. In the game, a random BGM will come along with the flying bird. When there is Major-tonality music going (sounds cheerful), the player should control the bird by the joystick in a normal mode. When another piece of Minor-tonality music tunes in (that sounds creepy and gloomy), the direction-mapping between the joystick and the bird will converse. In this ‘creepy’ mode, the user should press up for the bird to go down, and press down for going up. Those two modes will randomly come up in the game, and the player should response and adjust accordingly.

There are several issues concerning the initial ideation:
1. The bird game relies heavily on the player’s speed of response. Thus, there will be a relatively high demand for the time sensitivity of the system. If we want to switch the control mode, or set up several levels of speed for the bird in a prompt (to make the game gradually exciting), it will be challenging for us to ensure the robustness of this system.
2. In the Flappy Bird game, there is a default speed of 'falling down'. 'Click to go up' is the only choice of interaction for a player. Thus, there is no counterpart in the creepy mode (you don't hit another button to let the bird go down, left, or right).
3. It may require some knowledge of music for the players to identify the piece of BGM as Major-tonality or Minor-tonality.

Thus, we decided to implement the Creepy Snake - four directions are all included! Also, we decide to change the way of triggering a Creepy Mode, in order to make the game more universal. We would also expect to add more fun for the game in the future (e.g. facilitate two players and make them compete in the board simoutaniously).

Have Fun:)

