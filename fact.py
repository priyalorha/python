/*
For this challenge you will be determining the factorial for a given number.
*/


def FirstFactorial(num): 
    if(num==1 or num==0):
        return 1
    else:
        return num*FirstFactorial(num-1)
        
    
    return num
    
# keep this function call here  
print FirstFactorial(raw_input())