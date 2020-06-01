# Wifi-Positioning-System
Hello Guys,
This is Yuvnish Malhotra. I am a student of IIT Indore. 
We currently are working on a project where we have to make an automatic robot to be deployed in covid-19 ward in a hospital that can give medicines to patients and do almost all sort of works a doctor has to do, to minimize the contact between doctors and infected people.
As this robot is going to be autonomous so it needs the target location and its current location and it has to work inside a room in a hospital, so using GPS for location won't work as we need highly precise locations.
So instead of GPS we are using Wifi-Positioning System for getting the location.
Location can be calculated through signal strength recieved by the robot from different access points or wifi hotspots by RSSI Fingerprint Method.
"Wifi-positioning system.pdf" is the research paper "RSSI based Algorithm for Indoor Localisation" by "Xiuyan Zhu and Yuan Feng" on which I have developed my code.
"access_points.py" is the main code for calculating distance from different access points and coordinates of unknown point based on its distance from different access points.
Here I am using 3 access points so I have written the code accordingly.
"parameters.py" is the code for calculating 2 parameters namely Reference Signal Strength and Signal Attenuation Factor which depend on the environment and are used in access_points.py file.


