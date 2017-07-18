#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def run(**kwargs):
    print("[*] In dirlister module.")
    return str(os.listdir("."))
