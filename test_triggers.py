from trigger import Trigger

from psychopy import core
from config import CONF


trigger = Trigger(CONF["trigger"]["serial_device"],
                  CONF["sendTriggers"], CONF["trigger"]["labels"])
n = 500

for i in range(1,n):
    trigger.send(i)
    core.wait(1)


