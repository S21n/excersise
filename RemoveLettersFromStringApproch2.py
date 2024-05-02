def Remove(s,i):
    if i==0:
        # return s[1:]
        
        
        
         return s[0] + Remove(s[1:], i - 1)
 
 
# Test the function
test_str = "GeeksForGeeks"
new_str = Remove(test_str, 2)
print("The string after removal of ith character:", new_str)