def findthegreatestcommonfactor(firstnumb, secondnumb):
  
    if firstnumb == 0:
      
        return firstnumb
      
    while secondnumb != 0:
      
        if firstnumb > secondnumb:
          
            firstnumb = firstnumb - secondnumb
          
        else:
          
            secondnumb = secondnumb - firstnumb
          
    return firstnumb

class greatestcommonfactor:
  
  def __init__(value,numb1,numb2):
    
    value.numb1 = numb1
    
    value.numb2 = numb2
    
  def __class__(value):
    
    if numb1 == 0:
      
      value.numb1 = numb1
      
    if numb1 > numb2:
      
      value.numb1 = numb1 - numb2
      
    if numb2 > numb1:
      
      value.numb2 = numb2 - numb1
      
    return numb1
           
def greatestcommonfactor():
  
    a = int(input("Enter the first number: "))
  
    b = int(input("Enter the second number: ")) 
  
    greatestcommonfactor = findthegreatestcommonfactor(a, b)
  
    print("The greatest common factor of {0} and {1} is: {2}".format(a, b, greatestcommonfactor))
  
    print()