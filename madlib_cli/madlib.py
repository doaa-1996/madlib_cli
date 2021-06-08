import re
files=" "
arr=[]
def read_template():
    try:
        with open('assests/template.txt') as file:
            files=file.read()
           
            parse_template(files) 
    except FileNotFoundError:
            print('the path is invalid') 
def parse_template(files):
    
    regex1= re.sub('\(.+?\)','',files)
    reg=re.findall('{(.+?)}',regex1)
    
   
    input_fun(reg ,files)
def input_fun(reg ,files):
    for w in range(len(reg)):
        inp=input('please insert  '+ reg[w] + ' ')
        arr.append(inp)
       
    merge(reg ,files)
def merge(reg ,files):
    
    for i in range(len(arr)):
        files = files.replace( "{" + reg[i] + "}" , arr[i] )
    print (files)
read_template()