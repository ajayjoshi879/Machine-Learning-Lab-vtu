import csv
with open ("Training_examples.csv",'r') as f:
    jsk = csv.reader(f)
    jsk_list = list(jsk)


h = ['0','0','0','0','0','0']
for i in jsk_list:
    print(i)
    if i[-1] == 'Yes' :
        j=0
        for x in i:
            if x!='Yes':
                if(x!= h[j]and h[j] == '0'):
                    h[j] = x
                elif(x!= h[j] and h[j]!= '0'):
                    h[j] = '?'
            j = j+1        
print("most specific hypthesis is",h)
    