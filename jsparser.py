import re
def read(path):
    f = open(path, "r")
    string  = f.read()
    f.close()
    return string 

text =  read("input.txt")




            

def lexxer(string):
    banned = [ '(', ')', '[', ']', '{','}', '=', '!', '&','*','-','+', ';', ":", "|", "?", ",", "<", ">",
              "/", ".", "'", '"']
    result = []
    temp = ''
    for i,currentChar in enumerate(string):
        if currentChar!=" ":
            temp += currentChar
        else:
            result.append(" ")
        if(i<len(string)-1):
            nextChar = string[i+1]
            if temp != "" and (nextChar == " "or nextChar == "\n" or nextChar in banned or (temp in banned)) or currentChar =='\n':
                result.append(temp)
                temp = ''
        if i==len(string)-1 and temp != " ":
            result.append(temp)
    return result


def removecomment(lex):
    reject = False
    tobeDiscarded = []
    comment = False
    result = ""
    for i, currentChar in enumerate(lex):
        if(i==0):
            if currentChar == "'" or currentChar == '"':
                reject = True
                ban = currentChar
                double = False
            result+= currentChar
            continue
        else:
            prec = lex[i-1]
            
            
        if reject:
            if not comment:
                result += currentChar
            if double:
                if currentChar == ban[1] and lex[i-1] == ban[0]:
                    reject = False
                    comment = False
            else:
                if currentChar == ban:
                    reject = False
                    comment = False
            continue
        
        if currentChar == "*" and prec == '/':
            reject = True
            double = True
            ban =  currentChar + prec
            start = i
            comment = True
            result = result[:-1]
            continue
        elif currentChar == "'" or currentChar == '"':
            reject = True
            ban = currentChar
            double = False
            
        elif currentChar == "/" and prec == "/":
            reject = True
            ban = '\n'
            double = False
            start = i
            comment = True
            result = result[:-1]
            continue
        result += currentChar
    return result
