#Maddie Stigler
#mgs4ff
#1/20/15
#HW1

import math


#classified items object
class Classified(object):
  def __init__(self, category, x, y):
    self.category = category
    self.x = float(x)
    self.y = float(y)
    self.distance = 0
    
  def set_distance(self, x, y):
    self.distance = math.sqrt(pow(abs(self.x - float(x)), 2) + pow(abs(self.y - float(y)), 2))
    

#prompt user for k value
k = int(raw_input("Please enter a value for k: "))

#prompt user for M value
M = int(raw_input("Please enter the number of values to be read from the file: "))

#prompt user for data file name
dataFile = raw_input("Please enter the data file name: ")

#prevent k from being larger than M
if M < k:
  k = M

#create list of classified objects (M)
classified_objects = [ ]

#open file, for 1-M, read line and add to list
f = open(dataFile, 'r')
for i in range(0, M):
   dataLine = f.readline().split()
   cObject = Classified(dataLine[0], dataLine[1], dataLine[2])
   classified_objects.append(cObject)  
f.close()

#Get unclassified
unclassified = " "

while unclassified != "1.0 1.0":
  unclassified = raw_input("Please enter an (X,Y) value pair for unclassified data: ") 
  if unclassified == "1.0 1.0": break
  unclassified = unclassified.split()
  x = unclassified[0]
  y = unclassified[1]
  for Classified in classified_objects:
    Classified.set_distance(float(x), float(y))
    
#print set of k nearest points nearest first (category, xy values, distance)
  cat1 = 0
  cat2 = 0
  cat1_sum = 0
  cat2_sum = 0
  classified_objects.sort(key=lambda x:x.distance)
  category1 = classified_objects[0].category
  category2 = " "
  for i in range(0, k):
    category = classified_objects[i].category
    if category1 == category:
      cat1 += 1
      cat1_sum += classified_objects[i].distance
    else:
      category2 = category
      cat2 += 1
      cat2_sum += classified_objects[i].distance
    print category + " " + str(classified_objects[i].x) +  " " + str(classified_objects[i].y) + " " + str("%.1f" % classified_objects[i].distance)



#print category data item belongs to ("Data item (x, y) assigned to: ")

  if(cat1 == cat2):
      tieBreaker = classified_objects[0].category
      print "Data item assigned to: " + str(tieBreaker)
  elif(cat1 > cat2):
      print "Data item assigned to: " + str(category1)
      
  else:
      print "Data item assigned to: " + str(category2)
  

#print avg distance to category items ("Average distance to category1 items: ")
  cat1_avg = cat1_sum/cat1
  print "Average distance to cat1 items: " + str("%.1f" % cat1_avg)
  if(cat2 == 0):
    print "There are no cat2 items within k of the unclassified point."
  else:
    cat2_avg = cat2_sum/cat2
    print "Average distance to cat2 items: " + str("%.1f" % cat2_avg)# CS3240
