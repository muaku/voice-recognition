test="私のidにしてください"
val = "".join(filter(str.isdigit, test))
print ("val: {}".format(val))
if(val != ""):
    number = int(val)
    print (number)