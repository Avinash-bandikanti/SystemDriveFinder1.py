import os
import time
class FileFinder:
    def __init__(self):
        pass
    def find_file(self,filename,filepath):
        files=[]
        self.filename=filename
        self.filepath=filepath
        for root,dir,file in os.walk(filepath):
            if filename in file:
                files.append(os.path.join(root,filename))
            return files
if __name__=='__main__':
    #st=time.time()
    obj=FileFinder()
    print(obj.find_file('avi.txt','C:/hcl1'))
    """st1=time.time()
    print(obj.find_file('SearchFile.py','C:'))
    et1=time.time()
    et=time.time()
    print(et-st)
    print(et1-st1)
"""
