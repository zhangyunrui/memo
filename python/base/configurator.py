import codecs
import os

import sys
import yaml


class ConfigStore(object):
    SEPARATOR = '/'

    def __init__(self):
        self._data = {}

    @classmethod
    def normalize_key(cls, key):
        return key[1:] if key.startswith(cls.SEPARATOR) else key

    def get(self, key):
        return self[key]

    def __getitem__(self, key):
        key = self.normalize_key(key)
        data = self._data
        try:
            for part in key.split(self.SEPARATOR):
                data = data[part]
            return data
        except KeyError:
            raise KeyError('`{}` is not found'.format(key))

    def __setitem__(self, key, value):
        key = self.normalize_key(key)
        parts = key.split(self.SEPARATOR)
        if not all([part.strip() for part in parts]):
            raise KeyError('{} contains full-spaces part'.format(key))

        current = self._data
        for part in parts:
            if part not in current:
                current[part] = ConfigStore()
            previous = current
            current = current[part]
        previous[parts[-1]] = value

    def __contains__(self, key):
        key = self.normalize_key(key)
        try:
            _ = self[key]  # noqa
            return True
        except KeyError:
            return False

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return 'ConfigStore({})'.format(repr(self._data))

    def iteritems(self):
        for k1, v1 in self._data.iteritems():
            if isinstance(v1, ConfigStore):
                for k2, v2 in v1.iteritems():
                    yield self.SEPARATOR.join([k1, k2]), v2
            else:
                yield k1, v1

    def get_raw(self):
        res = {}
        for k1, v1 in self._data.iteritems():
            v = v1.get_raw() if isinstance(v1, ConfigStore) else v1
            res.update({k1: v})
        return res


class Node(object):
    def __init__(self):
        self.value = None
        self.children = {}

    def __str__(self):
        return 'value: {}, children: {}'.format(self.value, self.children)


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
        node.value = path

    def traverse(self, root):
        yield root
        for child in root.children.itervalues():
            for node in self.traverse(child):
                yield node

    @property
    def nodes(self):
        for node in self.traverse(self.root):
            yield node


class Configurator(object):
    def __init__(self, config_file):
        self.config_file = os.path.abspath(config_file)
        with codecs.open(self.config_file, 'r', encoding='utf-8') as cfile:
            self._raw_configs = yaml.load(cfile)
        self._validate()
        self._populate()

    def _validate(self):
        t = Trie()
        for key, value in self._raw_configs.iteritems():
            t.insert(key)

        for node in t.nodes:
            if node.value is not None and node.children:
                raise Exception

    def _populate(self):
        self._store = ConfigStore()

        for key, value in self._raw_configs.iteritems():
            self._store[key] = value

    def __getitem__(self, key):
        return self._store[key]

    def __contains__(self, key):
        return key in self._store

    def get(self, key):
        return self._store[key]

    def get_raw(self):
        return self._store.get_raw()

    def iteritems(self):
        for k, v in self._store.iteritems():
            yield k, v

    def __str__(self):
        return str(self._store)

    def __repr__(self):
        return '<Configurator: {}>'.format(repr(self._store))


conf = Configurator('config.tpl.yaml')
conf.get_raw()
for k, v in conf.iteritems():
    print k, v

