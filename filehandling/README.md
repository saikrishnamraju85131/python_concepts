File handling in python:
       It means creating,removing files using python,reading and writing contnet from files using python.

f=open("file name","mode of the file")

when we use open() method with two arguments passing i.e file name,mode of the file

It asks the os to open or create a file and, os returns file descriptor(an integer id for an opened file)

Now,open() method returns an instance of a class(TextIOwrapper) which holds the state of the opened file like file descriptor,

cursor position,buffering etc and provides methods to read or write content in files or get the current state of file etc.

here,
file descriptor -> is an integer id which os uses to track open resource(file),so whenever python object  need to write or read some content,it uses the integer id,so the os knows what python object is talking about.

buffering->python object holds content in memory  instead of asking or requesting os to get the content from file every time.
E.g if we want to read first two lines in a file,but python object sends request to get whole file contnet and store it in memory,next time if we want other two lines there is no need to send request for os.

Mode:specifies weather we want to create a file,read content from file,writing content in file.

"r"->read->uses to read content from file,it raises error if file not present.

"w"->write->uses to write contnet from file,if file does not present,it creates new one

"a"->append->uses to append content at the end of file with out overriding the existing content in file,it creates new file if file does not present.

"x"->create->uses to create a new file,if file already exists it raises error.