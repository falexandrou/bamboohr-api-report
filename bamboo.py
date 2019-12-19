#!/usr/bin/env python3
"""Runs the bamboo integration"""
# -*- coding: utf-8 -*-
import sys
from bamboo_api import BambooApi

API = BambooApi(subdomain=sys.argv[1], api_key=sys.argv[2])
