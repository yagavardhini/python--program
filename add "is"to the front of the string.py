def fun(str)
 if len(str)>=2 and str[0:2]=="is":
  return str
 else:
  return "is"+str
print(fun("land"))
print(fun("island"))
  
