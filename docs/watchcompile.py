"""
simple script for watching new content in sphinx source
folder then invoke compile ``make html`` command.

requirement:
    pyinotify
    sh

how to run:
    python watchcompile.py
"""
import pyinotify
from sh import make


wm = pyinotify.WatchManager()
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MODIFY


class EventCompileHandler(pyinotify.ProcessEvent):
    def compile(self):
        print make('html')

    def process_IN_CREATE(self, event):
        print "create:", event.pathname
        self.compile()

    def process_IN_DELETE(self, event):
        print "delete:", event.pathname
        self.compile()

    def process_IN_MODIFY(self, event):
        print "modify:", event.pathname
        self.compile()

handler = EventCompileHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('./source', mask, rec=True)

notifier.loop()
