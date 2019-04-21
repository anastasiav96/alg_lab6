#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stack import Stack

def is_paranthesis_balanced(s):
  
    open_bkt = ['(','[','{','<']
    matches = [('{','}'), ('[',']'), ('(',')'), ('<','>')]
    stack = Stack(len(s))
    
    for i in s:
        if i in open_bkt:
            stack.push(i)
        else:
            if stack.__len__() == 0 :
                return False
            last_bkt = stack.pop()
            if (last_bkt, i) not in matches:
                return False
    return stack.__len__() == 0


