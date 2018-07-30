#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urlparse
import os
import os.path
repoDir="/Users/zhangcs/zcsMac/studyProject/studying"

"""
1.gradle  若配置了代理则使用
2.gradle ant自动识别出jar/war包目录

maven local:
USER_HOME/.m2/repository
"""


gradleInitContent="allprojects {\n\
    repositories {\n\
        mavenCentral()\n\
        jcenter {\n\
            url \"http://jcenter.bintray.com\"\n\
        }\n\
        mavenLocal()\n\
   }\n\
}\n\
"

gradleInitDir="/tmp/.gradle"

class Builder(object):
    def prepareEnvironment(self):
        return self
    def getBuildCMD(self):
        pass

class MavenBuilder(Builder):
    def getBuildCMD(self):
        return "mvn package\ncp target/*.jar ."

class GradleBuilder(Builder):
    def prepareEnvironment(self):
        if not os.path.exists(gradleInitDir):
            os.makedirs(gradleInitDir, 0750)

        #http全局仓库配置
        with open(gradleInitDir + "/init.gradle", "w", 0644) as fd:
            fd.write(gradleInitContent)


        #代理配置
        httpProxy = os.environ.get("http_proxy")
        httpsProxy = os.environ.get("https_proxy")
        if httpProxy != None:
            proxyInfo=urlparse.urlsplit(httpProxy)
            with open(gradleInitDir + "/gradle.properties", "a+", 0640) as fd:
                fd.write("systemProp.http.proxyHost=" + proxyInfo.hostname)
                fd.write("systemProp.http.proxyPort=" + proxyInfo.port)
                fd.write("systemProp.http.proxyUser=" + proxyInfo.username)
                fd.write("systemProp.http.proxyPassword=" + proxyInfo.password)
                fd.write("systemProp.http.nonProxyHosts=")
        if httpsProxy != None:
            proxyInfo=urlparse.urlsplit(httpsProxy)
            with open(gradleInitDir + "/gradle.properties", "a+", 0640) as fd:
                fd.write("systemProp.https.proxyHost=" + proxyInfo.hostname)
                fd.write("systemProp.https.proxyPort=" + proxyInfo.port)
                fd.write("systemProp.https.proxyUser=" + proxyInfo.username)
                fd.write("systemProp.https.proxyPassword=" + proxyInfo.password)
                fd.write("systemProp.https.nonProxyHosts=")
        #jar/war拷贝

        return self

    def getBuildCMD(self):
        return "gradle build\ncp build/libs/* ."

class AntBuilder(Builder):
    def getBuildCMD(self):
        return "ant\n cp build/libs/* ."

class Gene:
    def genCMD(self):
        files = os.listdir(repoDir)
        if "pom.xml" in files:
            return buiders["maven"].getBuildCMD()
        elif "build.gradle" in files:
            return buiders["gradle"].getBuildCMD()
        elif "build.xml" in files:
            return buiders["ant"].getBuildCMD()
        return "sleep 1s"

buiders = {
    "maven":MavenBuilder(),
    "gradle":GradleBuilder(),
    "ant":AntBuilder()
}

#print Gene().genCMD()

# if __name__ == "__main__":
#     repoDir=sys.argv[1]
#     print Gene().genCMD()

def test():
    buiders["gradle"].prepareEnvironment()

test()
