import re

dict = {'auto':0, 'break':0, 'case':0, 'char':0, 'const':0, 'continue':0, 'default':0, 'do':0, 
'double':0, 'else':0, 'enum':0, 'extern':0, 'float':0, 'for':0, 'goto':0, 'if':0, 'int':0, 'long':0, 
'register':0, 'return':0, 'short':0, 'signed':0, 'sizeof':0, 'static':0, 'struct':0, 'switch':0, 
'typedef':0, 'union':0, 'unsigned':0, 'void':0, 'volatile':0, 'while':0}

with open('codeTxt.txt', encoding='utf8') as f:
	lineNum1=0
	list1=[]
	for line in f:
		for ch in ", < > { } ( ) ; : = ! 聽":
			line=line.replace(ch," ")
		words=line.split()
		lineNum1+=1
		# print(words)
		for word in words:
			if word in dict:
				dict[word]+=1
				if word=="switch":
					list1.append(lineNum1)

with open('codeTxt.txt', encoding='utf8') as ff:
	list1.append(lineNum1)
	lineNum2=0
	list2=[]
	indexSwitch=1
	caseNum=0
	for line in ff:
		for ch in ", < > { } ( ) ; : = ! 聽":
			line=line.replace(ch," ")
		words=line.split()
		lineNum2+=1
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

with open('codeTxt.txt', encoding='utf8') as f:
	lineNum3=0
	if_else_num=0
	list3=[]
	point_if=0
	point_else=0
	for line in f:
		for ch in ", < > { } ( ) ; : = ! 聽":
			line=line.replace(ch," ")
		words=line.split()
		lineNum3+=1
		for word in words:
			if word=="if":
				point_if=lineNum3
				if point_else==lineNum3:
					if_else_num-=1
			if word=="else":
				point_else=lineNum3
				if point_if==lineNum3-1:
					if_else_num+=1
				

print("total num: ", sum(dict.values()))
print("switch num: ", dict["switch"])
print("case num: ",end="")
print(*list2, sep=' ')
print(if_else_num)