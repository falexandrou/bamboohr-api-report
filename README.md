# BambooHR API Report

This small Python app, uses the BambooHR API to export reports as CSV files

### Installation
To install the app, enter the directory you cloned this repository in and simply run:

```
pip install . 
```

### Usage
To run the app, you need to create an API key in BambooHR and the following environment variables:

- `BAMBOOHR_SUBDOMAIN` - The subdomain for your BambooHR organization (eg. use `my-awesome-company` if you're using `my-awesome-company.bamboohr.com`)
- `BAMBOOHR_APIKEY` - The API key to use
- `BAMBOOHR_REPORT_ID` - The ID of the report to export


### References
- [How to issue an API Key in BambooHR](https://documentation.bamboohr.com/docs#authentication)
- [BambooHR API Reference](https://documentation.bamboohr.com/reference/)
- [Who am I](https://www.falexandrou.com/)

### License
This software is provided without any warranty, under the MIT license
