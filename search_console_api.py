# -*- coding: utf-8 -*-
# encoding=utf8
# module with requests and connections to google api console, requests execution and parsing

import random
import time
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
import httplib2


#get google service
def get_service(api_name, api_version, scope, key_file_location,
                service_account_email):
  credentials = ServiceAccountCredentials.from_p12_keyfile(
    service_account_email, key_file_location, scopes=scope)
  http = credentials.authorize(httplib2.Http())
  service = build(api_name, api_version, http=http)
  return service

#first request to download urls
def request_page(endDate, searchType, startRow):
    request = {
        'startDate': endDate,
        'endDate': endDate,
        'dimensions': ['page'],
        'searchType': searchType,
        'rowLimit': 5000,
        'startRow': startRow
    }
    print (request)
    return request

#second request to download queries of urls from 1st request
def request_query_by_pages(endDate, searchType, url, startRow):
    request = {
        'startDate': endDate,
        'endDate': endDate,
        'dimensions': ['query'],
        'searchType': searchType,
        "dimensionFilterGroups": [
            {
                "filters": [
                    {
                        "dimension": 'page',
                        "expression": url
                    }
                ]
            }
        ],
        'rowLimit': 5000,
        'startRow': startRow
    }
    print (request)
    return request

#executing google api request
def execute_request(service, property_uri, request):
    while True:
        for n in range(5, 7):
            try:
                return service.searchanalytics().query(
                    siteUrl=property_uri, body=request).execute()
            except HttpError, error:
                print error.resp.reason
                if error.resp.reason in ['userRateLimitExceeded', 'dailyLimitExceeded402',
                                         'internalServerError', 'backendError', 'rateLimitExceeded', 'unknown', 'quotaExceeded']:
                    print ("Google Error")
                    print error.resp.reason
                    time.sleep((2 ** n) + random.random())
                elif error.resp.status in [500, 404, 503, 403]:
                    print ("Google Error")
                    print error.resp.status
                    time.sleep((2 ** n) + random.random())
                else:
                    print ("An HTTP error %d occurred:\n%s" % (error.resp.status, error.content))
                    print ("There has been an error, the request never succeeded.")
                    break


#reading of google api answer
def parse_table(response):
  if 'rows' not in response:
    print 'Empty response 3'
    return

  data = []
  for row in response['rows']:
      data.append(
          [
              row['keys'][0],
              row['clicks'],
              row['impressions'],
              row['ctr'],
              row['position']
          ]
      )
  return data
