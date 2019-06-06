import numpy as np
import matplotlib.pylab as plt
from matplotlib.colors import LogNorm
import os

def getLyrics(file):
	f = open(os.path.join('songs/',file),'r')
	lyrics = f.read()
	f.close()
	return lyrics

def processLyrics(lyrics, name):
	arr1 = lyrics.split()
	length = len(arr1)
	song = [[0 for x in range(length)] for y in range(length)] 

	for i in range(length):
		for j in range(length):
			if arr1[i] == arr1[j]:
				song[i][j] = 1
				song[j][i] = 1

	fig, ax0 = plt.subplots(1)

	c = ax0.pcolor(song)
	ax0.set_title(name)

	fig.tight_layout()
	plt.show()


def main():
	files = os.listdir('songs/')

	print('files found: %d' % len(files))

	for file in files:
		if os.path.isfile("songs/" + file):
			print('attr. lyrics')
			lyrics = getLyrics(file)
			processLyrics(lyrics, file)
		else:
			print('os.path.isfile returned False.')
			
if __name__ == '__main__':
    main()