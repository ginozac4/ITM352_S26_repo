emotions = ("happy", "sad", "fear", "surprise")
# conditional expression - one that looks to see if a certain condition is met

result = emotions[-1] == "happy" and len(emotions) > 3
print(result)

if(result == True):
    print("True")
else:
    print("False")