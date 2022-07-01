# try  to find  whether  the alphabet  is presennt  in given string or not

string = "python is easy to learn"

char = input ("Enter character  to check:")

if char in string:
    print(char,"is present in",string)
else:
    print(char,"is not present in",string)