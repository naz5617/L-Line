from pystrix import *
import random
import time

if __name__ == '__main__':
    agi = pystrix.agi.AGI()
    send_audio = agi.execute(pystrix.agi.core.ControlStreamFile)
    digit_input = agi.execute(pystrix.agi.core.WaitForDigit)
    agi.execute(pystrix.agi.core.Answer)

    num = digit_input
    send_audio('intro.wav')
    send_audio('max.wav')
    send_audio('joe.wav')
    send_audio('angela.wav')
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
        send_audio(name + '_Intro_1')
    elif intro == 2:
        send_audio(name + '_Intro_2')
    elif intro == 3:
        send_audio(name + '_Intro_3')
    else:
        send_audio(name + '_Intro_4')
    time.sleep(2)
    send_audio(name + '_Introduction')
    time.sleep(2)
    send_audio(name + '_Intro_Response')
    num = digit_input
    if num == 1:
        agi.execute(pystrix.agi.core.SetExtension(109))
        # transfer call to conference room
    elif num == 2:
        num = digit_input
        send_audio(name + '_Intro_LiveMenu')
        # Start Live chat info
        if num == 1:
            send_audio(name + '_Basic')
            agi.execute(pystrix.agi.core.SetExtension(793))
        elif num == 2:
            send_audio(name + '_Basic+')
            agi.execute(pystrix.agi.core.SetExtension(793))
        elif num == 3:
            send_audio(name + '_Brutal')
            agi.execute(pystrix.agi.core.SetExtension(793))
        elif num == 4:
            send_audio(name + '_Brutal+')
            agi.execute(pystrix.agi.core.SetExtension(793))
        elif num == 5:
            send_audio(name + '_Other')
            agi.execute(pystrix.agi.core.SetExtension(793))
        elif num == 6:
            send_audio(name + '_Ultra')
            agi.execute(pystrix.agi.core.SetExtension(793))
        elif num == 7:
            send_audio(name + '_Specials_Intro')
            spec = random.randint(1, 6)
            if spec == 1:
                send_audio(name + '_UnderTheSea')
                agi.execute(pystrix.agi.core.SetExtension(793))
            elif spec == 2:
                send_audio(name + '_Lovecraft')
                agi.execute(pystrix.agi.core.SetExtension(793))
            elif spec == 3:
                send_audio(name + '_Rainbow')
                agi.execute(pystrix.agi.core.SetExtension(793))
            elif spec == 4:
                send_audio(name + '_Fruit')
                agi.execute(pystrix.agi.core.SetExtension(793))
            elif spec == 5:
                send_audio(name + '_Bees')
                agi.execute(pystrix.agi.core.SetExtension(793))
            else:
                send_audio(name + '_Soups')
                agi.execute(pystrix.agi.core.SetExtension(793))

    elif num == 3:
        send_audio(name + '_Porno_Intro')
        porno = []
        while porno <= 5:
            random = random.randint(1, 32)
            porn = name + "_p" + random
            if porn not in porno:
                porno.append(porn)
        send_audio(porno[1])
        time.sleep(1)
        send_audio(porno[2])
        time.sleep(1)
        send_audio(porno[3])
        time.sleep(1)
        send_audio(porno[4])
        time.sleep(1)
        send_audio(porno[5])
        # go into the pre-made porno listings random five.
    else:
        agi.execute(pystrix.agi.core.Hangup())

    agi.execute(pystrix.agi.core.Hangup())


