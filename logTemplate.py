#!/usr/bin/env python
#-*- coding: utf8 -*-
#########################################################################
# File Name: logTemplate.py
# Author: kejiewei
# mail: jiewei_ke@163.com
# Created Time: Sat 28 Nov 2015 12:03:52 AM CST
#########################################################################
import re

'''
logTDict
   logT : {"src" : srcFile, "varList" : varList, "regexLogT" : regexLogT} 
'''
class LogTemplate:
    def __init__(self, tempFile):
        self.logTDict = {}
        self.tempFile = tempFile
        self.getLogTemplate()

    def genLogPattern(self, logT, varList):
        if not (logT.count(".*") == len(varList) or logT.count(".*") + 1 == len(varList)):
            return None
        for i in range(len(varList)):
            logT = logT.replace(".*", "(?P<_%s>.+)" % i, 1)
        return logT

    def getLogTemplate(self):
        with open(self.tempFile) as input:
            for template in input:
                #print template
                tempList = template.strip().split("\t")
                srcFile = tempList[0]
                logT = tempList[1]
                if len(logT) < 10: #Length < 4
                    continue
                varList = tempList[2:]
                regexLogT = self.genLogPattern(logT, varList)
                #print logT
                if logT != None:
                    self.logTDict[logT] = {"src" : srcFile, "varList" : varList, "regexLogT" : regexLogT}

    def parseVarValue(self, logMsg, logT):
        varDict = {}
        varList = self.logTDict[logT]["varList"]
        regexLogT = self.logTDict[logT]["regexLogT"]
        m = re.match(re.compile(regexLogT), logMsg)
        if m != None:
            for i in range(regexLogT.count("(?P<_")):
                varDict[varList[i]] = m.group("_%s" % i)
        return varDict
