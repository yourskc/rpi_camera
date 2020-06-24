# Web streaming example
# Source code from the official PiCamera package
# http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming

import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server
import time
import RPi.GPIO as GPIO
import os

# Led pin, left 5:ground, 6 pin11
LedPin = 11
BtnPin = 12

PAGE="""\
<html>
<head>
<title>Raspberry Pi - Surveillance Camera</title>
</head>
<body>
<center><h1>Raspberry Pi - Surveillance Camera</h1></center>
<center><img src="stream.mjpg" width="640" height="480"></center>
</body>
</html>
"""
r_count = 0
count_filename = '/home/pi/camera/py/count.txt'

if( not os.path.exists(count_filename)):
    file1 = open(count_filename,"w")
    print (str(r_count))
    file1.write(str(r_count))
    file1.close()






def setup():
    GPIO.setmode(GPIO.BOARD)    
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.setup(BtnPin, GPIO.IN)
    
class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

setup()

print( count_filename)
if( os.path.exists(count_filename)):
    file1 = open(count_filename,"r")
    file1.seek(0)
    r_count = int(file1.readline())
    print(r_count)
    file1.close()
   
    file1 = open(count_filename,"w")
    file1.write(str(r_count+1))
    file1.close()
  
record_prefix = '/home/pi/camera/py/' + 'record/' + str(r_count)   
if (not os.path.exists (record_prefix)):
    os.mkdir(record_prefix)
    
   
    
  
with picamera.PiCamera(resolution='2592x1944', framerate=4) as camera:

    #camera.start_preview()
    print('Wait...')
    time.sleep(2)
    print('Start Recording...')
    state = 0
    for filename in camera.capture_continuous( record_prefix + '/img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        if state == 0 :
            GPIO.output(LedPin, GPIO.LOW)
            state = 1
        else :
            GPIO.output(LedPin, GPIO.HIGH)
            state = 0


        
