import mysql
import mysql.connector as db  # Use library "mysql-connector-python"
import re
import numpy  as np
import pandas as pd
import math

cursor = ''

class DBConnectionError(Exception):
    def __init__(self,n): 
        self.n=n


class SQLQueryError(Exception):
    def __init__(self,n): 
        self.n=n


# The basic function for database connection
# Do not use it directly

def mysql_connection(ip_port, user, passwd, schema):
# ip_port should be like this: ip:port
    global cursor
    ip_port_split = re.search("(.*):(\d*)", ip_port)
    ip   = ip_port_split[1]
    port = ip_port_split[2]

    try:
        connection = db.connect(host=ip, port=port,
                                user=user, passwd=passwd, 
                                db=schema) # specify the schema

        cursor = connection.cursor()
    except mysql.connector.Error as msg: 
        raise DBConnectionError(msg)
    return connection,cursor


# The function for sql query, will produce raw data
# Do not use it directly

def event_query_data(event_type, name, date1, date2):
# input format
# event_type: world,league,all
# name: country name, case insensitive
# date1 & date2: YYYY, YYYY-MM, YYYY-MM-DD
# roubustness: if MM or DD does not meet the requirement, then ignore it

    conn, cur = mysql_connection("localhost:6123", "root", "mysql", "football")
    
    date1_split = re.search("(\d*)-?(\d*)-?(\d*)", date1)
    date2_split = re.search("(\d*)-?(\d*)-?(\d*)", date2)
    
    fuzzy_mark=True
    
    if(len(date1_split[1])!=4 or len(date2_split[1])!=4): raise Exception("Incorrect Date Format!")
    # No need to check "date1_split is None or date_split is None"
    
    date1_query = "'" + date1_split[1]
    date2_query = "'" + date2_split[1]
    
    if(len(date1_split[2])==2 and len(date2_split[2])==2):
        date1_query = date1_query + '-' + date1_split[2]
        date2_query = date2_query + '-' + date2_split[2]
    
    if(len(date1_split[3])==2 and len(date2_split[3])==2):
        date1_query = date1_query + '-' + date1_split[3]
        date2_query = date2_query + '-' + date2_split[3]
        fuzzy_mark=False
    
    if(fuzzy_mark):
        date1_query = date1_query + '%'
        date2_query = date2_query + '%'
    
    date1_query = date1_query + "'"
    date2_query = date2_query + "'"
    
    format_str="""
        SELECT date, home_name, away_name, home_score, away_score, importance, result
        FROM all_event
        WHERE {event_type_sub} (home_name={name} OR away_name={name}) AND 
        (DATE_FORMAT(date, '%Y-%M-%D') BETWEEN {date1} AND {date2})
        ORDER BY date ASC;"""
    # event_type_sub means sub-statement for event_type
    
    if(event_type=="world"): 
        query = format_str.format(event_type_sub="league_mark=0 AND", \
                                    name="'"+name+"'", date1=date1_query, date2=date2_query)
    elif(event_type=="league"):
        query = format_str.format(event_type_sub="league_mark=1 AND", \
                                    name="'"+name+"'", date1=date1_query, date2=date2_query)
    else:
        query = format_str.format(event_type_sub=''                 , \
                                    name="'"+name+"'", date1=date1_query, date2=date2_query)
    
    #print(query) # for debug
    
    try:
        cursor.execute(query)
    except mysql.connector.ProgrammingError as msg:
        raise SQLQueryError(msg)
    
    try:
        results = cursor.fetchall()
    except InterfaceError as msg:
        if(msg=="No result set to fetch from."): return None
    
    df_results = pd.DataFrame(results, columns=["date", "home_name", "away_name", \
                                                "home_score", "away_score", "importance", "result"])
    return df_results

def cal_pts_change(name,x):
    dr = (x[3] - x[4]) / 600 # dr = (home_score - away_score) / 600
    if(name.lower()==x[1].lower()): 
        we = 1 / (1 + math.pow(10, -dr))
        pts_change = x[5] * (x[6] - we)
    else: 
        we = 1 / (1 + math.pow(10,  dr))
        pts_change = x[5] * ( (1 - x[6]) - we)
    return pts_change

global_pts=1150


def cal_pts(pts_change):
    global global_pts
    global_pts += pts_change
    return global_pts


def plot_data(event_type, name, date1, date2):
# input format
# event_type: world,league,all
# name: country name, case sensitive
# date1 & date2: YYYY, YYYY-MM, YYYY-MM-DD
# roubustness: if MM or DD does not meet the requirement, then ignore it
    global global_pts
    
    df_current = event_query_data(event_type, name, date1, date2)
    df_before  = event_query_data(event_type, name, "1000", date1)
    
    df_before["pts_change"] = df_before.apply(lambda x:cal_pts_change(name,x), axis=1)
    df_before["pts"] = df_before.apply(lambda x:cal_pts(x[7]), axis=1)
    
    before_pts = global_pts # store the pts before df_current as we need it
    
    df_current["pts_change"] = df_current.apply(lambda x:cal_pts_change(name,x), axis=1)
    df_current["pts"] = df_current.apply(lambda x:cal_pts(x[7]), axis=1)
    # can directly calculate as we store the last pts in global_pts
    
    # use to extract the last pts, not needed now as we have global_pts
    #before_pts = df_before.tail(1)["pts"] # get the slice of the last row
    #before_pts = before_pts.tolist()[0] # get the value
    
    #display(df_before) # for debug
    #display(df_current) # for debug
    
    df_plot = df_current[["date","pts"]].copy(deep=True)
    #display(df_plot) # for debug
    
    df_plot_before = pd.DataFrame(["Before",before_pts]).T
    df_plot_before.columns = df_plot.columns
    df_plot = pd.concat([df_plot_before,df_plot], ignore_index=True)
    # insert a new line at the beginning of df_plot

    #display(df_plot) # for debug

    return df_plot

#plot_data('all', "scotland", '2012-01', '2015-06') # for debug