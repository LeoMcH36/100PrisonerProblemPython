import random

#prisoner class
class Prisoner:
  #the first param is also the object itself does not have to be called self
  def __init__(self, number):
    self.number = number
    self.success = False
   
#box class
class Box:
  def __init__(self, outsideNumber, insideNumber):
    self.outsideNumber = outsideNumber
    self.insideNumber = insideNumber

#because outside numbers are ordered we can reduce time complexity by using binary search
def binary_search(boxes, low, high, insideNumCurrent):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if boxes[mid].outsideNumber == insideNumCurrent:         
            boxes[mid].insideNumber
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif boxes[mid].outsideNumber > insideNumCurrent:
            return binary_search(boxes, low, mid - 1, insideNumCurrent)
        # Else the element can only be present in right subarray
        else:
            return binary_search(boxes, mid + 1, high, insideNumCurrent)
    else:
        # Element is not present in the array 
        return -1

# #**********************************************************************************
# #Set Up Loop selection attempt
# #**********************************************************************************
#successful runs variable
wins = 0
#simulation runs
runs = 10000
for loop in range(runs):
  print("****************************************** Run: " , loop + 1)
  #create list of numbers from 1 - 100
  numbers = range(1,101)
  #create a list that doesnt change to reset things in the future
  numbersOG = list(numbers).copy()
  #list to be changed
  numbersNew = numbersOG.copy()
  
  #lists to hold prisoner and box objects
  prisoners = []
  boxes = []
  #size of list to use in for loop
  listSize = len(numbersOG)
  
  #go through numbers list
  for i in range(listSize):
    #get number, create prisoner and add prisoner to list
    rNumPris = numbersNew.pop(random.randint(0,len(numbersNew) - 1))
    tP1 = Prisoner(rNumPris)
    prisoners.append(tP1)

  #reset numbers list
  numbersNew = numbersOG.copy()

  for x in range(1,listSize + 1):
    #same as above but with boxes
    #outside boxes dont have to be randomised
    rNumBoxOutside = x
    rNumBoxInside = numbersNew.pop(random.randint(0 ,len(numbersNew) -1 ))
    tB1 = Box(rNumBoxOutside,rNumBoxInside)
    boxes.append(tB1)

  #reset boxes
  numbersNew = numbersOG.copy()
  boxesOG = boxes.copy()

  #each run reset prisoners
  for prisoner in prisoners:
    prisoner.success = False
  #how many prisoners were successful
  successfulAttempts = 0

#for each prisoner
  for prisoner in prisoners:
    #hold the inside number they've just seen
    insideNumCurrent = 0
    #reset boxes after each prisoner
    boxes = boxesOG.copy()
    #fifty attempts per prisoner
    for attempt in range(1,51): 
      #if the last prisoner was successfull last box stop move to next prisoner
      if insideNumCurrent == prisoner.number:
          prisoner.success = True
          break
      #on first attempt choose the prisoner's number where it is the outside number
      if attempt == 1:
        #pop open  box and get inside number and set it to current inside number to look for
        boxIndex = -1
        for b in boxes:
          boxIndex += 1
          if b.outsideNumber == prisoner.number:
            insideNumCurrent = boxes.pop(boxIndex).insideNumber 
                    
      #on every other attempt, follow the loop
      if attempt > 1: 
        #search the boxes for match
        insideNumCurrent = boxes.pop(binary_search(boxes, 0, len(boxes), insideNumCurrent)).insideNumber
        #check success
        if insideNumCurrent == prisoner.number:
          prisoner.success = True
          break
#if there were 100 successes out of 100 prisoners save as a win
  for prisoner in prisoners:
    if prisoner.success == True:
      successfulAttempts += 1
  if successfulAttempts == 100:
    wins += 1
    #tab'd to make slightly more visible
    print("\t\t\t\t\t\tSuccessful run")
  else:
    print("UnSuccessful run")
                
  
#Useful Stats
print("Amount of successful runs: ",wins)
successPercentage = (wins/runs) * 100
print("Success rate:",successPercentage, "%")

