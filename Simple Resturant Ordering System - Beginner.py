print("welcome to my shop! What is you name")
name = input("")
 
print("Well that is great, Mr.", name, "What do you want to order today? Here is our list\n Bannana Juice, Apple Mint, Orange Juice")

order = input("")

print("Well, that sound a great idea for a morning walk! Mr.", name, "your", order, "will be ready in just few mins!\n\n Want to see what is going on in the world by getting a morning brew newspaper from our shop?")

newsresponse = input("")

if newsresponse == "Yes":
    print("Here is you newspaper sir")

elif newsresponse == "No":
    print("Ok, then please just wait for a few mins!")

else:
    print("Ok, as you wish")