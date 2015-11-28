#!/usr/bin/env python
#-*- coding: utf8 -*-
#########################################################################
# File Name: logFile.py
# Author: kejiewei
# mail: jiewei_ke@163.com
# Created Time: Sat 28 Nov 2015 12:16:52 AM CST
#########################################################################
import re

LOG_PATTERN = r"(?P<logTime>.*) (?P<logType>(INFO|WARN|ERROR)) org.apache.hadoop.hdfs[^:]+: (?P<logMsg>.*)"

class LogFile:
    def __init__(self, logFile):
        self.logFile = logFile
        self.logList = []
        with open(logFile) as input:
            for log in input:
                log = log.strip()
                m = re.match(LOG_PATTERN, log)
                if m == None:
                    continue
                logMsg = m.group('logMsg').strip()
                logType = m.group('logType').strip()
                logTime = m.group('logTime').strip()
                self.logList.append([logMsg, logType, logTime])
