#!/usr/bin/env python
#-*- coding: utf8 -*-
#########################################################################
# File Name: logMatcher.py
# Author: kejiewei
# mail: jiewei_ke@163.com
# Created Time: Sat 28 Nov 2015 12:27:33 AM CST
#########################################################################
import whooshUtil
import utils

class LogMatcher:
    def __init__(self, logFile):
        self.whooshUtil = whooshUtil.WhooshUtil("./logIndex")
        self.logT2logMsg = {}
        self.logMsg2logT = {}
        i = 1
        for log in logFile.logList:
            self.whooshUtil.addDoc(logFile.logFile + str(i), log[0])
            i += 1
        self.whooshUtil.commit()

    def logMatch(self, logTemplate):
        for logT in logTemplate.logTDict:
            #print logT
            logT = logT.replace('(', '\(').replace(')', '\)')
            (count, results) = self.whooshUtil.search(logT)
            if count == 0:
                continue
            for hit in results:
                if logT not in self.logT2logMsg:
                    self.logT2logMsg[logT] = []
                self.logT2logMsg[logT].append(hit["content"])
    
        #Reverse self.logT2logMsg to self.logMsg2logT
        for logT in self.logT2logMsg:
            for logMsg in self.logT2logMsg[logT]:
                if logMsg not in self.logMsg2logT:
                    self.logMsg2logT[logMsg] = []
                self.logMsg2logT[logMsg].append(logT)

        #utils.printDict(self.logMsg2logT)
    
        for logMsg in self.logMsg2logT:
            maxLen = 0
            maxLogT = None
            for logT in self.logMsg2logT[logMsg]:
                if len(logT) > maxLen:
                    maxLen = len(logT)
                    maxLogT = logT
            self.logMsg2logT[logMsg] = maxLogT
        utils.printDict(self.logMsg2logT)

        return self.logMsg2logT

