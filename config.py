#!/usr/bin/env python3
import os

debug = True
max_curr = os.getenv('AMP_MAX', 40)
min_curr = os.getenv('AMP_MIN', 10)
sense_user = os.getenv('SENSE_USER')
sense_pass =  os.getenv('SENSE_PASS')
openevse_ip = os.getenv('OPENEVSE_IP')
loop_sleep = os.getenv('LOOP_SLEEP', 300)