#dictionary testing
diction ={"http":"hypetext transfer protocol","wwww":"world wide web","who":"world health organ"}
print(diction["http"])
retrieve = diction.get("who","oops, its not in here")
print(retrieve)
keyy = input("type ur keyword:\t")
valuedef = input("type ur definition:\t")
if keyy not in diction:
    diction[keyy] = valuedef
else:
    print("ur keyword already exists. will you replace?")
print(diction)

