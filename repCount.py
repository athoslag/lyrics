import os
import string

reps = []

def removePunctuation(strList):
	translator = str.maketrans('', '', string.punctuation)
	newList = []
	
	for item in strList:
		newList.append(item.translate(translator))

	return newList

def saveReps():
	output = open("repetitiveness.txt", "w+")

	for rep in reps:
		output.write('%s\n' % rep)
		
	output.close

def countSong(originalLyrics, fileName):
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
		if occurencies[key] is 1:
			onlyOnce += 1

	repetitiveness = (len(lyrics) - onlyOnce) / len(lyrics)
	print("\t " + fileName + " repetitiveness: {0:.2%}".format(repetitiveness))

	reps.append(fileName.split('.')[0] + ": {0:.2%}".format(repetitiveness))

def getLyrics(file):
	f = open(os.path.join('songs/',file),'r')
	lyrics = f.read()
	f.close()
	return lyrics

def main():
	files = os.listdir('songs/')

	for file in sorted(files):
		if os.path.isfile("songs/" + file):
			lyrics = getLyrics(file)
			countSong(lyrics, file)
		else:
			print('\t os.path.isfile returned False.')

	saveReps()

if __name__ == '__main__':
    main()
