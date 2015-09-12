#!/usr/bin/python
# ----------------------------------------------------------------------------
# Multiplying Table Generator
# ----------------------------------------------------------------------------
'''
Multiplying Table Generator
'''
from __future__ import division, unicode_literals, print_function
import sys
import os
import getopt


__docformat__ = 'restructuredtext'


def run(ffrom, to, multnumber, tables):
    # print 8 elements per line
    sys.stdout.write('; autogenerated table: %s -f%s -t%s -%d %s' % (os.path.basename(sys.argv[0]), ffrom, to, tables, multnumber))

    if tables == 1:
        for i, item in enumerate(range(ffrom, to)):
            if i % 8 == 0:
                sys.stdout.write('\n.word $%04x' % (i * multnumber))
            else:
                sys.stdout.write(',$%04x' % (i * multnumber))
    else:
        lows_str = '\n; LSB values\nmult_%d_lo:' % multnumber
        his_str = '\n; MSB values\nmult_%d_hi:' % multnumber
        for i, item in enumerate(range(ffrom, to)):
            if i % 8 == 0:
                lows_str += '\n.byte <$%04x' % (i * multnumber)
                his_str += '\n.byte >$%04x' % (i * multnumber)
            else:
                lows_str += ',<$%04x' % (i * multnumber)
                his_str += ',>$%04x' % (i * multnumber)

        sys.stdout.write(lows_str)
        sys.stdout.write(his_str)
    sys.stdout.write('\n')


def help():
    print("%s v0.1 - An utility to create multiplyting tables. Useful for c64 and other 8-bit computers" % os.path.basename(sys.argv[0]))
    print("\nUsage: %s [options] number_to_multiply" % os.path.basename(sys.argv[0]))
    print("\t-f from_number\t\t\tDefault=0")
    print("\t-t to_number\t\t\tDefault=255")
    print("\t-1\t\t\tGenerate 1 table with values stored in .word")
    print("\t-2\t\t\tGenerate 2 tables. One with the low values (.byte), other with the hi values (.byte). Default: One table ")
    print("\nExamples:")
    print("\t%s -f0 -t24 40" % os.path.basename(sys.argv[0]))
    sys.exit(-1)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        help()

    ffrom = 0
    to = 255
    number_to_multiply = 0
    tables = 1

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "f:t:12", ["from=", "to=","one","two"])
        for opt, arg in opts:
            if opt in ("-f", "--from"):
                ffrom = int(arg)
            elif opt in ("-t", "--tto"):
                to = int(arg)
            elif opt in ("-1", "--one"):
                tables = 1
            elif opt in ("-2", "--two"):
                tables = 2
        if not len(args) == 1:
            help()
        else:
            number_to_multiply = int(args[0])
    except getopt.GetoptError, e:
        print(e)

    run(ffrom, to, number_to_multiply, tables)
