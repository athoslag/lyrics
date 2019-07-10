import numpy as np
import matplotlib.pylab as plt
from matplotlib.colors import LogNorm
import os

length = 0
words = []
colorspace = 'BuPu' # colorspace reference: https://matplotlib.org/users/colormaps.html

def colorIntensity(word):
	if len(word) < 3:
		return 1

	if word not in words:
		words.append(word)
	return (words.index(word)/len(words)) * 0.5

def getLyrics(file):
	if file[0] is '.':
		print('\t [graph.py] Ignoring file %s' % file)
		return

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
				song[i][j] = colorIntensity(arr1[i])
				song[j][i] = colorIntensity(arr1[i])

	fig, ax0 = plt.subplots(1)
	plt.set_cmap(colorspace)

	c = ax0.pcolor(song)
	ax0.set_title(name)
	fig.tight_layout()

def main():
	files = os.listdir('songs/')

	print('\t files found: %d' % len(files))

	for file in sorted(files):
		if os.path.isfile("songs/" + file):
			print('\t Processing %s...' % file)
			lyrics = getLyrics(file)
			processLyrics(lyrics, file)
		else:
			print('\t os.path.isfile returned False.')
	
	plt.show()

if __name__ == '__main__':
    main()
