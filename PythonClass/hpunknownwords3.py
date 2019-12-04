import re #allows us to use regular expressions - A way of defining characters that we will include or exclude in our searches.

f = open ("words") #opens the dictionary of stopwords that we are going to use to remove all the 'normal' words in Lovecrafts tales
f = [item.lower() for item in f] #makes all the words lowercase - which we need in for matching - captials matter
stops = set() # creates a set called stops, sets are collections of distinct elements with no order
for word in f: #for each line in f, 
	stops.add(word.strip())  #since each item is a single word, we can strip off any whitespace and add that word to the set called stops we created

print (sorted(stops)[11000:11100], "\n") #check to show that we have a set 

#Now we have the stop words we are not interested in prepared as a set for python to use

f = open ("lovecraft") #Opens the lovecraft text file
f = [item.lower() for item in f] #Converts all the text to lowercase, case matters for comparison to dictionary
words = []  #square brackets indicate a list, lists can have repetitive elements, and maintains a specific order
for line in f:
	words.extend(re.findall("[A-z\-\']+", line.strip()))#Eliminates numbers but includes hyphenated words, which is relevant to Loveraft's unique entity and place names
#words.extend - means we are adding the results to the end of the list words that we have created
#re.findall, turns the text into a list of words, looking for anything that includes A-Z, hyphen, or apostrophe, line.strip removes all whitespace from each word

#Now we have a list of words from the stories, in order, and a set of stop words(words we want to ignore)



wcount = dict()  #create a dictionary -  associative array - key:value pair
for w in words:   #for each word in the text
	if w in stops: #if the word is in stops
		continue    #keep going
	if w in wcount:  #if word is already in dictionary
		wcount[w]+=1  #add one to the value
	else:              #if not in the dictionary or the stops, 
		wcount[w]=1     #make the word count 1 for that word


print ("New word count:", len(wcount), "\n")      #print the length of that dictionary


wlist = sorted(wcount, key=wcount.get, reverse=True)    #create a new set using wcount, that is sorted by the values for each key, and then listed in reverse order, so it starts with the greatest
for i in wlist[1:100]:         #prints the first 100 values in the new list
	print (i, wcount[ i ])