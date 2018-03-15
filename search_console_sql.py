# -*- coding: utf-8 -*-
# encoding=utf8
# module with mysql connections, selections, updates

import MySQLdb as my

def database_connect():
    db = my.connect(host="127.0.0.1",
                    user="user",
                    passwd="password",
                    db="DataBase",
                    charset="utf8",
                    use_unicode=True
                    )
    db.autocommit = True
    return db


#choosing date from calendar
def choose_date():
    db = database_connect()
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql = "SELECT MIN(id), date, status FROM search_console_calendar WHERE status = 'not downloaded'"
    print (sql)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            sc_date = row[1]
            status = row[2]
            # Now print fetched result
            print ("id=%d,sc_date=%s,status=%s" % \
                  (id, sc_date, status))
            db.close()
            print (sc_date)
            return sc_date
    except:
        print ("Error: unable to fecth data")
        db.close()


#update downloaded status when all data downloaded from SC for this day
def update_date_status(endDate):
    db = database_connect()
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to UPDATE required records
    sql = "UPDATE search_console_calendar SET status = 'downloaded' WHERE date = '%s' LIMIT 1" % (endDate)
    print sql
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()

    
#choose SC API data
def choose_property():
    db = database_connect()
    cursor = db.cursor()
    sql = "SELECT * FROM search_console_property WHERE id = 1"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            property_uri = row[1]
            service_account = row[2]
            key_file = row[3]
            # Now print fetched result
            print ("id=%d,property_uri=%s,service_account=%s,key_file=%s" % \
                  (id, property_uri, service_account, key_file))
            db.close()
            print (property_uri)
            return property_uri, service_account, key_file
    except:
        print ("Error: unable to fecth data")
        db.close()


#check if not all data was downloaded for this day in SC
def check_not_downloaded_status():
    db = database_connect()
    cursor = db.cursor()
    not_downloaded_count = 0
    try:
        sql_not_downloaded_check = "SELECT COUNT(*) FROM search_console_calendar WHERE status='not downloaded'"
        cursor.execute(sql_not_downloaded_check)
        not_downloaded_check = cursor.fetchall()
        for row in not_downloaded_check:
            not_downloaded_count = row[0]
    except:
      print ("Error: unable to fetch data")
    db.close()
    if (not_downloaded_count == 0):
        return False


def get_site_url():
    db = database_connect()
    cursor = db.cursor()
    sql_get_site_url = "SELECT url FROM site_url_data"
    site_url_list = []
    try:
        cursor.execute(sql_get_site_url)
        site_url = cursor.fetchall()
        site_url_list = [list(i) for i in site_url]
    except:
        print ("Error: unable to fetch data")
    db.close()
    return site_url_list

def get_url_category_id(url):
    db = database_connect()
    cursor = db.cursor()
    sql_get_url_category_id = "SELECT category_id FROM site_url_data WHERE url = \"" + url + "\""
    url_category = 0
    try:
        cursor.execute(sql_get_url_category_id)
        url_category_id = cursor.fetchall()
        for row in url_category_id:
            url_category = row[0]
    except:
        print ("Error: unable to fetch data")
    db.close()
    return url_category

def update_category_id(endDate, url, query, category_id):
    print category_id
    db = database_connect()
    cursor = db.cursor()
    sql_update_category_id = "UPDATE search_console_data SET category_id = %s WHERE url = '%s'" % (category_id, url)
    print sql_update_category_id
    try:
        # Execute the SQL command
        cursor.execute(sql_update_category_id)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    # disconnect from server
    db.close()
