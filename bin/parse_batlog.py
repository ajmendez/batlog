#!/usr/bin/env python
import os
import re
import time
import json
from dateutil import parser


FILENAME = os.path.expanduser('~/.batlog.dat')
OUTFILENAME = os.path.expanduser('~/data/batterylog/simplelog.json')
PREFIX = '    | |           '
PATTERN = '"(\w+)" = (.+)'

def parse_legacy(value):
    tmp = value.replace('=',':')
    return json.loads(tmp)

def parse(filename, outfile):
    out = []
    measurement = {}
    
    if os.path.exists(outfile):
        print 'Output file already exists: {}'.format(outfile)
    
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line.startswith(PREFIX):
                x = line.replace(PREFIX, '').strip()
                item,value = re.match(PATTERN, x).groups()
                if item == 'LegacyBatteryInfo':
                    tmp = parse_legacy(value)
                    measurement.update(tmp)
                else:
                    measurement[item] = int(value)
            else:
                if len(measurement) > 0:
                    out.append(measurement)
                
                key = time.mktime(parser.parse(line).timetuple())
                measurement = dict(date=key)
    with open(outfile, 'w') as f:
        json.dump(out, f, indent=2)
                
                    



if __name__ == '__main__':
    parse(FILENAME, OUTFILENAME)
