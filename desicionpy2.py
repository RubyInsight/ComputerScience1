#Awesome Decision Making Program
#import modules
import random

#questions
userQue = raw_input("Ask me a yes or no question, Type your question then press ENTER. \n ")


#results
result1 = "It is certain"
result2 = "It is decidedly so"
result3 = "Without a doubt"
result4 = "Yes, definitely"
result5 = "You may rely on it"
result6 = "As I see it, yes"
result7 = "Most likely"
result8 = "Outlook good"
result9 = "Yes"
result10 = "Signs point to yes"
result11 = "Reply hazy try again"
result12 = "Ask again later"
result13 = "Better not tell you now"
result14 = "Cannot predict now"
result15 = "Concentrate and ask again"
result16 = "Don't count on it"
result17 = "My reply is no"
result18 = "My sources say no"
result19 = "Outlook not so good"
result20 = "Very doubtful"

#flip
import time
time.sleep(3) #delay for 3 seconds 
print"..."
raw_input("press ENTER when you're ready for my answer.")

#test
coinResult = random.randint(1,20)

if coinResult == 1:
    answer=result1
elif coinResult == 2:
    answer=result2
elif coinResult == 3:
    answer=result3
elif coinResult == 4:
    answer=result4
elif coinResult == 5:
    answer=result5
elif coinResult == 6:
    answer=result6
elif coinResult == 7:
    answer=result7
elif coinResult == 8:
    answer=result8
elif coinResult == 9:
    answer=result9
elif coinResult == 10:
    answer=result10
elif coinResult == 11:
    answer=result11
elif coinResult == 12:
    answer=result12
elif coinResult == 13:
    answer=result13
elif coinResult == 14:
    answer=result14
elif coinResult == 15:
    answer=result15
elif coinResult == 15:
    answer=result16
elif coinResult == 17:
    answer=result17
elif coinResult == 18:
    answer=result18
elif coinResult == 19:
    answer=result19
else:
    answer=result20




#print the answer
print"answer"