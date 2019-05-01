#!/usr/bin/env python2
# coding=utf-8

"""
Load all logs into ElasticSearch.
"""
import os
import requests


class ESLog(object):
    def __init__(self):
        self.host = 'http://127.0.0.1:9200'
        # self.host = 'http://10.70.1.31:9200'
        self.index = 'mercku'
        self.type = 'doc'

        self.req = requests.Session()

    @property
    def index_url(self):
        return '/'.join([self.host, self.index])

    @property
    def type_url(self):
        return '/'.join([self.host, self.index, self.type])

    @property
    def mapping_url(self):
        return '/'.join([self.host, self.index, '_mapping', self.type])

    def reset_type(self):
        # NOTE: you could not remove a type from ES, which means you could never setup a clean type during
        # re-execution. so, we have to setup the mapping correctly, and then cleanup all docs in the type.
        self.req.delete(self.index_url)

        self.req.put(self.index_url, json={
            "settings": {
                "analysis": {
                    "analyzer": {
                        "hyku_ngram_analyzer": {
                            "type": "custom",
                            "tokenizer": "hyku_ngram_tokenizer",
                            "filter": [
                                "lowercase",
                                "asciifolding"
                            ]
                        },
                        "hyku_punctuation_analyzer": {
                            "type": "custom",
                            "tokenizer": "hyku_punctuation_tokenizer",
                            "filter": [
                                "lowercase",
                                "asciifolding"
                            ]
                        }
                    },
                    "tokenizer": {
                        "hyku_punctuation_tokenizer": {
                            "type": "pattern",
                            "pattern": "\\p{Punct}|\\h"
                        },
                        "hyku_ngram_tokenizer": {
                            "type": "nGram",
                            "min_gram": 1,
                            "max_gram": 14,
                            "token_chars": [
                                "letter",
                                "digit"
                            ]
                        }
                    }
                }
            }
        })
        self.req.put(self.mapping_url, json={"properties": {
            "data": {
                "analyzer": "hyku_ngram_analyzer",
                "search_analyzer": "hyku_punctuation_analyzer",
                "type": "text",
                "fielddata": True
            },
            "req_time": {"type": "integer"},
            "host": {"type": "keyword"},
            "method": {"type": "keyword"},
            "mMerckuMethod": {"type": "keyword"},
            "serverSend": {"type": "long"},
            "end_serverReply": {"type": "integer"},
            "appRecv": {"type": "long"},
            "serverReply": {"type": "long"},
            "serverInitial_appSend": {"type": "integer"},
            "appSend": {"type": "long"},
            "serverRecv_routerReply": {"type": "integer"},
            "routerReply_routerRecv": {"type": "integer"},
            "routerReply": {"type": "long"},
            "serverInitial": {"type": "long"},
            "serverSend_routerRecv": {"type": "integer"},
            "routerRecv": {"type": "long"},
            "serverRecv": {"type": "long"},
            "totalTime": {"type": "integer"},
            "t0": {"type": "integer"},
            "t1": {"type": "integer"},
            "t2": {"type": "integer"},
            "t3": {"type": "integer"},
            "t4": {"type": "integer"},
            "t5": {"type": "integer"},
            "t6": {"type": "integer"}
        }})

        # cleanup existing type
        # This is useless if index is removed.
        # self.req.post(self.type_url + '/_delete_by_query', json={'query': {'match_all': {}}})

    def emit(self):
        with open('/Users/jiayue/Desktop/mercku-server-mock.log') as f:
            self.req.post(self.type_url, json={"data": f.read()[:100]})

def main():
    esl = ESLog()
    esl.reset_type()
    # esl.emit()

if __name__ == '__main__':
    main()
