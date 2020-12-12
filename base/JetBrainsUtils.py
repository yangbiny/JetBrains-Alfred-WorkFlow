# coding=utf-8
import os

import XmlUtils

RECENT_FILE = "/options/recentProjects.xml"


class JetBrainsUtils:
    RUN_PATH = ""
    CONFIG_PATH = ""
    SYSTEM_PATH = ""

    def __init__(self, binPath):
        binFile = open(binPath)
        line = binFile.readline()  # 调用文件的 readline()方法
        while line:
            # 他应该是三个中的最后一行
            if line.startswith("SYSTEM_PATH"):
                JetBrainsUtils.SYSTEM_PATH = line.replace("u'", "").replace("'", "").replace("\n", '')
                break
            if line.startswith("CONFIG_PATH"):
                JetBrainsUtils.CONFIG_PATH = line.replace("u'", "").replace("'", "").replace("\n", '')
            if line.startswith("RUN_PATH"):
                JetBrainsUtils.RUN_PATH = line.replace("u'", "").replace("'", "").replace("\n", '')
            line = binFile.readline()
        binFile.close()

    def readFile(self):
        recent_file = JetBrainsUtils.CONFIG_PATH + RECENT_FILE
        recent_file = recent_file.replace("CONFIG_PATH = ", "")
        if not os.path.exists(recent_file):
            return
        read = XmlUtils.XmlUtils.read(recent_file)
        return read
