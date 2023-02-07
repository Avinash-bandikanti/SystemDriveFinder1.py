import pytest
from level1.SearchFile import FileFinder
from level1.SystemDriveFinder import SystemDriveFinder

class Test_Drive:
    def test_DriveCase(self):
        obj=SystemDriveFinder()
        self.excepted=obj.find_drives()
        self.actual=['C']
        assert self.excepted==self.actual
    def test_searchfile(self):
        obj=FileFinder()
        d=obj.find_file('avi.txt','C:/hcl1')
        act=['C:/hcl1\\avi.txt']
        self.excepted_filename=act
        self.actual_res=d
        #self.excepted_filename=d[0]
        #self.actual_res='C:/hcl1\\avi.txt'
        assert self.excepted_filename==self.actual_res