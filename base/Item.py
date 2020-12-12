try:
    import xml.etree.cElementTree as ET
except ImportError:  # pragma: no cover
    import xml.etree.ElementTree as ET


class Item(object):

    def __init__(self):
        self.quicklookurl = None
        self.copytext = None
        self.largetext = None
        self.icontype = None
        self.modifier_subtitles = {}
        self.autocomplete = None
        self._valid = None
        self._arg = None
        self._icon = None
        self._title = None
        self._subtitle = None

    @property
    def subtitle(self):
        return self

    @subtitle.setter
    def subtitle(self, value):
        self._subtitle = value

    @property
    def title(self):
        return self

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def icon(self):
        return self

    @property
    def arg(self):
        return self

    @icon.setter
    def icon(self, value):
        self._icon = value

    @arg.setter
    def arg(self, value):
        self._arg = value

    @property
    def valid(self):
        return self

    @valid.setter
    def valid(self, value):
        self._valid = value

    @staticmethod
    def buildItem(jobName, job):
        item = Item()
        item.title = jobName
        item.subtitle = job
        item.arg = job
        item.icon = "./bac.png"
        item.valid = True
        return item

