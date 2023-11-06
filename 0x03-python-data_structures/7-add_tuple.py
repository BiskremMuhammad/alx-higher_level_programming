#!/usr/bin/env python3
def add_tuple(tuple_a=(), tuple_b=()):
    return tuple(sum(tuple_a[:2]), sum(tuple_b[:2]), )
