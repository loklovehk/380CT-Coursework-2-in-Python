import math
import time
import random

def create(n, min_d, max_d):
      stack =[]
      # n is the amount of element
      for i in range (n):    
          stack.append(random.randrange(min_d,max_d,1))
      stack.sort(reverse=True)
      #create a random number for target
      target = random.randrange(max_d*(len(str(max_d)))) 
      # return the array and the target
      return stack, target

def powersert (element):
      result = [[]]
      # take out element in the array 
      for item in element:
            newset = [r+[item] for r in result]
            result.extend(newset)
      return result

def display( stack ,target):
      s = stack
      t = target
      #print out the array
      print "data" ,s
      #getting the 
      for a in range (len(powersert(s))):
            line = (powersert(s))[a]
            total= sum((powersert(s))[a])
            print "substring %s  Total: %s"%(line,total)
            if (total == target):
                  print "\n\nThe answers is below: "
                  print "substring %s  Total: %s"%(line,total)
                  break
      print"None of subset total is: %s"%target 



#s = [12, 24, 52, 90, 56, 23, 10]
#t = 134
#Generate the array      
c = create(10,1, 101)
# array is the first element of the return value
s = c[0]
# target is the srcond element of the return value
t = c[1]
Tstart = time.time()
display(s,t)
print "The algorithm finish in %s seconds."%(time.time() - Tstart)      
