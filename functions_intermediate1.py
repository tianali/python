import random
def randInt(min=0 , max=100 ):
    if min>max:
        return "min is greater than max"
    if max<0: 
        return "we don't want a negative max"
    if ((min==0) and (max==100)):
        num = random.random() * 100
    if ((min!=0) and (max!=100)):
        num = random.random()* (max - min) + min
        return num
    if max!=100:
        num = random.random() * max
    if min!=0:
        num= random.random() * min + 50
    return num
print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
print(randInt(min=50, max=20))      #should print string
print(randInt(min=-8, max=-5))      #should print string