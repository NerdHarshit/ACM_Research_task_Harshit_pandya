#task1 
phone_replacement = "[REDACTED]"

python_replacement = "🐍"#python
java_replacement = "☕"#java

months = {
     '01':"january",
     '02':"february",
     '03' :"march",
     '04':"april",
     '05':"may",
     '06':"june",
     '07':"july",
     '08':"august",
     '09':"september",
     '10':"october",
     '11':"november",
     '12' : "december"
}

def transform_text(inputStr):
    inputStr = inputStr.replace('.',"")
    '''
    as of now getting rid of . from sentences as they cause errors or
    just put space before and after a '.' and remove line 23
    '''
    newStr =""
    words = inputStr.split(' ')

    for i in words:
        #handeling the python word
        if i.lower() == "python":
            i = python_replacement
        
        #handeling java word
        elif i.lower() == "java":
            i = java_replacement
        
        #handeling phone nums assuming phone number has 1 hyphen in it as given in example
        elif i.count('-') ==1:
            temp = i[:i.index('-')] + i[i.index('-')+1:]
            if(temp.isnumeric() and len(temp) == 10):
                i = phone_replacement
        
 
        #assuming input format is 2025-08-23 yyyy-mm-day mm in numeric form as given in example
        #and output format is day monthInWords yyyy as given in example
        elif i.count('-') == 2:
            tempL = i.split('-')
            tempS = i.replace('-','')
            if(tempS.isnumeric()):
                newtemp = tempL[2] +" "+  (months[tempL[1]] if (int(tempL[1]) in range(1,13)) else "MonthOutOfBounds" )+" " + tempL[0]
                i = newtemp
            
        #forming new string
        newStr = newStr + i +" "


    return(newStr)
#end of function
example_str = "Call me at 98123-45678 on 2025-08-23. I love Python more than Java."
print(transform_text(example_str))
#output => Call me at [REDACTED] on 23 august 2025 I love 🐍 more than ☕