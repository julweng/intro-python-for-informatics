# -*- coding: utf-8 -*-
# Assignment 5: Message Frequency Count
# Julia Tzu-Ya Weng U07487022

# This program reads through the mail box data and extract email addresses from
# lines that start with "From". Then, the person with the highest number of 
# messages is printed

# open file
filename = raw_input("Enter the file name: ")

try:
    fh = open(filename)

except:
    print "Error opening file %s" %filename
    raise SystemExit("Exiting program...") 

# starts an empty list to store extracted addresses
email_lst = list()
count = dict()

# loop through each line in the file
for line in fh:
    
    # skip line that doesn't start with From or From:
    if not (line.startswith("From") or line.startswith("From:")): 
        continue
    
    # split the words
    words = line.split()
    
    # fill the email_list
    email_lst.append(words[1])
    
    # fill in the count dictionary
    for email in email_lst:
      count[email] = count.get(email, 0) + 1
    
# create a list of tuples with number, email
count_email = list()
for email, number in count.items():
    count_email.append((number, email))

# sort by count
count_email.sort(reverse = True)

# print the email address with the highest number messages
print "%d emails from %s" %(count_email[0][0], count_email[0][1]) 

fh.close()       
