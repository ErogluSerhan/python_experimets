# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def lmb(aa):
    return aa*5

# ile aşağıdaki aynı

b = lambda a:a*5

print b(5)