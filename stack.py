#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StackOverflowError(RuntimeError):
    pass


class StackIsEmptyError(RuntimeError):
    pass


class Stack:
    def __init__(self, size):
        self.size = size
        self.storage = [None] * size
        self.head = -1

    def push(self, v):
        if self.head >= self.size - 1:
            raise StackOverflowError(RuntimeError)
        elif self.head < self.size - 1:
            self.head += 1
            self.storage[self.head] = v
            return self.storage

    def pop(self):
        if self.head == -1:
            raise StackIsEmptyError(RuntimeError)
        else:
            p = self.storage[self.head]
            self.head -= 1
            return p

    def __len__(self):
        return self.head + 1