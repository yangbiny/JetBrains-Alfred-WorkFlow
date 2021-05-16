from base import JetBrainsUtils
from workflow import Workflow
import sys
import os

if __name__ == '__main__':
    path = sys.argv[1]
    jetbrains = JetBrainsUtils.JetBrainsUtils(path)
    jobs = jetbrains.readFile()
    wf = Workflow()
    jsonStr = list()
    user_home = os.path.expandvars('$HOME')
    for job in jobs:
        index = job.rfind("/")
        jobName = job[index + 1:]
        jobStr = str(job)
        jobStr = jobStr.replace("$USER_HOME$", user_home)
        wf.add_item(title=jobName, subtitle=job, arg=jobStr+","+path, valid=True)
    wf.send_feedback()