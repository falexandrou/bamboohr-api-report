#!/usr/bin/env python3
"""Runs the bamboo integration"""
# -*- coding: utf-8 -*-
import os
import csv
import datetime
from PyBambooHR import PyBambooHR
from utils import get_employee_entry, order_employee_entries

CSV_FILE_NAME = os.environ.get('ERP_EXPORT_FILENAME', 'erp-export.csv')

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

for employee_number, entries in entries_per_employee.items():
    entries_per_employee[employee_number] = order_employee_entries(entries)


# Output the file
HEADER_WRITTEN = False

with open(CSV_FILE_NAME, 'w+') as csvfile:
    writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_ALL)

    for _, employee_entries in entries_per_employee.items():
        if not employee_entries:
            continue

        if not HEADER_WRITTEN:
            writer.writerow(employee_entries[0].keys())
            HEADER_WRITTEN = True

        writer.writerows([e.values() for e in employee_entries])

    csvfile.close()

current_date = datetime.datetime.now().strftime('%A %d %B %Y %H:%M:%S')
print(f'[{current_date}] Exported Bamboo HR information')
