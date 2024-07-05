class Stack:
    def __init__(self):
        self.list = []
       
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
   
    def push(self,value):
        self.list.append(value)
        return "Element pushed"
       
    def show(self):
        if self.isEmpty():
            return "No Element"
        else:
            print(self.list)
           
    def peek(self):
        if self.isEmpty():
            return "No Element"
        else:
            return self.list[len(self.list)-1]
           
    def pop(self):
        if self.isEmpty():
            return "No Element"
        else:
            return (self.list.pop())
           
    def delete(self):
        self.list = None
       
    def stackMenu(self):
        while True:
            print("1. Is Empty")
            print("2. Push Element ")
            print("3. Peek Operation ")
            print("4. Pop Element ")
            print("5. Delete ")
            print("6. Exit ")
            print("7. Display all stack element")
            self.ch = int(input("Enter choice: "))
            if self.ch ==1:
                print(self.isEmpty())
            if self.ch ==2:
                self.value = int(input("Push Element in Stack: "))
                print(self.push(self.value))
            if self.ch ==3:
                print(self.peek())
            if self.ch ==4:
                print(self.pop())
            if self.ch ==5:
                print(self.delete())
            if self.ch ==6:
                print(sys.exit())
            if self.ch ==7:
                self.show()
               
print("1. Create Stack")
ch = int(input("Enter Choice: "))
if ch==1:
    if __name__=='__main__':
        obj = Stack()
        print("Stack created Successfully")
        print()
        obj.stackMenu()
        print("Thank You")