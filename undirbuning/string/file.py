file = input("Enter in a file name (or 'q' for quit): ")
while file != "q":
  if ".py" in file:
    print("This is a Python file")
  
  elif ".cpp" in file:
    print("This is a C++ file")
  
  elif ".js" in file:
    print("This is a Javascript file")
  
  elif ".java" in file:
    print("This is a Java file")
  
  else:
    print("Unknown extension")

  file = input("Enter in a file name (or 'q' for quit): ")

#tjeka which file type er þetta með "if" setningar og "IN" 
