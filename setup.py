# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et:

import sys

from distutils.core import setup

try:
    import gtk
except:
    print('PyGTK isn\'t installed.')
    sys.exit(1)

setup(name='Traydesk',
      description='Displays windows not in the current desktop in the system tray.',
      author='Ricardo Liang',
      author_email='ricardoliang@gmail.com',
      url='https://github.com/rliang/traydesk',
      license='MIT/X',
      platforms='POSIX',
      scripts=['traydesk'],
      data_files=[('share/doc/traydesk', ['LICENSE'])]
      )
