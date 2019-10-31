
# Enhanced Drone Autopilot Project

## Introdution 
This project will help you to control your drone manually by using the keyboard of your laptop, 
you will be able to take off, fly in the all directions, make rotations, start/stop the camera and land the drone. 
The software will save the all movements that you do on the drone in a separate file called autoPilot so you can run it again
and the drone will repeating the exact flight movements includeing start/stop camera.

## How to use this project

1- system requirements, Ubuntu 18.04, only Linux 64 bits.   

2- follow the install intructions on https://developer.parrot.com/docs/olympe/installation.html   

3- Install Parrot-Sphinx   

- requirements for Parrot-Sphinx on https://developer.parrot.com/docs/sphinx/system-requirements.html   
- Installation procedure on https://developer.parrot.com/docs/sphinx/installation.html   
- Installation procedure   

  ### Add new apt repository to your system   

  ### Setup your computer to accept packages from Parrot’s public server.   
  
  $ echo "deb http://plf.parrot.com/sphinx/binary `lsb_release -cs`/" | sudo tee /etc/apt/sources.list.d/sphinx.list > /dev/null    
  
  $ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 508B1AE5   
  
  ### Install the packages   
  
  $ sudo apt-get update   
  
  $ sudo apt-get install parrot-sphinx   
  
  
- First step on https://developer.parrot.com/docs/sphinx/firststep.html
- How to connect to the simulated drone https://developer.parrot.com/docs/sphinx/connectdrone.html

After you have installed the all requirements on your laptop you need just to run the moveby.py file in your terminal and your are ready 
to control your drone.   

T == Take off   

L == land   

W == press ones and the drone will move one meter to the front twics for two meters and so on.        

S == press ones and the drone will move one meter back twics for two meters and so on.       

D == press ones and the drone will move one meter to the right twics for two meters and so on.   

A == press ones and the drone will move one meter to the left twics for two meters and so on.     

U == press ones and the drone will move one meter up twics for two meters and so on.    

N == press ones and the drone will move one meter down twics for two meters and so on.    

Q == make rotation to the left    

E == make rotation to the right   

C == start recoding from the camera    

V == stop recording from the camera   

when you finish with all movements and you stop running this file in your terminal, you will find the autoPilot.py in you home diroctroy and all you need to do is to run this file in the terminal and the drone will repeat all movements automatically. 
