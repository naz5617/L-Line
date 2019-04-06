from asterisk.agi import *

def main():

    agi = AGI()
    agi.verbose("python agi started")
    callerId = agi.env['agi callerid']
    agi.verbose("Call from %s" %callerId)

    agi.answer()
    agi.stream_file('greeting_audio')
    agi.hangup()
