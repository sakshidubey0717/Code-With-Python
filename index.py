print = ("Hello world")


'''
1 for snake 
-1 for water
o for gun
'''

computer =-1
youstr = input("Enter your choice:")
youDict ={"s":1,"w":-1, "g":0}
you = youDict[youstr]

if (computer ==-1 and you ==1):
    print("you win!")

elif(computer==-1 and you ==0):
    print("you Lose!")

if (computer ==1 and you ==-1):
    print("you Lose!")

elif(computer==1 and you ==0):
    print("you win!") 

if (computer ==0 and you ==-1):
    print("you win!")

elif(computer==0 and you ==1):
    print("you Lose!")
    
else:
    print("something went wrong!")
