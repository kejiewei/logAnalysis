#!/usr/bin/env python
#-*- coding: utf8 -*-
#########################################################################
# File Name: main.py
# Author: kejiewei
# mail: jiewei_ke@163.com
# Created Time: Sat 28 Nov 2015 01:36:16 AM CST
#########################################################################

import logFile
import logTemplate
import logMatcher

logFile = logFile.LogFile("./logs/hadoop-hadoop-datanode-G304G206-BDDL-dell-001.log")
logTemplate = logTemplate.LogTemplate("./logTemplate.txt")
logMatcher = logMatcher.LogMatcher(logFile)

logMsg2logT = logMatcher.logMatch(logTemplate)
for (logMsg, logT) in logMsg2logT.items():
    varDict = logTemplate.parseVarValue(logMsg, logT)
    print varDict

