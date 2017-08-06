import difflib
import sys,os

##we need 2 file name to be compareds
if len(sys.argv) != 3:
    print "please provide 2 file name to be compared!"
    sys.exit()

file1=sys.argv[1]
file2=sys.argv[2]

if not os.path.isfile(file1):
    print "Invalid file "+file1
    sys.exit()

if not os.path.isfile(file2):
    print "Invalid file "+file2
    sys.exit()

print "Start to compare file "+file1+" and "+file2

def readfile(filename):
    try:
        filehandle = open(filename,'rb')
        text = filehandle.read().splitlines()
        filehandle.close()
        return text

    except IOError as error:
        print "read file error"+str(error)
        sys.exit()

text1 = readfile(file1)
text2 = readfile(file2)

htmldiff = difflib.HtmlDiff()
print htmldiff.make_file(text1,text2)

