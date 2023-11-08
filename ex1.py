with open('data.txt') as f:
    lines = f.readlines()
    
sum = 0
    
for line in lines:
    line = line.strip()
        
    if line.lstrip('-').isdigit(): 
        sum+= int(line)
            
print(sum)