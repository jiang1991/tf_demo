#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_response(r):
    print('status code: %s, %s \n' % (r.status_code, r.reason))
    # print(r.headers, '\n')
    print(r.json())
