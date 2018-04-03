# Assignment 6: URL Reader
# Julia Tzu-Ya Weng U07487022

# program description: this program prompts user for URL and uses urllib to 
# retrieve content from the webpage. The program prints the first 3000 
# characters read and the total number of characters read

# use urllib library for retrieving data from a web page 
import urllib

# prompt user for url
url = raw_input("Enter URL: ") 

try:
    # open webpage 
    webpage = urllib.urlopen(url)
    
    # count_ch to count character in web content
    count_ch = 0
    
    # read content
    web_content = webpage.read()

    for ch in web_content:
        # count characters
        count_ch += 1
        
    # print 3000 characters
    print web_content[:3000]
    
    # print total number of characters read
    print '\nTotal number of characters read: ', count_ch

# if error occurrs, exist
except:
    print ("Error opening %s" %url)
    raise SystemExit("Exiting program...")
