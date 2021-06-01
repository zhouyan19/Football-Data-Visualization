from django.shortcuts import render
from django.http import JsonResponse
from matplotlib.pyplot import get
from .models import Match
from .matplotlib.draw import getPicture
from django.views.decorators.csrf import csrf_exempt
import mysql
import mysql.connector as db  # Use library "mysql-connector-python"
import re
import json
import numpy as np
import pandas as pd
import math

# cursor = ''


class DBConnectionError(Exception):
    def __init__(self, n):
        self.n = n


class SQLQueryError(Exception):
    def __init__(self, n):
        self.n = n


# The basic function for database connection
# Do not use it directly

def mysql_connection(ip_port, user, passwd, schema):
    # ip_port should be like this: ip:port
    # global cursor
    ip_port_split = re.search("(.*):(\d*)", ip_port)
    ip = ip_port_split[1]
    port = ip_port_split[2]

    try:
        connection = db.connect(host=ip, port=port,
                                user=user, passwd=passwd,
                                db=schema)  # specify the schema

        cursor = connection.cursor()
    except mysql.connector.Error as msg:
        raise DBConnectionError(msg)
    return connection, cursor
# Create your views here.


def json_response(code, data):
    return JsonResponse({'code': code, 'data': data}, status=code)


def home(request):
    if request.method == 'GET':
        e = request.GET.get('event')
        n = request.GET.get('name')
        d1 = request.GET.get('date1')
        d2 = request.GET.get('date2')
        pic_url = getPicture(e, n, d1, d2)
        return json_response(200, {'url': pic_url})
    return json_response(400, {'message': 'Error!'})

@csrf_exempt
def add(request):
    if request.method=='GET':
        # print('receive the request!')
        return json_response(400, {'message': 'CANNOT GET!'})
    if request.method == 'POST':
        # print("receive the post!")
        try:
            body=json.loads(request.body)
            date = body['date']
            home_name = body['home_name']
            away_name = body['away_name']
            home_score = body['home_score']
            away_score = body['away_score']
            tournament = body['tournament']
            league_mark=body['league_mark']

        except:
            return json_response(400, {'message': 'json data not complete!'})
        conn, cur = mysql_connection(
            "localhost:6123", "root", "mysql", "football")
        format_str = """INSERT INTO all_event(date,home_name,away_name,home_score,away_score,tournament,league_mark)
            VALUES ({date}, {home_name}, {away_name}, {home_score},{away_score},{tournament},{league_mark})"""
        format_str = format_str.format(
            date="'"+date+"'", home_name="'"+home_name+"'", away_name="'"+away_name+"'",
            home_score=home_score, away_score=away_score, tournament="'"+tournament+"'",league_mark=league_mark)
        try:
            # 执行sql语句
            cur.execute(format_str)
            conn.commit()
        except:
            conn.rollback()
            return json_response(400, {'message': 'sql Error'})
        return json_response(200, {'message': 'add successfully!'})

@csrf_exempt
def delete_data(request):
    if request.method == 'GET' or 'POST':
        conn, cur = mysql_connection(
            "localhost:6123", "root", "mysql", "football")
        format_str = """
                    SELECT MAX(ID)
                    FROM all_event"""
        try:
            cur.execute(format_str)
        except:
            conn.rollback()
            return json_response(400, {'message': 'sql Error1'})
        maxID = cur.fetchone()[0]
        format_str="DELETE FROM all_event WHERE ID = {maxID};".format(maxID=maxID)
        try:
            cur.execute(format_str)
            conn.commit()
        except:
            conn.rollback()
            return json_response(400, {'message': 'sql Error2'})
        return json_response(200, {'data': "del successfully!"})

@csrf_exempt
def change(request):
    if request.method == 'POST':
        try:
            delete_data(request)
            add(request)
        except:
            return json_response(400, {'message': 'Change Error'})
        return json_response(200, {'message': 'Change success'})

def getOne(request):
    # try:
    #     delete_data(request)
    # except:
    #     return json_response(400,'delete not ok!')
    conn, cur = mysql_connection(
        "localhost:6123", "root", "mysql", "football")
    format_str = """
            SELECT *
            FROM all_event
            ORDER BY ID DESC;"""
    try:
        cur.execute(format_str)
        result=cur.fetchall()
    except:
        conn.rollback()
        return json_response(400, {'message': 'sql Error'})
    return json_response(200, {'data':result})


