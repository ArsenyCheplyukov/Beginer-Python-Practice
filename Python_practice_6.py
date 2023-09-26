def subgenerator():
    yield 'World'

def generator():
    yield 'Hello'
    yield from subgenerator() #Запрашиваем значение из субгенератора
    yield '!'

for i in generator():
    print(i, end = ' ')

def nextSquare(): 
    i = 1; 
# An Infinite loop to generate squares  
    while True: 
        yield i*i                 
        i += 1  # Next execution resumes  
# from this point      

# Driver code to test above generator  
# function 
for num in nextSquare(): 
    if num > 100: 
        break    
    print(num) 