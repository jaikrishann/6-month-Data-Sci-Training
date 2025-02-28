# print("hello world")          -- comment 
# #data types -- 1 primitive - int, float, str, bool, complex
# #             2 non-primitive - list, tuple, set, dict

# #string -- collection of characters
# #string is immutable(unchangeable) -- basic changes -- insert , add , delete , update


# string denoted by single, double, triple quotes -- '',"",'''''',""""""""
#str is immutable(unchangeable) -- basic changes -- insert , add , delete , update

# a = 'hello'
# b = "hello"
# c = '''hello'''                                  #PARAGRAPH ya multiple lines

# rupees = 2000
# print("I have",rupees,"rupees")


#to join/ add two strings 
# a = "hello "
# b = "world"
# c = a + b
# print(c)



name = "uPSflairS companyS"
# ##methods of string
# print(name.upper()) #convert string into uppercase 
# print(name.lower()) #upflairs
# print(name.capitalize()) #Upflairs
# print(name.title()) #Upflairs
# print(name.swapcase()) #UpFLAIRS COMPANY
# print(name.casefold()) #upflairs company
# print(name.count('a')) #2
# print(name.index('S')) #2
# print(name.find('S')) 
# print(name.startswith('u')) #True
# print(name.endswith('y')) #True
# print(name.replace('company','pvt ltd')) #upflairs pvt ltd
# print(name.split()) #['upflairs', 'company']
# print(name.split('a')) #['uPSfl', 'irs comp', 'ny']
# print(name.strip()) #remove spaces from start and end
# print(name.lstrip()) #remove spaces from start
# print(name.rstrip()) #remove spaces from end
# print(name.center(30)) #center the string
# print(name.ljust(40)) #left justify the string
# print(name.rjust(40)) #right justify the string
# print(name.zfill(40)) #fill zeros at start
# print(name.isprintable())
# print(name.isalnum())
# print(name.isalpha())
# print(name.isdigit())
# print(name.islower())
# print(name.isupper())
# print(name.isspace())
# print(name.istitle())
# print(name.isnumeric())
# # print(name.isidentifier())
# print(name.isdecimal())
# print(name.isascii())
# print(name.encode("utf-8"))
# print(name.encode("ascii"))
# print(name.join("hello")) 
# print(name.partition("c"))
# print(name.removeprefix("u"))
# print(name.removesuffix("y"))













# u p f l a i r s
# 0 1 2 3 4 5 6 7 -- index
# -8-7-6-5-4-3-2-1 -- reverse index



name = " upflairs "
# print(name[5])
# print(name[2])
# print(name[-3])
# print(name[-1])

# print(name[1:4])                           #slicing -- [start:stop:step]
# print(name[-6:])





## formated string// f-string 
# age = 10 
# # text = "my age is" + age 
# text = f"my age is {age}"
# print(text)