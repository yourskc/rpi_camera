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
	python3 rpi_camera

## 4. Connect to camera

	set the camera's URL in MAINMOIL
	http://{raspberry pi's IP}:8000/stream.mjpg
	click "Camera" button to start
	 
## 5. for Raspbian Lite

	run raspi-config to enable camera
	sudo apt install git
	sudo apt install python3-picamera
	git clone https://github.com/yourskc/rpi_camera
	cd rpi_camera
	ifconfig ( check IP address)
	raspistill -v
	python3 rpi_camera
	 


