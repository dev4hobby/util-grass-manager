#!/usr/bin/python
import os
import sys

def alert_perm():
  print('[Gardener] : Please run as root perm')
  sys.exit(1)

if int(os.getuid()) != 0:
  alert_perm()

fpath = os.getcwd()+'/daily_report.log'
with open('gardener', 'w') as fd:
  fd.write('#!/bin/bash\n')
  fd.write('date >> '+fpath+'\n')
  fd.write('git add '+fpath+'\n')
  fd.write('git commit -m "G\'day Sir"\n')
  fd.write('git push\n')

os.system('chmod 755 gardener')
try:
  os.system('mv gardener /etc/cron.daily/')
  os.system('service cron restart')
  print('[Gardener] : I\'m ready.')
  print('You can find me here,')
  print('"/etc/cron.daily/"')
except Exception as e:
  alert_perm()

print('[Gardener] : Thank you for hiring me!')
