#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def run(**kwargs):
    print("[*] In dirlister module.")
    return str(os.listdir("." if not 'path' in kwargs.keys() else kwargs['path']))
