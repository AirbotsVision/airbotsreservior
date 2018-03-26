import os
import sys
from collections import Counter        #import essential packages
import numpy as np 
from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB
from sklearn.svm import SVC,NuSVC,LinearSVC      
from sklearn.metrics import confusion_matrix


def makedictionary(train_dir):
	count=0
	for f in os.listdir():                 #open the training file and process it
		if f.endswith(".eml"):
			count+=1
			print(count)                     
			email=(os.path.join("C:\\Users\\Iyantras\\TRAINING",f))
	allwords=[]
	with open(email) as w:             #get the words in the file
		for i,lines in enumerate(w):
			if((i)==21):
				words=lines.split()      #splitthe lines 
				allwords+=words
	dictionary=Counter(allwords)       #create a dictioanary with words and its index
	for item in list(dictionary):      
		if item.isalpha()==False:      #if a words exceeds its range then it has ti be trained as spam
			del dictionary[item]         
		elif len(item)==1:            
			del dictionary[item]         #delete th word from the  dictionary and add that word to the another list 
	dictionary=dictionary.most_common(3000)
	print(dictionary)
	return dictionary

train_dir=os.chdir("C:\\Users\\Iyantras\\TRAINING")
dictionary=makedictionary(train_dir)                    

def extract_features(mail_dir): 
	count=0                                        #open the testing  folder
	for f in os.listdir():
		if f.endswith(".txt"):
			count+=1                                 #check whether the file ends with the text and append a file to it
			print(count)
			files=(os.path.join("C:\\Users\\Iyantras\\TESTING",f))
	features_matrix = np.zeros((len(files),3000))
	docID = 0              
   	with open(files) as f:
		for i,line in enumerate(fi):             #open each of those files and process it
			if i == 2:                                       
				words = line.split()
				for word in words:                  #check for each word in a file
					wordID =0
					for i,d in enumerate(dictionary):
						if d[0] == word:                   #check whether the words are present in a dicionary
							wordID = i
					features_matrix[docID,wordID] = words.count(word) #if present then add it to the features matri function
		docID = docID + 1     
	return features_matrix

train_labels = np.zeros(702)
train_labels[351:701] = 1                   #finally train the files 
train_matrix = extract_features("C:\\Users\\Iyantras\\TRAINING")

# Training SVM and Naive bayes classifier

model1 = MultinomialNB()
model2 = LinearSVC()
model1.fit(train_matrix,train_labels)
model2.fit(train_matrix,train_labels)

# Test the unseen mails for Spam
test_dir = 'test-mails'
test_matrix = extract_features("C:\\Users\\Iyantras\\TRAINING")
test_labels = np.zeros(260)
test_labels[130:260] = 1
result1 = model1.predict(test_matrix)
result2 = model2.predict(test_matrix)
print (confusion_matrix(test_labels,result1))
print (confusion_matrix(test_labels,result2))