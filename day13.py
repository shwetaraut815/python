## strings are immutable  ---it wont change existing string but it create new string after string method

## strings operation
## upper()

a = "hgFGeHHf"
print (a.upper())

## lower()
print (a.lower())

### strip()   --print string as it is 
str = "kfc"
print (str.strip())

## rstrip()  -- remove trailing characters  --means only last character not front

x = "!!!helooo!!!!##"
print (x.rstrip("!,#"))

## replace()
print (x.replace("elo", "iillo"))

## split() ---split the string as a list items 
spl = "fgff@sy u@bs jh@hu ffffyw"
print (spl.split("@"))
print (spl.split(" "))

## capitalize()  --convert 1st character into uppercase and remaining  in lowercase
K = "helLO GyaTri"
capK = K.capitalize()
print (capK)  ## or
print (K.capitalize())

## center()  ---allign string in centre
z = "welcome"
print (z.center(50))

# count()  --- count the letter or word in string
print (spl.count("ff"))

##endswith()  --it checks is this string end with given values or not --- and act as a boolean oprt returns value in true or false
print (spl.endswith("yw"))

str1 = "kiara want some mangoes"
print (str1.endswith("want", 3, 15))   #.endswith("want") checks if "ra want some" ends with "want".

#"ra want some" ends with "some", not "want".
print (str1.endswith("ome", 3, 15)) 

## find() --- searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

## index() --- searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

## isalnum() --- returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

## isalnum() --- returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

##  islower() --- returns True if all the characters in the string are lower case, else it returns False.

## isprintable() --- returns True if all the values within the given string are printable, if not, then return False.  eg. /n is not printable

## isspace() --- returns True only and only if the string contains white spaces, else returns False.

## istitile() --- returns True only if the first letter of each word of the string is capitalized, else it returns False.

## startswith() --- checks if the string starts with a given value. If yes then return True, else return False.

## swapcase() --- changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

## title() --- capitalizes each letter of the word within the string.