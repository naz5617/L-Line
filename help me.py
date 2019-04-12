from pystrix import *


if __name__ == '__main__':
    agi = pystrix.agi.AGI()

    agi.execute(pystrix.agi.core.Answer)

    response = agi.execute(pystrix.agi.core.StreamFile('demo-thanks', escape_digits=('1', '2')))
    if response:
        (dtmf_character, offset) = response
    num = agi.execute(pystrix.agi.core.WaitForDigit)
    agi.execute(pystrix.agi.core.ControlStreamFile('intro.wav'))
    agi.execute(pystrix.agi.core.ControlStreamFile('max.wav'))
    agi.execute(pystrix.agi.core.ControlStreamFile('joe.wav'))
    agi.execute(pystrix.agi.core.ControlStreamFile('angela.wav'))
    if num == 1:
        agi.execute(pystrix.agi.core.ControlStreamFile('max.wav'))
        num = agi.execute(pystrix.agi.core.WaitForDigit)
        if num == 1:
            num = agi.execute(pystrix.agi.core.WaitForDigit)
            # transfer call to conference room
        elif num == 2:
            num = agi.execute(pystrix.agi.core.WaitForDigit)
            agi.execute(pystrix.agi.core.ControlStreamFile('max.wav'))
            # Start Live chat info
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

        elif num == 3:
            num = agi.execute(pystrix.agi.core.WaitForDigit)
            # go into the pre-made porno listings random five.
        else:
            agi.execute(pystrix.agi.core.Hangup())
    elif num == 2:
        agi.execute(pystrix.agi.core.ControlStreamFile('joe.wav'))
        num = agi.execute(pystrix.agi.core.WaitForDigit)
        if num == 1:
            num = agi.execute(pystrix.agi.core.WaitForDigit)
            # transfer call to conference room
        elif num == 2:
            num = agi.execute(pystrix.agi.core.WaitForDigit)
            agi.execute(pystrix.agi.core.ControlStreamFile('joe.wav'))
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
            # go into the pre-made porno listings random five.
        else:
            agi.execute(pystrix.agi.core.Hangup())
    else:
        agi.execute(pystrix.agi.core.Hangup())


