"""Bamboo API class"""
# -*- coding: utf-8 -*-
from PyBambooHR import PyBambooHR

class BambooApi:
    """Extracts data from the bamboo api"""
    def __init__(self, subdomain, api_key):
        self.subdomain = subdomain
        self.api_key = api_key
        import pdb; pdb.set_trace()
        self.client = PyBambooHR.PyBambooHR(subdomain=self.subdomain, api_key=self.api_key)

    def get_employees(self):
        """Returns the list of emploeyees available"""
        return self.client.get_employee_directory()
