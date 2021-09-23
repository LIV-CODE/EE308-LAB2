# Copyright by Zhenshuo Chen.
# FZU:831901313
# MU:19104979
# Function: C++ code for keyword and structure recognition.
import re

# Keyword dictionary
dict = {'auto':0, 'break':0, 'case':0, 'char':0, 'const':0, 'continue':0, 'default':0, 'do':0, 
'double':0, 'else':0, 'enum':0, 'extern':0, 'float':0, 'for':0, 'goto':0, 'if':0, 'int':0, 'long':0, 
'register':0, 'return':0, 'short':0, 'signed':0, 'sizeof':0, 'static':0, 'struct':0, 'switch':0, 
'typedef':0, 'union':0, 'unsigned':0, 'void':0, 'volatile':0, 'while':0}

# Class of stack
class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def value(self,num):
        return self.items[num]
    def size(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def peek(self):
        return self.items[len(self.items)-1]
    def pop(self):
        return self.items.pop()

# ------------function-------------
# Count the number of keywords
def key_num():
    words = re.findall(reg, text)
    for word in words:
	    if word in dict:
		    dict[word]+=1
    print("total num: ", sum(dict.values()))

# Count the number of switch and case
def switch_num():
    lineNum1=0
    # Record the number of lines where the switch resides
    list1=[]
    for line in codeList:
        words = re.findall(reg, line)
        lineNum1+=1
        for word in words:
            if word=="switch":
                list1.append(lineNum1)
    list1.append(lineNum1)
    # Records the number of lines read
    lineNum2=0
    # Record the number of cases under each switch
    list2=[]
    indexSwitch=1
    caseNum=0
    for line in codeList:
        words = re.findall(reg, line)
        lineNum2+=1
        # Intercepts the content between specified lines
        if lineNum2>=list1[indexSwitch-1] and lineNum2<list1[indexSwitch]:
            for word in words:
                if word=="case":
                    caseNum+=1
        else:
            if caseNum != 0:
                list2.append(caseNum)
            if lineNum2>list1[0]:
                indexSwitch+=1
            caseNum=0
            if indexSwitch>=len(list1):
                break

    print("switch num: ", dict["switch"])
    print("case num: ",end="")
    print(*list2, sep=' ')

# Count the number of if_else and if-elif-else
def if_else_elseif_num(level):
    # change "else if" to "elseif"
    text_elseif = replace_space(text)
    line_elseif = re.findall(reg, text_elseif)
    ifelseNum = 0
    ifelifelseNum = 0
    ifelifelseFlag = 0
    stack = Stack()
    for word in line_elseif:
        if word == 'if':
            stack.push('if')
        elif word == 'elseif' and stack.value(-1) == 'if':
            stack.push('elseif')
        elif word == 'else':
            while (stack.value(-1) != 'if'):
                ifelifelseFlag = 1
                stack.pop()
            stack.pop()
            if  ifelifelseFlag:
                ifelifelseNum += 1
                ifelifelseFlag = 0
            else:
                ifelseNum += 1
    if level==3:
        print("if-else num: ", ifelseNum)
    elif level==4:
        print("if-else num: ", ifelseNum)
        print("if-elif-else num: ", ifelifelseNum)

# Replace Spaces between else and if
def replace_space(text):
    reg = r"\be.*?f\b"
    comment = re.finditer(reg,text)
    for match in comment:
        text = text.replace(match.group(),'elseif')
    return text

# -------------main--------------
# Regular expression
# The regular expression matches all the required values and returns a list
reg = r'\b[a-zA-Z]+\b'

path = input("Please enter your code address: ")
level = int(input("Please input the level you want(1,2,3,4)"))

#Read the code
with open(path, encoding='utf8') as f:
# with open('key.c', encoding='utf8') as f:
	codeList=[]
	for line in f:
		codeList.append(line)
	text = "".join(codeList)

if level == 1:
    key_num()
elif level == 2:
    key_num()
    switch_num()
elif level == 3 or level == 4:
    key_num()
    switch_num()
    if_else_elseif_num(level)
else:
    print("wrong number!")
