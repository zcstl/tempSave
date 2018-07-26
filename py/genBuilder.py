#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import os.path
repoDir="/Users/zhangcs/zcsMac/studyProject/studying"

class Builder(object):
    def getBuildCMD(self):
        pass

class MavenBuilder(Builder):
    def getBuildCMD(self):
        return "mvn package"

class GradleBuilder(Builder):
    def getBuildCMD(self):
        return "gradle"

class AntBuilder(Builder):
    def getBuildCMD(self):
        return "ant"

class Gene:
    def genCMD(self):
        files = os.listdir(repoDir)
        print files
        if "pom.xml" in files:
            return buiders["maven"].getBuildCMD()
        elif "gradle.xml" in files:
            return buiders["gradle"].getBuildCMD()
        elif "ant.xml" in files:
            return buiders["ant"].getBuildCMD()

buiders = {
    "maven":MavenBuilder(),
    "gradle":GradleBuilder(),
    "ant":AntBuilder()
}

print Gene().genCMD()

# if __name__ == "__main__":
#     repoDir=sys.argv[1]
#     print Gene().genCMD()
