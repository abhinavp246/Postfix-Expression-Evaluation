
# coding: utf-8

# In[37]:

'''Abhinav R. Pandey
   Project 1 (Part 1)
   eval_postfix.py 
'''

class Empty(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)

class ArrayStack:
    '''LIFO Stack implementation using a Python list as underlying storage. Code retrieved from Data Structures and Algorithms 
       in Python, pg. 232.
    '''

    def __init__(self):
        # Create an empty stack.
        self._data = []  # nonpublic list instance

    def __len__(self):
        # Return the number of elements in the stack.
        return len(self._data)

    def is_empty(self):
        # Return True if the stack is empty.
        return len(self._data) == 0

    def push(self, e):
        # Add element e to the top of the stack.
        self._data.append(e)  # new item stored at end of list

    def top(self):
        # Return (but do not remove) the element at the top of the stack.
        # Raise Empty exception if the stack is empty.
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]  # the last item in the list

    def pop(self):
        # Remove and return the element from the top of the stack (i.e., LIFO).
        # Raise Empty exception if the stack is empty.
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()  # remove last item from list
    
def eval_postfix(expr):
    ''' Function that accepts an input string with postfix expression, and returns a value of evaluating the postfix expression. 
    '''
    operator_check = ["+","-","/","*"] #List of operators (strings), for comparison with the input string. 
    myStack = ArrayStack() #Create an empty stack. 
    
    char_list = expr.split() #Convert the input expression into a list of strings. 

    for char in char_list:
        if char.isdigit(): #If the character is a number, convert it to an integer and add it to the top of the stack. 
            myStack.push(int(char))
            
        elif char in operator_check: #If the character is an operator, take the first 2 elements from the top of the stack, and evaluate them using the given operator. 
            
            element2 = myStack.pop()  
            element1 = myStack.pop()  
            operator = char

            if operator == "+":
                new_operand = element1 + element2
            elif operator == "-":
                new_operand = element1 - element2
            elif operator == "*":
                new_operand = element1 * element2
            elif operator == "/":
                new_operand = element1 / element2
                
            myStack.push(new_operand)      # Replace the elements with the evaluated value, and contine forward with the input string. 
            
        else:
            raise Exception('Invalid postfix expression')

    return myStack.pop()


if __name__ == "__main__":
    
    test1 = "5 2 + 8 3 - * 5 /"
    test2 = "3 2 * 12 8 + * 51 /"
    test3 = "7 2 *"
    test4 = "60 3 /"
    test5 = "10000000 1000000 /"
    
    print (eval_postfix(test1))
    print (eval_postfix(test2))
    print (eval_postfix(test3))
    print (eval_postfix(test4))
    print (eval_postfix(test5))
    


# In[ ]:




# In[ ]:



