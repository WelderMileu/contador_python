from time import sleep
import sys

progress = []

def contador(num):
	for i in range(1, int(num)):
		
		progress.append('#')
		progress_lenght = ''.join(progress)
		
		if i < 10:
			print("0{}% {}".format(i, progress_lenght), end="\r")
		else:
			print("{}% {}".format(i, progress_lenght), end="\r")
		sleep(1)

contador(sys.argv[1])