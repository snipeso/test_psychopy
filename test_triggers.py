from trigger import Trigger, id2triggers, triggers2id, crazy_shift

from psychopy import core
from config import CONF


#trigger = Trigger(CONF["trigger"]["serial_device"],
#                  CONF["sendTriggers"], CONF["trigger"]["labels"])

for i in range(0,32):
#    trigger.send(i)
    print(i, bin(crazy_shift(i)))
#    core.wait(.5)




for n in range(0,70):
    t = id2triggers(n)
    s = map(crazy_shift, t)
#    m = triggers2id(t)
    print("aaah", n, [bin(x) for x in s])
        

print("done")