from Asterisk.Manager import Manager

class GrabCallerID(object):
    def Newchannel(self, pbx, event):

        cli = event.Callerid
        print ("CallerID for %s is %s" %(event.Channel, cli))

        if self.bad_caller(cli):
            event.Channel.hangup()

    def bad_caller(self, cli):
        return cli.startswith('0870') # or whatever

    def __init__(self):
        self.events = events = Asterisk.Util.EventCollection()
        events.subscribe('NewChannel', self.Newchannel())

    def register(self, some_pbx):
        some_pbx.events += self.events

    def unregister(self, some_pbx):
        some_pbx.events -= self.events






pbx = Manager(('localhost', 5038),'dw', 'letmein')
grab = GrabCallerID()

grab.register(pbx)

pbx.serve_forever()










"""
agi =
agi.verbose("python agi started")
caller_id = agi.env['agi callerid']
agi.verbose("Call from %s" % caller_id)
agi.answer()
agi.stream_file('greeting_audio')
agi.hangup()

"""""







"""
myVar = 'something'
Some variable

agi = AGI()

creates an agi instance


agi.answer()

I/O Communication: stdin, stdout, stderr

"""
