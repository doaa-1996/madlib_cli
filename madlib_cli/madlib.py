import re
def read_template(root):
    """
    This is the read function ,It takes a root and read the file in that root
    """
    try:
      with open (root , "r") as file:
        filecontent=file.read().strip()
        return filecontent

    except FileNotFoundError:
        raise FileNotFoundError('The file not found')    
      
    except Exception as a :
        return (f"Error {a}")

def parse_template (text):
    
    """
   This is the parse function ,It takes a text and parses it into usable parts.
    """
    index=0
    origin_value=re.findall(r"\{(.*?)\}", text)  

    for i in origin_value:
        text= text.replace(origin_value[index], "",1)
        index+=1
    return text, tuple(origin_value)






def merge(text,origin_value):
    updatedText= text.format(*origin_value)
    print(updatedText)

    with open('assests/make_me_a_video_game_output.txt','w') as output:
        output.write(updatedText)

    return updatedText    
  



   
def result( text,origin_value):
    arr=[]

    for i in origin_value:
        arr.append(input(f"enter an { i} ")) 
    return merge(text,arr)   



if __name__ == "__main__":

 print("""
 Welcome to Madlib,You should enter a set of words to fill the blanks,Lets start playing
""")
 reading_template=read_template('assests/make_me_a_video_game_template.txt')
 parse_template (reading_template)
 text,origin_value=parse_template (reading_template)
 result( text, origin_value)  


 

