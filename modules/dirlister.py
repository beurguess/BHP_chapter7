#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def run(**kw):
    print("[*] In dirlister module.")
    return str(os.listdir("."))
