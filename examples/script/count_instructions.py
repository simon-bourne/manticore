#!/usr/bin/env python

import sys
from manticore import Manticore

'''
Count the number of emulated instructions.

This example uses the context property of the Manticore object to store data
that's updated by the hook function. Manticore.context is needed to properly
share data when running with multiple worker processes.
'''

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: %s [binary]\n"%(sys.argv[0],))
        sys.exit(2)

    m = Manticore(sys.argv[1])
    m.workers = 3
    m.context['count'] = 0

    @m.hook(None)
    def explore(state):
        m.context['count'] += 1

    m.run()

    print "Executed ", m.context['count'], " instructions."
