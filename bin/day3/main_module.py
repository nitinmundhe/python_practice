from project.net import submodule, submodule as s

# import sys
# print(sys.path)
# sys.path.append(r'C:\nitsmagic\lib')
print('main module : ', submodule.msg)
print('main module : ', submodule.sub(50, 20))

print('main module with alias : ', s.msg)
print('main module with alias : ', s.sub(50, 20))

from project.net.submodule import msg, sub

print('main module with from : ', msg)
print('main module with from : ', sub(50, 20))

from project.net.submodule import msg as m, sub as s

print('main module with from with alias : ', m)
print('main module with from with alias : ', s(50, 20))

# use * to import all
from project.net.submodule import *

print('With import * Msg : ', msg)
print('With import * Sub : ', sub(50, 20))

import project.net.submodule

print('Import with Package > Msg : ', project.net.submodule.msg)
print('Import with Package > Sub : ', project.net.submodule.sub(50, 20))

import project.net.submodule as s

print('Import with Package and alias > Msg : ', s.msg)
print('Import with Package and alias > Sub : ', s.sub(50, 20))

from project.net.submodule import msg, sub

print('Package with from import > Msg : ', msg)
print('Package with from import > Sub : ', sub(50, 20))

