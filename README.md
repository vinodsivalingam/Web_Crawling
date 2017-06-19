# Web_Crawling

Crawler module performs the below tasks:
The beautifulsoup module  get the underlying contents of html.
The parent directory contains the list of list of the users. 
The list of users details has been collected.
Using the list of names, URL is generated for the corresponding user and program crawls over all the generated URL
All the user have subfolder which has details of the emails
The module crawls over to the list of email page and collects the details of all the email ( The module can still be scaled up to read all the contents of the email and store it).
 The email details of the individual user is being grouped together and a file is created for each user which holds the email details of the respective person
The module returns a file with list of files created(a file per user) 
