##string - a sequence of characters
##string is immutable(unchangeable )
##string is ordered
##string is indexed

##how string is denoted?
##single quotes, double quotes, triple quotes

# name = "hello345678@@#$%"
# print(name)

# name1 = 'hello jdbjfbjks'
# print(name1)

# name2 = """hello                      
# ;daalksdklsadaks
# lkasdkkd
# askdkn"""                           ## triple quotes are used to create multiline string
# print(name2)

#indexing 
# U P F L A I R S
# 0 1 2 3 4 5 6 7  -- positive index 
# -8 -7 -6 -5 -4 -3 -2 -1 -- negative index 
# print(name.upper())
# print(name.lower())
# print(name.swapcase())
# print(name.title())
# print(name.capitalize())
# print(name.casefold())
# print(name.count("a"))
# print(name.find("pvt"))
# print(name.index("pvt"))
# print(name.isalnum())   # aplha numeric
# print(name.isalpha())   # alphabetic
# print(name.isascii())   #
# name = "1234"
# print(name.isdigit())   # numeric
# print(name.isdecimal())   # numeric
# print(name.islower())  #checks whether all the characters in the string are lowercase or not
# print(name.isnumeric()) #
# print(name.isprintable()) # checks whether all the characters in the string are printable or not
# print(name.isspace()) # checks whether all the characters in the string are whitespace or not
# print(name.istitle())
# print(name.isupper())
# name = "hello world"
# print(name.strip())  ## whitespace removal
# print(name.lstrip())
# print(name.rstrip())

# print(name.replace("hello","hi"))
# print(name.split("@"))
# print(name.partition("@"))
# print(name.rpartition("@"))
# print(name.center(50,"*"))
# print(name.ljust(50,"*"))
# print(name.rjust(50,"*"))
# name = "hello"
# name1 = "world"
# print(name + name1)
# print(name.encode())
# print(name.encode("utf-8"))
# print(name.encode("ascii"))
# print(name.endswith("h"))
# print(name.startswith("o"))

# print(name.zfill(50))
# print(name.join(["a"]))

# age = 10 
# text = "my age is" + age 
##formatted string //f-string -- 
# text = f"my age is {age}"
# print(text)


##type casting -- conversion of one data type to another

# a = float(10) 
# print(a)
# print(type(a))