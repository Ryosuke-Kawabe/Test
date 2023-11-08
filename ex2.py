

with open('catalog.json') as f:
    lines = f.readlines()
    
jacket = 0
    
for line in lines:
    line = line.strip()
        
    if line.lstrip('-').isdigit(): 
        sum+= int(line)
            
print(sum)