#1 Basic - Print all integers from 0 to 150
for x in range(151):
    print(x)

#2 Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for y in range(1001):
    if y % 5 == 0:
        print(y)

#3 Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo". 
for z in range(1, 101):
    if z % 10 == 0:
        print("Coding Dojo")
    elif z % 5 == 0:
        print("Coding")
    else:
        print(z)

#4 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for a in range(500000):
    if a % 2 == 1:
        sum = sum + a
print(sum)

#5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for c in range(2018, 0, -4):
    print(c)

#6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for d in range(lowNum, highNum+1):
    if d % mult == 0:
        print(d)
