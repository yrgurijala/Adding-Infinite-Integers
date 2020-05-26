import sys


class Node:
    def __init__(self, value):
        self.Value = value
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.counter = 0

    def insertfront(self, value):
        newNode = Node(value)
        newNode.nextNode = self.head
        self.head = newNode
        self.counter = self.counter + 1

    def display(self, line, lastLine):
        refNode = self.head
        finalDisplay = ""
        check = 0

        while check < len(line)-1:
            finalDisplay = finalDisplay + line[check]
            check = check + 1

        finalDisplay = finalDisplay + "="

        if self.counter < 40:
            while refNode:
                finalDisplay = str(finalDisplay) + str(refNode.Value)
                refNode = refNode.nextNode
        else:
            finalDisplay = str(finalDisplay) + "error"

        print(finalDisplay)

    def deletehead(self):
        if self.head is None:
            return
        refNode = self.head
        self.head = refNode.nextNode
        self.counter = self.counter-1

    def clearList(self):
        self.head = None
        self.counter = 0

    def isnotempty(self):
        if self.head is None:
            return False
        return True


# The Following code takes input from a txt file
#argument = sys.argv[1]
#filename = ""
#lengthOfFile = len(argument)
#i1 = 6

#while i1 < lengthOfFile:
    #filename = filename+argument[i1]
    #i1 = i1 + 1

filename = "tc6.txt"
inputFile = open(filename, "r")

aList = LinkedList()
bList = LinkedList()
addList = LinkedList()

for line in inputFile:
    i = 0;

    if (line[i] is '='):
        print(line,end="")
        continue

    length = len(line)

    while i < length:
        if line[i] is '(':
            i = i + 1
            while line[i] is not ',':
                aList.insertfront(line[i])
                i = i + 1
            i = i + 1
            while line[i] is not ')':
                bList.insertfront(line[i])
                i = i + 1
        i = i + 1

    remainder = None

    while aList.isnotempty() or bList.isnotempty():
        if aList.isnotempty() is False:
            a = 0
            b = bList.head.Value
        elif bList.isnotempty() is False:
            b = 0
            a = aList.head.Value
        else:
            a = aList.head.Value
            b = bList.head.Value

        addition = str(int(a) + int(b))

        if remainder is not None:
            addition = str(int(a) + int(b) + remainder)
            remainder = None

        if len(addition) is 2:
            addList.insertfront(addition[1])
            remainder = int(addition[0])
        else:
            addList.insertfront(addition)
            remainder = None

        aList.deletehead()
        bList.deletehead()

    if remainder is not None:
        addList.insertfront(remainder)
        remainder = None

    addList.display(line)
    addList.clearList()
