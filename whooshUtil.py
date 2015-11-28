#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.analysis import RegexAnalyzer
from whoosh.query import Regex

class WhooshUtil:
    def __init__(self, indexDir):
	#analyzer = RegexAnalyzer(r"(\w+(\.?\w+)*)")
	analyzer = RegexAnalyzer(ur".*")
	schema = Schema(path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
	#schema = Schema(path=ID(stored=True), content=TEXT(stored=True))
	self.ix = create_in(indexDir, schema)
	self.writer = self.ix.writer()

    def addDoc(self, path, content):
	path = unicode(path)
	content = unicode(content)
        self.writer.add_document(path=path, content = content)

    def commit(self):
	self.writer.commit()
	self.searcher = self.ix.searcher()

    def search(self, key):
        #results = self.searcher.find("content", key)
        results = self.searcher.search(Regex("content", key))
	#print len(results)
	return (len(results), results)

if __name__ == '__main__':
    whooshUtil = WhooshUtil("testIndexDir")
    whooshUtil.addDoc(u"1", u"Hello world")
    whooshUtil.addDoc(u"2", u"Hell word")
    whooshUtil.commit()
    print whooshUtil.search(u"Hello .*")[1][0]["content"]
