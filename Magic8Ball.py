import random
import time
import sys
import os



answerRand = random.randrange(0,29)
print("   ___  ____        _ _ ")
print("  / _ \|  _ \      | | |")
print(" | (_) | |_) | __ _| | |")
print("  > _ <|  _ < / _` | | |")
print(" | (_) | |_) | (_| | | |")
print("  \___/|____/ \__,_|_|_|")


while True:
    question = input("Greetings mortal creature. Ask me a single YES or NO question...: ")

    if question !='':
        break
    else:
        print("")
        print("(￣^￣)      You're supposed to ask me something. I'll ask you again...")
        print ("")

print("----------------")

print("(ー_ーゞ Hmm, let me think...")

time.sleep(2.0)

filename = 'demo.txt'
try:
    file = open(filename, "r")
    contents = file.read()
    list_of_contents = contents.split(",")
    file.close()
except FileNotFoundError:
    errormsg = "Sorry, the required file : "+ filename + "doesn't exist. Make sure it's in the parent directory, please."
    print(errormsg)
    sys.exit("Program Closed.")

#print(list_of_contents)

time.sleep(2.0)
print("")
print('The answer to your question of :',question,' is...')
print("")
time.sleep(2.0)
print("----------------")
print(list_of_contents[answerRand])
print("")
print("")
print("      ::::    :::  ::::::::  :::       :::          :::::::::     :::   :::   :::            :::   :::   ::::::::::    ")
print("     :+:+:   :+: :+:    :+: :+:       :+:          :+:    :+:  :+: :+: :+:   :+:           :+:+: :+:+:  :+:            ")
print("    :+:+:+  +:+ +:+    +:+ +:+       +:+          +:+    +:+ +:+   +:+ +:+ +:+           +:+ +:+:+ +:+ +:+             ")
print("   +#+ +:+ +#+ +#+    +:+ +#+  +:+  +#+          +#++:++#+ +#++:++#++: +#++:            +#+  +:+  +#+ +#++:++#         ")
print("  +#+  +#+#+# +#+    +#+ +#+ +#+#+ +#+          +#+       +#+     +#+  +#+             +#+       +#+ +#+               ")
print(" #+#   #+#+# #+#    #+#  #+#+# #+#+#           #+#       #+#     #+#  #+#             #+#       #+# #+#        #+#     ")
print("###    ####  ########    ###   ###            ###       ###     ###  ###             ###       ### ########## ###      ")
