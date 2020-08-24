#From python 3 we need to use html.parser instead of HTMLParser
from html.parser import HTMLParser
#For regular expression
import re

class MyHTMLParser(HTMLParser):
    #Here 'attribute' is a list that holds tuples
    def handle_starttag(self, tag, attribute):
        print("Start : {}".format(tag))
        #If the 'attribute' list is empty then it will not print the attribute name and its value.
        if len(attribute) == 0:
            pass
        else:
            #Print the name of the attribute and its value
            for i in range(len(attribute)):
                #Here 'attribute' list holds tuples. Each of them always hold two elements. 'i' for the index of the list and '0' and '1' for the index of the tuple
                print("-> {} > {}".format(attribute[i][0], attribute[i][1]))
    def handle_endtag(self, tag):
        print("End   : {}".format(tag))
    def handle_startendtag(self, tag, attribute):
        print("Empty : {}".format(tag))
        if len(attribute) == 0:
            pass
        else:
            for i in range(len(attribute)):
                print("-> {} > {}".format(attribute[i][0], attribute[i][1]))
    
#Defining the variable
HTML_code = ''
#Taking input and putting them all in a variable
for _ in range(int(input())):
    HTML_code += input()
#Discarding the comments
without_comment = re.sub(r"(?:<!--(.|\s)*?(?:-->))","", HTML_code)
#The HTMLParser class is instantiated without arguments.
parser = MyHTMLParser()
#An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered. The user should subclass HTMLParser and override its methods to implement the desired behavior.
parser.feed(without_comment)
