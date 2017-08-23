import urllib

def read_text():
    quotes = open("C:\Users\Sangram\Documents\workspace\udacity\FullStack\python\movie_quotes.txt")
    text = quotes.read()
    quotes.close()
    output = check_profianity(text)
    if "true" in output:
        print ("Profanity found")
    elif "false" in output:
        print ("Document is rated G")
    else:
       print("Error")    
	

def check_profianity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    connection.close()
    return output

read_text()
