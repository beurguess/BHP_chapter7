#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def run(**kw):
    print("[*] In environment module.")
    return str(os.environ)
