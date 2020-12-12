# coding=utf-8
from xml.etree import ElementTree as ET


class XmlUtils:

    def __init__(self):
        pass

    @staticmethod
    def read(path):
        tree = ET.parse(path)
        root = tree.getroot()
        comment = list(root).pop(0)
        option = list(comment).pop(0)
        mapItem = list(option).pop(0)
        res = list()
        for item in list(mapItem):
            res.append(item.attrib["key"])
        return res
