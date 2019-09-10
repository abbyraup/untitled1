'''This is Homework Two for CSC 280 - 005 Fall 2019.
This will be distributed through Github Classroom.
Please fill in your name, and make sure your
code is executable. Each answer should show up properly
when I run the code while grading. 


Advice: If you wish to stop a process while it's running, hit Control-C
        Apple users: Command-C

'''

print("Name: ", 'Abby Raup')

# PROBLEM ONE:  Use www.pythontutor.com/visualize.html to help you!
print("")
print ("Problem one: ..... ..... ..... .....")
for i in range(2):
    for j in range(10):
        for k in range(10):
            if not (k+10*j+100*i) % 13:
                print(k+10*j+100*i)

# part A) How many lines of code will be executed overall when this
#        block of code runs?  (Replace ... with an integer.)
print("The block of code in problem one executes 461 lines of code when run.")

# part B) Summarize the contents of what prints, without giving a list of
#        the values which print.

print("The code in problem 1 starts with the values for i,j, and k being zero and "
      "plugs those values into the equation on the fourth line of code. "
      "The value is printed if there is no remainder when the output is divided by 13. "
      "First it will loop through keeping i=0 and j=0 and having k values of 0 up to 9. "
      "Then i=0,j=1, and k values zero to 9. "
      "Then i=0,j=2, k values 0-9 and this keeps going through all the range values. "
      "This keeps looping while only printing the values that are divisible by 13.")

# PROBLEM TWO: 
# Copy, paste, and adjust the code from problem one so that all positive
# multiples of 17 which are less than 300 will print.
print("")
print ("Problem two: ..... ..... ..... .....")
b=0
while b<300:
    for i in range(2):
        for j in range(10):
            for k in range(10):
                if not (k+10*j+100*i) % 17:
                    print(k+10*j+100*i)

    else:
        break


# PROBLEM THREE:
# Explain what happens when the code below is run as given.
# Then, adjust the code somehow so it does not happen when I run
# it as I grade your submission!
print("")
print ("Problem three: ..... ..... ..... .....")

c=0
while c<10:
    c=c+1
    print(c)

#when c is 0, it is always less than 10 so it gets to the second line when it says to print c and it keeps printing in a loop and doesn't get to the function with c.
#it needs to be rearranged

print("The code in problem three is going to always give an output of zero "
      "because it keeps plugging 0 in for c and 0 is always less than 10 so it keeps going")
print("I kept that from happening by assuming the goal was to get it to give the output of "
      "1 through 10 but honestly I'm not sure.")

# PROBLEM FOUR: Create a list of 10 strings. Then, print out the third and
#               seventh items.
print('Two problem 4-looking things showed up on my HW so I just did them both')
L=["hi","i","think","this",'is','left','over','from','HW', '1']
print(L[2])
print(L[6])

print("")
print ("Problem four: ..... ..... ..... .....")
# Explain why the code prints what it does in the block below:
for e in range(13,8,-1):
    print(e)
#it is going to start at 13 and count backwards by 1 and stop before 8. because the first number is the starting point
# and it's going to stop before getting to the stopping point(8).
# The last number is how much it's going to skip by and since it's negative it is going to go backwards by negative 1.


# PROBLEM FIVE: Explain at a high level what goes "wrong" in this code:
# Also, adjust it so that doesn't happen while I'm grading.

x=1
y=10
while(x+1<y):
    x=x+1
    y=y-1
print(x,y,"x=y now!")


#once x=y, the program does not stop
#so i fixed it so it stops and doesnt do a continuous loop but I could not figure out how to get it to stop
# and compare once they were both equal within the loop so I made it so that they would be equal coming out of the loop
#idk i spent an hour tinkering on this problem and have to be done

    

