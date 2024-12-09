# name = "jai"
# n = 'jai'
# m = """jai"""           ## multiline code ya paragraph 

# rupees = 2000

# print("I have",rupees,"rupees")

## string methods/functions 
# name = "upflairs"

# print(name.upper())  # converts all characters to uppercase
# print(name.lower())
# print(name.capitalize())
# print(name.swapcase())


# print(name.strip())
# print(name.rstrip())
# print(name.lstrip())


# s = "hello world hhhhh"
# print(s.title())

# print(s.replace("hello","bye"))

# print(s.find("world"))   ##-1 
# print(s.count("h"))

# print(s.split("-"))

# s = "-"
# print(s.join("hello"))

# s = "hello world"
# print(s.startswith("world"))
# print(s.endswith("world"))

# s = "ghjk"
# print(s.isdigit())
# print(s.isalpha())
# print(s.isnumeric())
# print(s.isalnum())


# s = "45"
# print(s.zfill(5))

# s = "hello"
# w = " world"
# t = s+w
# print(t)

# age = 10 
# # text = "my age is" + age
# ##formAtted string/ f-string
# text = f"my age is {age}" 
# print(text)

# name = "jai"
# age = 10
# print("Name : {}, Age : {}".format(name,age))

# indexing(numering)
# h e l l o 
# 0 1 2 3 4

# name = "hello"
# print(len(name))

# n = 123
# # print(type("dfghj"))
# #type casting 
# m = str(n)
# print(type(m))

# s = "HELLO"
# print(s.casefold())

# s = "  "
# print(s.isspace())

# s = "Hello World"
# print(s.istitle())

# print("hello".find("u"))

# print("helloe".rfind("u"))                  ##highest indexx 


# print("upflairs".index("l"))
# print("upfllairs".rindex("l"))

# print("hello\nworld".splitlines())

# print("hello".ljust(100," "))                              ##adjustment 
# print("hello".rjust(100,"k"))                               ##adjustment 
# print("hello".center(100,"k"))                               ##adjustment 


# print("hello".encode('utf-8'))  

# print(b'hello'.decode('utf-8'))  

# text = "apple,banana,cherry"
# text = "apple"
# result = text.partition(",")
# print(result)  

# The part before the first occurrence of the separator.
# The separator itself.
# The part after the first occurrence of the separator.

# "hello".

# text = "example.py"
# # result = text.removesuffix(".py")
# result = text.removeprefix("example")
# print(result)  # 'example'


# s = "hello\tworld"
# print(s.expandtabs())


#maketrans -- 
# Creating a translation table
# table = str.maketrans("aeiou", "12345")

# # Applying the translation to a string
# text = "hello world"
# translated_text = text.translate(table)
# print(translated_text)  # h2ll4 w4rld
