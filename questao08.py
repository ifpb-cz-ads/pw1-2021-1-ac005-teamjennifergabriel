def find(string, list):
    
    for item in list:
        if item == string:
            return True
            
        

r = find('v', ['b','a','c'])

print(r)