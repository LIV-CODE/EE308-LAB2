import re

reg = r'\b[a-zA-Z]+\b' #正则表达式匹配英文单词
# 正则表达式匹配所有符合要求的值，返回一个列表

# Keyword dictionary
dict = {'auto':0, 'break':0, 'case':0, 'char':0, 'const':0, 'continue':0, 'default':0, 'do':0, 
'double':0, 'else':0, 'enum':0, 'extern':0, 'float':0, 'for':0, 'goto':0, 'if':0, 'int':0, 'long':0, 
'register':0, 'return':0, 'short':0, 'signed':0, 'sizeof':0, 'static':0, 'struct':0, 'switch':0, 
'typedef':0, 'union':0, 'unsigned':0, 'void':0, 'volatile':0, 'while':0}
# path = input("Please enter your code address: ")
# level = int(input("Please input the level you want(1,2,3,4)"))

class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def value(self,num):
        return self.items[num]

def key_num():
    for word in words:
	    if word in dict:
		    dict[word]+=1
    print("total num: ", sum(dict.values()))

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
    # Interval pointer that intercepts the content between specified lines
    indexSwitch=1
    caseNum=0
    for line in codeList:
        # Replace the symbol with " "
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

def if_else_elseif_num():
    # change "else if" to "elseif"
    text_elseif = replace_space(text)
    line_elseif = re.findall(reg, text_elseif)
    ifelse_num = 0
    ifelifelse_num = 0
    ifelifelse_flag = 0
    stack = Stack()
    for kw in line_elseif:
        if kw == 'if':
            stack.push('if')
        elif kw == 'elseif' and stack.value(-1) == 'if':
            stack.push('elseif')
        elif kw == 'else':
            while (stack.value(-1) != 'if'):
                ifelifelse_flag = 1
                stack.pop()
            stack.pop()
            if ifelifelse_flag:
                ifelifelse_num += 1
                ifelifelse_flag = 0
            else:
                ifelse_num += 1

    print('if-else num: {}'.format(ifelse_num))
    print('if-elif-else num: {}'.format(ifelifelse_num))

def replace_space(text):
    reg = r"\be.*?f\b"
    comment = re.finditer(reg,text)
    for match in comment:
        text = text.replace(match.group(),'elseif')
    return text

#Read the code
with open('key.c', encoding='utf8') as f:
	codeList=[]
	for line in f:
		codeList.append(line)
	text = "".join(codeList)
words = re.findall(reg, text)

key_num()
switch_num()
if_else_elseif_num()