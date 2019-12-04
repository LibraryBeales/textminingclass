import re  #Import regular expressions into memory.  We will need these to define what kinds of words Python is looking for in different commands.

f = open("words") #Open the list of stop words we have in the file called 'words' and assign the file to a variable
f = [item.lower() for item in f] #Look at each word, and convert any capital letters to lowercase

stops = set() #Create an empty SET called 'stops', so we can use our words more effectively in Python
for word in f:
	stops.add(word.strip())#Look at each word in the file 'words'.  Remove the whitespace, and add it to the SET called 'stops'.


#print (sorted(stops)[10000:10900], "\n")#Look at the SET 'stops' so we can make sure we have what we want.

f = open("lovecraft") #Open the list of stop words we have in the file called 'words' and assign the file to a variable
f = [item.lower() for item in f] #Look at each word, and convert any capital letters to lowercase

words = []
for line in f:
	words.extend(re.findall("[A-z\-\']+", line.strip()))

#print (words[1:100], "\n")

#wcount = []
#for w in words:
#	if w in stops:
#		continue
#	else:
#		wcount.append(w)

#print("New word count:", len(wcount), "\n")
#print(sorted(wcount)[1:100], "\n")

wcount = dict()
for w in words:
	if w in stops:
		continue
	if w in wcount:
		wcount[w]+=1
	else:
		wcount[w]=1

print("New word count:", len(wcount), "\n")

wlist = sorted(wcount, key=wcount.get, reverse=True)

for i in wlist[1:100]:
	print (i, wcount[i])



#dictionary   key:value
#Open the text file called 'lovecraft' 
#Look at each word, and convert any capital letters to lowercase

#Create an empty LIST called 'words', so we can use our text more effectively in Python
#Look at each word in the file 'lovecraft'.  Remove the whitespace, and add it to the LIST called 'words'.  BUt onlu find words that use a-z, hyphens and apostrophes.

#Create a third empty LIST called 'wcount'
#Go through the LIST of words we created from the lovecraft text.
#Compare each one to the SET of stopwords we created.

#If the word is not in the SET of stopwords, then we add it to the LIST wcount

#Show how many unique words we found in the lovecraft stories.  
#Show the first 100 words in the list...


