from django.shortcuts import render
from influxdb import InfluxDBClient
from GUISummar.settings import INFLUX_DB
from .utils import Summarizer
import datetime

def SummarView(request):
    http_text=request.POST.get('input_text')
    http_option=request.POST.get('option')
    summary=""
    if http_text and http_option:
        try:
            client = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database=INFLUX_DB)
        except:
            print("Error Occured")
        client.create_database(INFLUX_DB)
        dbs = client.get_list_database()
        if http_option=="1":
            summary,efi=Summarizer(http_text)
        else:
            efi=""
            print("Not valid option")
        time=datetime.datetime.utcnow()
        data = [
        {
            "measurement": "data_table",
            "time": str(time),
            "fields": {
                "http_text": http_text,
                "http_option":http_option,
                "summary":str(summary),
                "Efficiency":str(efi),
            }
        }
        ]
        if summary and efi:
            try:
                client.write_points(data)
                #result = client.query('select * from data_table;')
                #print(result)
            except False:
                print("Error while writing")
    options={"1":"My Summarizer","2":"Not Yet"}
    return render(request, 'dashboard.html',{"options":options,"summary":summary,"input_text":http_text})

    
    
