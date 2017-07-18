#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def run(**kwargs):
    print("[*] In environment module.")
    return str(os.environ)
