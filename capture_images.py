from picamera import PiCamera
from picamera.array import PiRGBArray
import time


def image_capture():
	camera = PiCamera()

	camera.start_preview()
	for i in range(5):
		camera.capture('image_%s.jpg' % i)
		time.sleep(1)
	camera.stop_preview()

def video_capture():
	camera = PiCamera()
	camera.resolution = (640, 480)
	camera.framerate = 32
	rawCapture = PiRGBArray(camera, size=(640, 480))
	 
	# allow the camera to warmup
	time.sleep(0.1)

	counter = 0
	# capture frames from the camera
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		# grab the raw NumPy array representing the image, then initialize the timestamp
		# and occupied/unoccupied text
		image = frame.array
		print(image)

		# clear the stream in preparation for the next frame
		rawCapture.truncate(0)
		if counter == 10:
			break
		counter += 1


if __name__ == '__main__':
	video_capture()

