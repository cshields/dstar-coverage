# Copyright 2012 Corey Shields cshields@gmail.com
# License for use and modification under GPLv2
# Captures a sequence of coordinates, one set per call of this command
# intended to be run as a D*query command.  This will log the data
# collected and then repeat it back to check the viability of the
# two-way link.

import argparse
import logging

logging.basicConfig(filename='queryreport.log',level=logging.INFO,
					format='%(asctime)s,%(message)s', 
					datefmt='%m/%d/%Y %I:%M:%S %p')

parser = argparse.ArgumentParser(description='Process submitted coordinates.')
parser.add_argument('sequence', 
				   help='Packet position in a sequence')
parser.add_argument('latitude', 
                   help='Latitude: DDMM.mmN')
parser.add_argument('longitude',
				   help='Longitude: DDDMM.mmW')

args = parser.parse_args()
logging.info(args.sequence + ',' + args.latitude + ',' + args.longitude)
