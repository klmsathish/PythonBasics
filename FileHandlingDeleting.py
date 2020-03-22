with open ("one.txt","w") as r:
    r.write("my name is sathish")
'''
import os
os.remove("one.txt")
'''
with open("one.txt","r") as r:
    r.read()
