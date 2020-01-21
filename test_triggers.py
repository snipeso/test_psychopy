from trigger import Trigger

from psychopy import core
from config import CONF


trigger = Trigger(CONF["trigger"]["serial_device"],
                  CONF["sendTriggers"], CONF["trigger"]["labels"])
n = 1000

for i in range(n):
    trigger.send("Stim")


