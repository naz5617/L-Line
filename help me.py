from pystrix import *
import random
import time

if __name__ == '__main__':
    agi = pystrix.agi.AGI()

    agi.execute(pystrix.agi.core.Answer)

    num = agi.execute(pystrix.agi.core.WaitForDigit)
    agi.execute(pystrix.agi.core.ControlStreamFile('intro.wav'))
    agi.execute(pystrix.agi.core.ControlStreamFile('max.wav'))
    agi.execute(pystrix.agi.core.ControlStreamFile('joe.wav'))
    agi.execute(pystrix.agi.core.ControlStreamFile('angela.wav'))
    if num == 1:
        name = "Max"
    elif num == 2:
        name = "Joe"
    elif num == 3:
        name = "Angela"
    else:
        agi.execute(pystrix.agi.core.Hangup())
    intro = random.randint(1, 4)
    if intro == 1:
        agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Intro_1'))
    elif intro == 2:
        agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Intro_2'))
    elif intro == 3:
        agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Intro_3'))
    else:
        agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Intro_4'))
    time.sleep(2)
    agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Introduction'))
    time.sleep(2)
    agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Intro_Response'))
    num = agi.execute(pystrix.agi.core.WaitForDigit)
    if num == 1:
        num = agi.execute(pystrix.agi.core.WaitForDigit)
        # transfer call to conference room
    elif num == 2:
        num = agi.execute(pystrix.agi.core.WaitForDigit)
        agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Intro_LiveMenu'))
        # Start Live chat info
        if num == 1:
            agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Basic'))
        elif num == 2:
            agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Basic+'))
        elif num == 3:
            agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Brutal'))
        elif num == 4:
            agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Brutal+'))
        elif num == 5:
            agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Other'))
        elif num == 6:
            agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Ultra'))
        elif num == 7:
            agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Specials_Intro'))
            spec = random.randint(1, 6)
            if spec == 1:
                agi.execute(pystrix.agi.core.ControlStreamFile(name + '_UnderTheSea'))
            elif spec == 2:
                agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Lovecraft'))
            elif spec == 3:
                agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Rainbow'))
            elif spec == 4:
                agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Fruit'))
            elif spec == 5:
                agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Bees'))
            else:
                agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Soups'))

    elif num == 3:
        num = agi.execute(pystrix.agi.core.WaitForDigit)
        agi.execute(pystrix.agi.core.ControlStreamFile(name + '_Porno_Intro'))
        porno = []
        while porno <= 5:
            random = random.randint(1, 32)
            porn = name + "_p" + random
            if porn not in porno:
                porno.append(porn)
        agi.execute(pystrix.agi.core.ControlStreamFile(porno[1]))
        time.sleep(1)
        agi.execute(pystrix.agi.core.ControlStreamFile(porno[2]))
        time.sleep(1)
        agi.execute(pystrix.agi.core.ControlStreamFile(porno[3]))
        time.sleep(1)
        agi.execute(pystrix.agi.core.ControlStreamFile(porno[4]))
        time.sleep(1)
        agi.execute(pystrix.agi.core.ControlStreamFile(porno[5]))
        # go into the pre-made porno listings random five.
    else:
        agi.execute(pystrix.agi.core.Hangup())

    agi.execute(pystrix.agi.core.Hangup())


