# rpi_camera
A python3 script file for Raspberry Pi video streaming

## 1. Purpose

	A python3 script running on Raspberry Pi to be a video streaming server

## 2. Prepare the camera
	Please reference 
	https://randomnerdtutorials.com/video-streaming-with-raspberry-pi-camera/
 
## 3. Start video streaming in 2592x1944 resolution

	git clone https://github.com/yourskc/rpi_camera.git
	cd rpi_camera
	python3 rpi_camera.py

## 4. Connect to camera

        in web browser, 
	http://{IP}:8080 
	for mainmoil, set the camera's URL : 
	http://{IP}:8000/stream.mjpg
	
	 
## 5. for Raspbian Lite

	login as default user/pass: pi/raspberry
	run raspi-config to enable camera
	sudo apt install git
	sudo apt install python3-picamera
	git clone https://github.com/yourskc/rpi_camera
	cd rpi_camera
	ifconfig ( check IP address)
	raspistill -v
	python3 rpi_camera
	 
## 6. run camera server on start up
	sudo nano /etc/rc.local

	add the followings,
	python3 /home/pi/rpi_camera/rpi_camera.py

## 7. connect two  Raspberry Pi through Ethernet
	for the first one,
	ifconfig eth0 192.168.1.1 netmask 255.255.255.0
	for the second one,
	ifconfig eth0 192.168.1.2 netmask 255.255.255.0

	connect the two Raspberry Pi with one Ethernet cable


	


 

