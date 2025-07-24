num = input()
colors = list(input())
ans = 0
for i in range(len(colors)-1):
        	if colors[i] == "R" and colors[i+1] == "R":
        		ans +=1          
        	
for i in range(len(colors)-1):
        	if colors[i] == "G" and colors[i+1] == "G":
        		ans +=1    
        	
for i in range(len(colors)-1):
        	if colors[i] == "B" and colors[i+1] == "B":
        		ans +=1           
print(ans)