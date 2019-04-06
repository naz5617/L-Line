from asterisk.agi import *




agi = AGI()
agi.verbose("python agi started")
caller_id = agi.env['agi callerid']
agi.verbose("Call from %s" % caller_id)
agi.answer()
agi.stream_file('greeting_audio')
agi.hangup()









"""
myVar = 'something'
Some variable

agi = AGI()

creates an agi instance


agi.answer()

I/O Communication: stdin, stdout, stderr

"""
