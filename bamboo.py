#!/usr/bin/env python3
"""Runs the bamboo integration"""
# -*- coding: utf-8 -*-
import os
from PyBambooHR import PyBambooHR
from utils import get_employee_entry

client = PyBambooHR.PyBambooHR(
    subdomain=os.environ.get('BAMBOOHR_SUBDOMAIN'),
    api_key=os.environ.get('BAMBOOHR_APIKEY'))

report = client.request_company_report(
    os.environ.get('BAMBOOHR_REPORT_ID'),
    report_format='json')

entries = [get_employee_entry(row) for row in report.get('employees', [])]

entries_per_employee = {}

for entry in entries:
    employee_number = entry['employeeNumber']

    if employee_number not in entries_per_employee:
        entries_per_employee[employee_number] = []

    entries_per_employee[employee_number].append(entry)

import pdb; pdb.set_trace()
pass
