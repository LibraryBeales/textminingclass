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

wcount = []  #creates a new list
for w in words:  
	if w in stops:
		continue
	else:
		wcount.append(w)  #if a word is in the stop word list, we continue, if not, we add it to the end of the list 'wcount'


print ("New word count:", len(wcount), "\n")      #print the length of that dictionary
		
print (sorted(wcount)[1:100])  #print out the first 100 words we have that are not in our dictionary


