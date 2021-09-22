# Keyword dictionary
dict = {'auto':0, 'break':0, 'case':0, 'char':0, 'const':0, 'continue':0, 'default':0, 'do':0, 
'double':0, 'else':0, 'enum':0, 'extern':0, 'float':0, 'for':0, 'goto':0, 'if':0, 'int':0, 'long':0, 
'register':0, 'return':0, 'short':0, 'signed':0, 'sizeof':0, 'static':0, 'struct':0, 'switch':0, 
'typedef':0, 'union':0, 'unsigned':0, 'void':0, 'volatile':0, 'while':0}
# path = input("Please enter your code address: ")
# level = int(input("Please input the level you want(1,2,3,4)"))

#Read the code
with open('key.c', encoding='utf8') as f:
	# Records the number of lines read
	lineNum1=0
	codeList=[]
	# Record the number of lines where the switch resides
	list1=[]
	for line in f:
		# Replace the symbol with " "
		for ch in ", < > { } ( ) ; : = !":
			line=line.replace(ch," ")
		# codeList.append(words)
		words=line.split()
		lineNum1+=1
		for word in words:
			if word in dict:
				dict[word]+=1
				if word=="switch":
					list1.append(lineNum1)
with open('key.c', encoding='utf8') as f:
	list1.append(lineNum1)
	# Records the number of lines read	
	lineNum2=0
	# Record the number of cases under each switch
	list2=[]
	# Interval pointer that intercepts the content between specified lines
	indexSwitch=1
	caseNum=0
	for line in f:
		for ch in ", < > { } ( ) ; : = !":
			line=line.replace(ch," ")
		words=line.split()
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
# with open('codeTxt.txt', encoding='utf8') as f:
# 	lineNum3=0
# 	if_else_num=0
# 	# Indicates the number of rows
# 	point_if=0
# 	point_else=0
# 	for line in f:
# 		for ch in ", < > { } ( ) ; : = !":
# 			line=line.replace(ch," ")
# 		words=line.split()
# 		lineNum3+=1
# 		for word in words:
# 			if word=="if":
# 				point_if=lineNum3
# 				if point_else==lineNum3:
# 					if_else_num-=1
# 			if word=="else":
# 				point_else=lineNum3
# 				if point_if==lineNum3-1:
# 					if_else_num+=1
				
print("total num: ", sum(dict.values()))
print("switch num: ", dict["switch"])
print("case num: ",end="")
print(*list2, sep=' ')
# print("if else num: ",if_else_num)