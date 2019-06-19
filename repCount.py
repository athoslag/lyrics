import os
import string

def removePunctuation(strList):
	translator = str.maketrans('', '', string.punctuation)
	newList = []
	
	for item in strList:
		newList.append(item.translate(translator))

	return newList

def countSong(originalLyrics):
	words = []
	occurencies = {}
	lyrics = removePunctuation(originalLyrics.split())

	for word in lyrics:
		if word in words:
			occurencies[word] += 1
		else:
			words.append(word)
			occurencies[word] = 1

	onlyOnce = 0

	for key in occurencies:
		print('[%s]: %i' % (key, occurencies[key]))
		if occurencies[key] is 1:
			onlyOnce += 1

	repetitiveness = (len(lyrics) - onlyOnce) / len(lyrics)
	print("Repetitiveness: {0:.2%}".format(repetitiveness))

def getLyrics(file):
	f = open(os.path.join('songs/',file),'r')
	lyrics = f.read()
	f.close()
	return lyrics

def main():
	files = os.listdir('songs/')

	for file in sorted(files):
		if os.path.isfile("songs/" + file):
			print('Processing %s...' % file)
			lyrics = getLyrics(file)
			countSong(lyrics)
		else:
			print('os.path.isfile returned False.')

if __name__ == '__main__':
    main()
