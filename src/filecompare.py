import filecmp
import sys

filecmp.cmp("/projects/python/vepython/lib/python2.7/os.py", "/projects/python/vepython/lib/python2.7/re.py")
print 'next'
filecmp.dircmp("/projects/python/vepython/lib", "/projects/python/vepython/lib")

sys.exit()
