#About Python Program
#by Nicholas 

#import modules 
import time

#Opening
print("Make sure doc is opened to -------------------------------------------------------------------------------------------------------------------------->")
print("\n")
time.sleep(1) #wait one second
print("✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬✪ ✣ ✤ ✥✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬ ")
print("✬ Welcome to Nicholas's ✬")
print("✬         o           o                                      o           o__ __o                 o       o                                 ✬")                             
print("✬        <|>         <|>                                    <|>         <|     v\               <|>     <|>                                ✬")
print("✬        / \         / >                                    < >         / \     <\              < >     / >                                ✬")
print("✬      o/   \o       \o__ __o       o__ __o     o       o    |          \o/     o/   o      o    |      \o__ __o      o__ __o    \o__ __o  ✬")
print("✬     <|__ __|>       |     v\     /v     v\   <|>     <|>   o__/_       |__  _<|/  <|>    <|>   o__/_   |     v\    /v     v\    |     |> ✬")
print("✬     /       \      / \     <\   />       <\  < >     < >   |           |          < >    < >   |      / \     <\  />       <\  / \   / \ ✬")
print("✬   o/         \o    \o/      /   \         /   |       |    |          <o>          \o    o/    |      \o/     o/  \         /  \o/   \o/ ✬")
print("✬  /v           v\    |      o     o       o    o       o    o           |            v\  /v     o       |     <|    o       o    |     |  ✬")
print("✬ />             <\  / \  __/>     <\__ __/>    <\__ __/>    <\__       / \            <\/>      <\__   / \    / \   <\__ __/>   / \   / \ ✬")
print("✬                                                                                       /                                                  ✬")
print("✬                                                                                      o                                                   ✬")
print("✬                                                                                   __/>                                                   ✬")
print("✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬✪ ✣ ✤ ✥✬✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬✬✪ ✣ ✤ ✥ ✦ ✧ ✩ ✫ ✬")
time.sleep(1) #wait 1 second

#User Request 
print("Welcome to About Python \n")
print("1 - About Python     3 - About Strings")
print("2 - About Guido      4 - About Variables")
print("5 - About Algorithm  6 - About Input\n")
time.sleep(1) #wait 1 second
userReq = input("Input a number, to learn about that option.")

#Entries
aboutPython = "Python is a high-level general-purpose programming language which we learn how to use in computer science 1 it used for testing micro chips at Intel, to powering instagram to building video games with PyGame library. Python was conceived in the late 1980s, and its implementation began in December 1989 by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) . Python's original design goals—how he originally intended Python to bridge the gap between the shell and C,and how it eventually became used on large scale applications. Python is named after the television show Monty Python's Flying Circus. The main versions of Python are Python 3.x and Python 2.x.  The newest version of Python is Python 3.4.5 released on 2016-06-27."
aboutGuido = "Creator of Python which was made in 1989.He originally intended Python to bridge the gap between the shell and C, and how it eventually became used on large scale applications."
aboutStrings = "A string is a module that contains a number of useful constants and classes.  Are created by enclosing characters in quotes. Python treats single quote same as double quote."
aboutVar = "A variable is used as a assigned task that python reads."
aboutAlgorithm =" It is the a simple form of directions that the program follows."
aboutInput ="It is the action the user completes to interact with the program."

#Answers
if userReq == "1":
    answer = aboutPython
elif userReq == "2":
    answer = aboutGuido
elif userReq == "3":
    answer = aboutStrings
elif userReq == "4":
    answer = aboutVariables
elif userReq == "5":
    answer = aboutAlgorithm
else:
    answer = aboutInput


#Print Answer
print(answer)


#End Program
input("press ENTER/RETURN to end the program")