@csrf_exempt
def search(request):
    if request.method == 'GET':
        conn, cur = mysql_connection("localhost:6123", "root", "mysql", "football")
        try:
            date1 = request.GET.get('date1')
            date2 = request.GET.get('date2')
            name=request.GET.get('name')
            tournament = request.GET.get('tournament')
            result=request.GET.get('result')
        except:
            return json_response(400, {'message': 'json data not complete!'})

        if len(date1)==0:
            date1='1000'
        if len(date2)==0:
            date2='3000'

        fuzzy_mark = True
        date1_split = re.search("(\d*)-?(\d*)-?(\d*)", date1)
        if (len(date1_split[1]) != 4): raise Exception("Incorrect Date Format!")
        date1_query = "'" + date1_split[1]
        if (len(date1_split[2]) == 2):
            date1_query = date1_query + '-' + date1_split[2]
        if (len(date1_split[3]) == 2):
            date1_query = date1_query + '-' + date1_split[3]
            fuzzy_mark = False
        if (fuzzy_mark):
            date1_query = date1_query + '%'
        date1_query = date1_query + "'"

        fuzzy_mark = True
        date2_split = re.search("(\d*)-?(\d*)-?(\d*)", date2)
        if (len(date2_split[1]) != 4): raise Exception("Incorrect Date Format!")
        date2_query = "'" + date2_split[1]
        if (len(date2_split[2]) == 2):
            date2_query = date2_query + '-' + date2_split[2]
        if (len(date2_split[3]) == 2):
            date2_query = date2_query + '-' + date2_split[3]
            fuzzy_mark = False
        if (fuzzy_mark):
            date2_query = date2_query + '%'
        date2_query = date2_query + "'"



        # No need to check "date1_split is None or date_split is None"


        query = "SELECT date, home_name, away_name, home_score,away_score, tournament,result FROM all_event " \
                "WHERE (DATE_FORMAT(date, '%Y-%M-%D') BETWEEN {date1} AND {date2})".format(date1=date1_query, date2=date2_query)
        if len(name)>0:
            query+=" AND (home_name={name} OR away_name={name})".format(name="'"+name+"'")
        if len(tournament)>0:
            query+=" AND tournament={tournament}".format(tournament="'"+tournament+"'")
        if result!='2':
            query+=" AND result={result}".format(result=result)
        # print(query)
        try:
            cur.execute(query)
        except mysql.connector.ProgrammingError as msg:
            raise SQLQueryError(msg)

        try:
            results = cur.fetchall()
            # print(results)
        except Exception as msg:
            if (msg == "No result set to fetch from."): return None

        res_json=[]
        for item in results:
            res_json.append({
                'date':item[0].strftime('%Y-%m-%d'),
                'home_name':item[1],
                'away_name' :item[2],
                'home_score' : item[3],
                'away_score' : item[4],
                'tournament' : item[5],
                'result' : item[6]
            })
        res_json = dict(games=res_json, count=len(res_json))
        # print(res_json)
        return json_response(200, res_json)


@csrf_exempt
def ranking_query_data(request):
    # input format
    # type: world, league, all, fifa, uefa

    rank_type = 'all'
    if request.method == 'GET':
        rank_type = request.GET.get('rank_type')

    conn, cur = mysql_connection("localhost:6123", "root", "mysql", "football")

    if (len(rank_type) != 4):
        # use word length to judge whether is going to use our table or uefa / fifa table
        format_str = """
            SELECT NAME, points
            FROM {rank_type}_country
            ORDER BY points DESC;"""
        query = format_str.format(rank_type=rank_type)

    elif (rank_type == "fifa"):
        query = """
            SELECT TEAM, TOTAL_POINTS
            FROM std_fifa_ranking;"""

    else:
        query = """
            SELECT Country, Pts
            FROM std_uefa_ranking;"""

    # print(query)  # for debug

    try:
        cur.execute(query)
    except mysql.connector.ProgrammingError as msg:
        raise SQLQueryError(msg)

    try:
        results = cur.fetchall()
    except Exception as msg:
        if (msg == "No result set to fetch from."): return None

    df_results = pd.DataFrame(results, columns=["Country", "Points"]).to_dict(orient='index')

    res = []
    for key, value in df_results.items():
        key = int(key) + 1
        res.append({
            'rank': key,
            'name': value['Country']
        })
    
    res = dict(teams=res, count=len(res))
    # print(res)
    return json_response(200, res)

