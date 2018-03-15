""""

LLLLLLLLLLL                  UUUUUUUU     UUUUUUUU     NNNNNNNN        NNNNNNNN
L:::::::::L                  U::::::U     U::::::U     N:::::::N       N::::::N
L:::::::::L                  U::::::U     U::::::U     N::::::::N      N::::::N
LL:::::::LL                  UU:::::U     U:::::UU     N:::::::::N     N::::::N
  L:::::L                     U:::::U     U:::::U      N::::::::::N    N::::::N                  uuuuuu    uuuuuu         aaaaaaaaaaaaa
  L:::::L                     U:::::D     D:::::U      N:::::::::::N   N::::::N                  u::::u    u::::u         a::::::::::::a
  L:::::L                     U:::::D     D:::::U      N:::::::N::::N  N::::::N                  u::::u    u::::u         aaaaaaaaa:::::a
  L:::::L                     U:::::D     D:::::U      N::::::N N::::N N::::::N                  u::::u    u::::u                  a::::a
  L:::::L                     U:::::D     D:::::U      N::::::N  N::::N:::::::N                  u::::u    u::::u           aaaaaaa:::::a
  L:::::L                     U:::::D     D:::::U      N::::::N   N:::::::::::N                  u::::u    u::::u         aa::::::::::::a
  L:::::L                     U:::::D     D:::::U      N::::::N    N::::::::::N                  u::::u    u::::u        a::::aaaa::::::a
  L:::::L         LLLLLL      U::::::U   U::::::U      N::::::N     N:::::::::N                  u:::::uuuu:::::u       a::::a    a:::::a
LL:::::::LLLLLLLLL:::::L      U:::::::UUU:::::::U      N::::::N      N::::::::N                  u:::::::::::::::uu     a::::a    a:::::a
L::::::::::::::::::::::L       UU:::::::::::::UU       N::::::N       N:::::::N      ......       u:::::::::::::::u     a:::::aaaa::::::a
L::::::::::::::::::::::L         UU:::::::::UU         N::::::N        N::::::N      .::::.        uu::::::::uu:::u      a::::::::::aa:::a
LLLLLLLLLLLLLLLLLLLLLLLL           UUUUUUUUU           NNNNNNNN         NNNNNNN      ......          uuuuuuuu  uuuu       aaaaaaaaaa  aaaa

https://team.lun.ua/?filtered=vacancies

""""

# -*- coding: utf-8 -*-
# encoding=utf8
import sys
import urllib
import time
import search_console_api as sca
import search_console_sql as scs



def main():
  #to correct using uft-8
  reload(sys)
  sys.setdefaultencoding('utf8')
  #main loop
  while True:
      #connection to mySQL
      db = scs.database_connect()
      #  connect to google api
      if (scs.check_not_downloaded_status() == False):
          continue
      scope = ['https://www.googleapis.com/auth/webmasters.readonly']
      propertyData = scs.choose_property()
      service_account_email = propertyData[1]
      key_file_location = propertyData[2]
      service = sca.get_service('webmasters', 'v3', scope, key_file_location,
        service_account_email)
      #main info to request
      endDate = str(scs.choose_date())
      property_uri = propertyData[0]
      searchType = "web"
      #counter for pagination
      startRowPage = 0
      startRowQuery = 0

      #first request of URLS
      while True:
          response_page = sca.execute_request(service, property_uri, sca.request_page(endDate, searchType, startRowPage))
          #check if response is empty
          if 'rows' not in response_page:
              print ('Empty response. No URLs')
              break
          #creating list of urls to use in 2nd request
          dataPage = sca.parse_table(response_page)

          #pagination
          startRowPage = startRowPage + 5000
          time.sleep(.500)
          dataPageLength = len(dataPage)
          dataPageCurrent = 1
          #second request of Queries
          for dataPageRow in dataPage:
              while True:
                  response = sca.execute_request(service, property_uri,
                                             sca.request_query_by_pages(endDate, searchType, dataPageRow[0], startRowQuery))
                  if 'rows' not in response:
                      print ('Empty response. No queries for this URL')
                      time.sleep(.1)
                      break
                  dataQuery = sca.parse_table(response)

                  #google quotas
                  time.sleep(.1)

                  #insert data in mySQL
                  for dataQueryRow in dataQuery:
                      db = scs.database_connect()
                      cursor = db.cursor()
                      urlp = str(dataPageRow[0]).replace(propertyData[0], "/")
                      url = urllib.unquote(str(urlp)).decode('utf8')
                      url_category_id = scs.get_url_category_id(url)
                      try:
                          cursor.execute(
                              "INSERT INTO search_console_data(date, url, query, clicks, impressions, ctr, position) VALUES(%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE clicks=%s, impressions=%s, ctr=%s, position=%s",
                              (endDate, url, dataQueryRow[0], dataQueryRow[1], dataQueryRow[2], dataQueryRow[3],
                               dataQueryRow[4], dataQueryRow[1], dataQueryRow[2], dataQueryRow[3],
                               dataQueryRow[4]))
                      except scs.my.IntegrityError as e:
                          if not e[0] == 1062:
                              raise
                          else:
                              #print "MY ERROR 1062: " + e[1]
                              pass  # or may be at least log?
                      db.commit()
                      #get categories of URLs
                      try:
                          scs.update_category_id(endDate, url, dataQueryRow[0], url_category_id)
                      except:
                          print "No Category for URL"


                  dataPageCurrent = dataPageCurrent + 1

                  #conditions for pagination for queries
                  if len(dataQuery) < 5000:
                      break
                  elif len(dataQuery) >= 5000:
                      dataPage.append(dataPageRow[0])
                      print ("Data append back")

                  if dataPageLength < dataPageCurrent:
                      startRowQuery = startRowQuery + 5000
                      print ("New start row for URLS")
          db.close()
          #calendar update
          scs.update_date_status(endDate)
          if len(dataPage) < 5000:
              break

if __name__ == '__main__':
  main()
