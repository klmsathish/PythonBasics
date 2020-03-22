msg = input("enter a message = ")
msg = msg.lower()
Dict = dict()
for word in msg :
    if word not in Dict:
        Dict[word] = 1
    else:
        Dict[word]=Dict[word]+1
print(Dict)
for key,val in Dict.items():
    print(key,"#"*val)