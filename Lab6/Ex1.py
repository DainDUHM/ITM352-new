#Create a conditional expression that prints true if tupple is happy and 

#Contains at more than 3 conditional expressions 


emotions = ("anger", "sad", "fear", "jealous", "surprise", "happy")


print((len(emotions) > 3) and (emotions[len(emotions)-1] == "happy"))