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
        intro = random.randint(1, 4)
        if intro == 1:
            agi.execute(pystrix.agi.core.ControlStreamFile('Max_Intro_1'))
        elif intro == 2:
            agi.execute(pystrix.agi.core.ControlStreamFile('Max_Intro_2'))
        elif intro == 3:
            agi.execute(pystrix.agi.core.ControlStreamFile('Max_Intro_3'))
        else:
            agi.execute(pystrix.agi.core.ControlStreamFile('Max_Intro_4'))
        time.sleep(2)
        agi.execute(pystrix.agi.core.ControlStreamFile('Max_Introduction'))
        time.sleep(2)
        agi.execute(pystrix.agi.core.ControlStreamFile('Max_Intro_Response'))
        num = agi.execute(pystrix.agi.core.WaitForDigit)
        if num == 1:
            num = agi.execute(pystrix.agi.core.WaitForDigit)
            # transfer call to conference room
        elif num == 2:
            num = agi.execute(pystrix.agi.core.WaitForDigit)
            agi.execute(pystrix.agi.core.ControlStreamFile('Max_Intro_LiveMenu'))
            # Start Live chat info
            if num == 1:
                agi.execute(pystrix.agi.core.ControlStreamFile('Max_Basic'))
            elif num == 2:
                agi.execute(pystrix.agi.core.ControlStreamFile('Max_Basic+'))
            elif num == 3:
                agi.execute(pystrix.agi.core.ControlStreamFile('Max_Brutal'))
            elif num == 4:
                agi.execute(pystrix.agi.core.ControlStreamFile('Max_Brutal+'))
            elif num == 5:
                agi.execute(pystrix.agi.core.ControlStreamFile('Max_Other'))
            elif num == 6:
                agi.execute(pystrix.agi.core.ControlStreamFile('Max_Ultra'))
            elif num == 7:
                agi.execute(pystrix.agi.core.ControlStreamFile('Max_Specials_Intro'))
                spec = random.randint(1, 6)
                if spec == 1:
                    agi.execute(pystrix.agi.core.ControlStreamFile('Max_UnderTheSea'))
                elif spec == 2:
                    agi.execute(pystrix.agi.core.ControlStreamFile('Max_Lovecraft'))
                elif spec == 3:
                    agi.execute(pystrix.agi.core.ControlStreamFile('Max_Rainbow'))
                elif spec == 4:
                    agi.execute(pystrix.agi.core.ControlStreamFile('Max_Fruit'))
                elif spec == 5:
                    agi.execute(pystrix.agi.core.ControlStreamFile('Max_Bees'))
                else:
                    agi.execute(pystrix.agi.core.ControlStreamFile('Max_Soups'))

        elif num == 3:
            num = agi.execute(pystrix.agi.core.WaitForDigit)
            agi.execute(pystrix.agi.core.ControlStreamFile('Max_Porno_Intro'))
            porno = []
            while porno <= 5:
                porn = random.randint(1, 32)
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
    elif num == 2:
        intro = random.randint(1, 4)
        if intro == 1:
            agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Intro_1'))
        elif intro == 2:
            agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Intro_2'))
        elif intro == 3:
            agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Intro_3'))
        else:
            agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Intro_4'))
        time.sleep(2)
        agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Introduction'))
        time.sleep(2)
        agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Intro_Response'))
        num = agi.execute(pystrix.agi.core.WaitForDigit)
        if num == 1:
            num = agi.execute(pystrix.agi.core.WaitForDigit)
            # transfer call to conference room
        elif num == 2:
            num = agi.execute(pystrix.agi.core.WaitForDigit)
            agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Intro_LiveMenu'))
            # Start Live chat info
            if num == 1:
                agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Basic'))
            elif num == 2:
                agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Basic+'))
            elif num == 3:
                agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Brutal'))
            elif num == 4:
                agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Brutal+'))
            elif num == 5:
                agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Other'))
            elif num == 6:
                agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Ultra'))
            elif num == 7:
                agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Specials_Intro'))
                spec = random.randint(1, 6)
                if spec == 1:
                    agi.execute(pystrix.agi.core.ControlStreamFile('Joe_UnderTheSea'))
                elif spec == 2:
                    agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Lovecraft'))
                elif spec == 3:
                    agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Rainbow'))
                elif spec == 4:
                    agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Fruit'))
                elif spec == 5:
                    agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Bees'))
                else:
                    agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Soups'))

        elif num == 3:
            num = agi.execute(pystrix.agi.core.WaitForDigit)
            agi.execute(pystrix.agi.core.ControlStreamFile('Joe_Porno_Intro'))
            porno = []
            while porno <= 5:
                porn = random.randint(1, 32)
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
    elif num == 3:
        agi.execute(pystrix.agi.core.ControlStreamFile('angela.wav'))
        num = agi.execute(pystrix.agi.core.WaitForDigit)
        if num == 1:
            num = agi.execute(pystrix.agi.core.WaitForDigit)
            # transfer call to conference room
        elif num == 2:
            num = agi.execute(pystrix.agi.core.WaitForDigit)
            agi.execute(pystrix.agi.core.ControlStreamFile('angela.wav'))
            if num == 1:

                agi.execute(pystrix.agi.core.ControlStreamFile('basic.wav'))
            elif num == 2:
                agi.execute(pystrix.agi.core.ControlStreamFile('basic+.wav'))
            elif num == 3:
                agi.execute(pystrix.agi.core.ControlStreamFile('brutal.wav'))
            elif num == 4:
                agi.execute(pystrix.agi.core.ControlStreamFile('brutal+.wav'))
            elif num == 5:
                agi.execute(pystrix.agi.core.ControlStreamFile('other.wav'))
            elif num == 6:
                agi.execute(pystrix.agi.core.ControlStreamFile('Ultra.wav'))
            elif num == 7:
                agi.execute(pystrix.agi.core.ControlStreamFile('Specials.wav'))

            # Start Live chat info
        elif num == 3:
            num = agi.execute(pystrix.agi.core.WaitForDigit)
            agi.execute(pystrix.agi.core.ControlStreamFile('Ang_Porno_Intro'))
            porno = []
            while porno <= 5:
                porn = random.randint(1, 32)
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


