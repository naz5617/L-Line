from pystrix import *
import re
import threading
import time

if __name__ == '__main__':
    agi = pystrix.agi.AGI()

    agi.execute(pystrix.agi.core.Answer)

    response = agi.execute(pystrix.agi.core.StreamFile('demo-thanks', escape_digits=('1', '2')))
    if response:
        (dtmf_character, offset) = response
    num = agi.execute(pystrix.agi.core.GetVariable)
    agi.execute(pystrix.agi.core.ControlStreamFile('intro.wav'))
    if num ==1:
        agi.execute(pystrix.agi.core.ControlStreamFile('intro.wav'))
    elif num == 2:
        return(num)
    elif num ==3:
        return (num)
    else:
        agi.execute(pystrix.agi.core.Hangup())


