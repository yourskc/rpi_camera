# rpi_camera

    A python3 script file for Raspberry Pi video streaming

## 1. Purpose

	A python3 script running on Raspberry Pi to be a video streaming server, 
	automatically recording or controled with button and led.

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
	( sleep 10
	python3 /home/pi/rpi_camera/rpi_camera.py ) &

## 7. connect two Raspberry Pi through Ethernet

	for the first one,
	ifconfig eth0 192.168.1.1 netmask 255.255.255.0
	for the second one,
	ifconfig eth0 192.168.1.2 netmask 255.255.255.0

	connect the above two Raspberry Pi with one Ethernet cable

## 8. automatically start recording

	replace rpi_camera.py with rpi_camera_auto.py, that is, 
	cp rpi_camera_auto.py rpi_camera.py

	When you want to change it next time,
	ps -ef | grep rpi ( check the {process ID} )
	sudo kill {process ID}

## 9. control with button and led

	replace rpi_camera.py with rpi_camera_btn.py, that is, 
	cp rpi_camera_btn.py rpi_camera.py	

	sudo apt-get install rpi.gpio
	
	connect 2 pins of led to Ground and PIN#11
	connect 3 pins of button to  3.3V, Ground and PIN#12










	















 

