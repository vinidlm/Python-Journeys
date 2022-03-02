palavra = input("")  
aux = '' 
i = 0 
while i < len(palavra):     
    if i + 1 < len(palavra):         
        if palavra[i] == palavra[i+1]:             
            aux += palavra[i].upper()             
            i += 2         
        else:             
            aux += palavra[i]            
            i += 1     
    else:         
        aux += palavra[i]
        break
print(aux.lstrip())