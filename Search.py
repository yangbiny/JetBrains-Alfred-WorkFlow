from base import JetBrainsUtils
from workflow import Workflow
import sys

if __name__ == '__main__':
    path = sys.argv[1]
    jetbrains = JetBrainsUtils.JetBrainsUtils(path)
    jobs = jetbrains.readFile()
    wf = Workflow()
    jsonStr = list()
    for job in jobs:
        index = job.rfind("/")
        jobName = job[index + 1:]
        wf.add_item(title=jobName, subtitle=job+","+path, arg=job, valid=True)
    wf.send_feedback()
