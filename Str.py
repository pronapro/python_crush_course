#indexing strings
name = "my name is my name"
n= name[1]
#starting from the end
las = name[-1]
#at anypoint
any = name[4]
print(n)
print(las)
print(any)


#slicing
A=name[1:]
B=name[2:5]
C =name[2:4:2]
print(B)
#printing reverse
name[::-1]
#methods
#count
name.count("e")
name.count("e",3,6)
#find
#used to find the index of a string
name.find("is")

#lowercase
name.lower()
name.upper()
#others capitalize,title

#split methods
#takes in a delimenter and number
num = "256-78-782-678"
num.split("-")
num.split("-",1)
#join,uses a sequence. a list or tuple
word1 = ["hello", "world"]
" ".join(word1)
