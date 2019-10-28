import json
import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sqlalchemy import create_engine


def frame_to_json(frame):
    j_table = []
    for index, row in frame.iterrows():
        j_row = {'id': index}
        for col in frame.columns:
            j_row[col] = row[col]
        j_table.append(j_row)
    return {"table": j_table}


@api_view(["GET", "POST"])
def query(request):
    con = create_engine("mssql+pyodbc://denstreamsets:Grande16@densql")
    if request.method == 'GET':
        sql = 'SELECT * FROM LACT.dbo.ComparisonWater'
        df = pd.read_sql(sql, con)
        data = frame_to_json(df) 
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        return JsonResponse('pass', safe=False)


@api_view(["POST"])
def func1(request):
    try:
        body = json.loads(request.body)
        return JsonResponse(f'This is the body: {body}' ,safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def func2(request):
    try:
        body = json.loads(request.body)
        return JsonResponse(f'This is the body: {body}' ,safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
