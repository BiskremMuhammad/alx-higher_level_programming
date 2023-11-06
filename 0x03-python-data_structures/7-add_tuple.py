#!/usr/bin/env python3
def add_tuple(tuple_a=(), tuple_b=()):
    safe_a = (tuple_a[0] if len(tuple_a) > 0 else 0,
              tuple_a[1] if len(tuple_a) > 1 else 0)
    safe_b = (tuple_b[0] if len(tuple_b) > 0 else 0,
              tuple_b[1] if len(tuple_b) > 1 else 0)
    new_tuple = (safe_a[0] + safe_b[0], safe_a[1] + safe_b[1])
    return new_tuple
