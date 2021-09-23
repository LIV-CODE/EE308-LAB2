# EE308-LAB2
## Problem-solving ideas

​		This is our first soft programming assignment. It require independent completion of a program from design to testing process. I think this is a very challenging assignment. As a newcomer to code, I must start with **Git** and **GitHub**.

### Git&GitHub

​		**GitHub** is the **world's largest remote repository for software**. It is a hosting platform for open source and private software projects, using **Git** for **distributed version control**. Simply put, GitHub is one of the places where programmers and organizations publish code, and where programmers from all over the world upload their code to share it.

> Here's a tutorial that's easy to understand: [Git和GitHub使用教程 - 简书 (jianshu.com)](https://www.jianshu.com/p/296d22275cdd)

​                           <img src="https://upload-images.jianshu.io/upload_images/4064394-eed044759e8ad893.png?imageMogr2/auto-orient/strip|imageView2/2/w/823/format/webp" alt="img" style="zoom:25%;" /><img src="https://upload-images.jianshu.io/upload_images/4064394-badc6aa178c1173b.png?imageMogr2/auto-orient/strip|imageView2/2/w/509/format/webp" alt="img" style="zoom:25%;" />     



### Analyze requirements & Select the language

​		This assignment is for any programming language, and we need to choose our own implementation method. The core of the job requirement is to retrieve keywords and structures in the code. Consider that we've learned languages like Python and C++, I thought about using smarter **Python** to do the job.

### Debug programming environment

| Programming language | Python3.7     |
| -------------------- | ------------- |
| **Compiler**         | **VS Code**   |
| **Package manager**  | **Anaconda3** |

#### VS Code

​		I chose to use **vscode** as the compiler because it is smart enough to work with a variety of languages. I installed the git plug-in in vscode for code version control directly within the compiler. Each time you commit a change, you simply add a comment and commit it to the local library and then push it to the remote branch.

![image]https://github.com/LIV-CODE/EE308-LAB2/blob/main/image/image-20210923190118931.png

#### Python with Anaconda3

​			**Anaconda** is a distribution that makes it easy to get packages, manage packages, and manage the environment in a unified way. Anaconda includes more than 180 science packages and their dependencies, including **Conda** and **Python**.

​			The Anaconda environment makes it easy to configure python versions and required packages.

> Here's a tutorial that's easy to understand: [Anaconda+VSCode搭建python环境 - 简书 (jianshu.com)](https://www.jianshu.com/p/f10fb1a4cc87)

## Design and implementation process

### main structure

<img src="C:\Users\22478\AppData\Roaming\Typora\typora-user-images\image-20210923195049306.png" alt="image-20210923195049306" style="zoom:80%;" />

### keyword number

<img src="C:\Users\22478\AppData\Roaming\Typora\typora-user-images\image-20210923201556987.png" alt="image-20210923201556987" style="zoom:80%;" />

### switch_case number

<img src="C:\Users\22478\AppData\Roaming\Typora\typora-user-images\image-20210923203146632.png" alt="image-20210923203146632" style="zoom:80%;" />

### if else & if else_if else num

<img src="C:\Users\22478\AppData\Roaming\Typora\typora-user-images\image-20210923204437705.png" alt="image-20210923204437705" style="zoom:80%;" />

## Code description

### main code

- Input
- Read the file
- Judgment level
- Call functions
- Output

##### Regular expression

Regular expressions can be used to remove unwanted interfering characters from your code, leaving keywords for recognition.

```python
# -------------main--------------
# Regular expression
# The regular expression matches all the required values and returns a list
reg = r'\b[a-zA-Z]+\b'

# path = input("Please enter your code address: ")
level = int(input("Please input the level you want(1,2,3,4)"))

#Read the code
# with open(path, encoding='utf8') as f:
with open('key.c', encoding='utf8') as f:
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
```

### dictionary

Initialize all values to 0

```python
# Keyword dictionary
dict = {'auto':0, 'break':0, 'case':0, 'char':0, 'const':0, 'continue':0, 'default':0, 'do':0, 
'double':0, 'else':0, 'enum':0, 'extern':0, 'float':0, 'for':0, 'goto':0, 'if':0, 'int':0, 'long':0, 
'register':0, 'return':0, 'short':0, 'signed':0, 'sizeof':0, 'static':0, 'struct':0, 'switch':0, 
'typedef':0, 'union':0, 'unsigned':0, 'void':0, 'volatile':0, 'while':0}
```

### keyword number

After eliminating symbols with regular expressions, use dictionaries to count the keywords, and finally calculate the sum.

```python
# Count the number of keywords
def key_num():
    words = re.findall(reg, text)
    for word in words:
	    if word in dict:
		    dict[word]+=1
    print("total num: ", sum(dict.values()))
```

### switch_case number

Use two loops, the first one reads the number of lines of switch. The second one reads the code in sections according to the number of lines, and calculates the number of cases respectively

```python
# Count the number of switch and case
def switch_num():
    lineNum1=0
    # Record the number of lines where the switch resides.
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
```

### if else & if else_if else num

If is pushed on the stack, else is popped off the top element. And remove Spaces between else if to ensure that if in else if is not pushed as a new if.

```python
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
```

#### stack

```python
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
```

## Unit test

Use Coverage statistics unit test coverage, you need to install coverage

```
coverage run keyword.py arg1 arg2
coverage html
```

![image-20210923215820319](C:\Users\22478\AppData\Roaming\Typora\typora-user-images\image-20210923215820319.png)

## Performance test

Line_profiler is used for line-by-line analysis (which can be installed using PIP /conda), and the selected function is marked with a decorator (@profile).

```
kernprof -l -v
```

<img src="LIV-CODE\EE308-LAB2\blob\main\image\image-20210923221521447.png" alt="image-20210923221521447" style="zoom:80%;" />

<img src="C:\Users\22478\AppData\Roaming\Typora\typora-user-images\image-20210923221449312.png" alt="image-20210923221449312" style="zoom:80%;" />

<img src="C:\Users\22478\AppData\Roaming\Typora\typora-user-images\image-20210923221613866.png" alt="image-20210923221613866" style="zoom:80%;" />

## Summary

​		After finishing this assignment, I have a general understanding of the software development process and become more proficient in using tools like Git. I also learned some things I didn't know before, such as unit testing and performance testing. This gave me a taste of the wholeness of code development.

​		I hope I can learn more new knowledge and exercise my overall thinking ability in the following study.

## Appendix

<img src="C:\Users\22478\AppData\Roaming\Typora\typora-user-images\image-20210923222906071.png" alt="image-20210923222906071" style="zoom:80%;" />