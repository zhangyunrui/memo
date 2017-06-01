import codecs
import inspect
import os

import sys
import yaml


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, path):
        node = self.root
        for key in path.split(ConfigStore.SEPARATOR):
            if key not in node.children:
                child = Node()
                node.children[key] = child
                node = child
            else:
                node = node.children[key]

    def log(self, num, around):
        print('{:~^20}{:~^30}-{}'.format(num, around,
                                         '-'.join(
                                             [i[3] for i in inspect.getouterframes(inspect.currentframe())[1:-5]])))

    def traverse(self, root):
        self.log(' +2 ', root)
        yield root
        self.log(' -2 ', root)
        for child in root.children.itervalues():
            self.log(' +3 ', child)
            for node in self.traverse(child):
                self.log(' +4 ', node)
                yield node
                self.log(' -4 ', node)
            self.log(' -3 ', child)

    @property
    def nodes(self):
        self.log(' 0 ', "self")
        for node in self.traverse(self.root):
            self.log(' +1 ', node)
            yield node
            self.log(' -1 ', node)

            # def traverses(self, root):
            #     print 1
            #     print root
            #     print 2
            #     for child in root.children.itervalues():
            #         print 3
            #         self.traverses(child)
            #         print 4

            # def traverses(self, root):
            #     print root
            #     ll = root.children.values()
            #     for child in ll:
            #         print child
            #         ll.extend(child.children.values())

            # def traverse(self, root):
            #     print root
            #     for child in root.children.itervalues():
            #         for node in self.traverse(child):
            #             yield
            #
            # @property
            # def nodes(self):
            #     for node in self.traverse(self.root):
            #         pass
            #     return

            # def traverse(self, root):
            #     yield root
            #     for child in root.children.itervalues():
            #         tt = self.traverse(child)
            #         yield tt.next()
            #
            # @property
            # def nodes(self):
            #     for node in self.traverse(self.root):
            #         yield node


class Node(object):
    def __init__(self):
        self.children = {}

    def __str__(self):
        return 'children: {}'.format(self.children.keys())


class Configurator(object):
    def __init__(self, config_file):
        self.config_file = os.path.abspath(config_file)
        with codecs.open(self.config_file, 'r', encoding='utf-8') as cfile:
            self._raw_configs = yaml.load(cfile)
        self._validate()

    def _validate(self):
        t = Trie()
        for key, value in self._raw_configs.iteritems():
            t.insert(key)

        # t.nodes

        # t.traverses(t.root)

        # tt = t.nodes
        # print 1

        # tt = t.nodes
        # print tt.next()
        # print '{:~^30}'.format('split')
        # print tt.next()
        # print '{:~^30}'.format('split')
        # print tt.next()

        for node in t.nodes:
            print node


class ConfigStore(object):
    SEPARATOR = '/'


Configurator('config.tpl.yaml')
