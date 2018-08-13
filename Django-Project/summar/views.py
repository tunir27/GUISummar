from django.shortcuts import render
from influxdb import InfluxDBClient
from GUISummar.settings import INFLUX_DB,AUTO_SUMMARY_TIME,AUTO_SUMMARY_ALGO
from .utils import Summarizer
import datetime


from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.summarizers.kl import KLSummarizer
#from sumy.summarizers.reduction import ReductionSummarizer

from sumy.evaluation import rouge_n

options={"My Summarizer","Sumy Lsa","Sumy Lex Rank","Sumy Text Rank","Sumy Luhn","Sumy Edmundson","Sumy KL"}


def SummarView(request):
    http_text=request.POST.get('input_text')
    http_option=request.POST.get('option')
    http_sen=request.POST.get('sen')
    summary=""
    exsum=""
    LANGUAGE = "english"
    if http_sen:
        SENTENCES_COUNT = http_sen
    else:
         SENTENCES_COUNT = 10
    rouge="0"
    if http_text and http_option:
        try:
            client = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database=INFLUX_DB)
        except:
            print("Error Occured")
        client.create_database(INFLUX_DB)
##        result=client.query('select text from xml_data where time > now() - 30m;')
##        text=list(result.get_points(measurement='xml_data'))
##        for i in range(len(texst)):
##            http_text=http_text+str(text[i]['text'])
##        print(http_text)
        #dbs = client.get_list_database()
        if http_option=="My Summarizer":
            exsum,efi=Summarizer(http_text)
            reference = PlaintextParser.from_file("C:\\Users\\42wol\\Desktop\\ITRA\\GUISummar\\Django-Project\\summar\\reference_summary.txt", Tokenizer(LANGUAGE)).document.sentences
            candidate = PlaintextParser.from_string(exsum, Tokenizer(LANGUAGE)).document.sentences
            #print(exsum)
            rouge=rouge_n(candidate, reference, 2)
            print(http_option)
            print("Rouge score for n=2",rouge)
        elif http_option=="Sumy Lsa":
            # or for plain text files
            parser = PlaintextParser.from_string(http_text, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = LsaSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            summary=summarizer(parser.document, SENTENCES_COUNT)
            reference = PlaintextParser.from_file("C:\\Users\\42wol\\Desktop\\ITRA\\GUISummar\\Django-Project\\summar\\reference_summary.txt", Tokenizer(LANGUAGE)).document.sentences
            #print(summary)
            rouge=rouge_n(summary, reference, 2)
            print(http_option)
            print("Rouge score for n=2",rouge)
        elif http_option=="Sumy Lex Rank":
            parser = PlaintextParser.from_string(http_text, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = LexRankSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            summary=summarizer(parser.document, SENTENCES_COUNT)

            reference = PlaintextParser.from_file("C:\\Users\\42wol\\Desktop\\ITRA\\GUISummar\\Django-Project\\summar\\reference_summary.txt", Tokenizer(LANGUAGE)).document.sentences
            #print(summary)
            rouge=rouge_n(summary, reference, 2)
            print(http_option)
            print("Rouge score for n=2",rouge)
        elif http_option=="Sumy Text Rank":
            parser = PlaintextParser.from_string(http_text, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = TextRankSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            summary=summarizer(parser.document, SENTENCES_COUNT)
            reference = PlaintextParser.from_file("C:\\Users\\42wol\\Desktop\\ITRA\\GUISummar\\Django-Project\\summar\\reference_summary.txt", Tokenizer(LANGUAGE)).document.sentences
            #print(summary)
            rouge=rouge_n(summary, reference, 2)
            print(http_option)
            print("Rouge score for n=2",rouge)
        elif http_option=="Sumy Luhn":
            parser = PlaintextParser.from_string(http_text, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = LuhnSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            summary=summarizer(parser.document, SENTENCES_COUNT)
            reference = PlaintextParser.from_file("C:\\Users\\42wol\\Desktop\\ITRA\\GUISummar\\Django-Project\\summar\\reference_summary.txt", Tokenizer(LANGUAGE)).document.sentences
            print(summary)
            rouge=rouge_n(summary, reference, 2)
            print(http_option)
            print("Rouge score for n=2",rouge)
        elif http_option=="Sumy Edmundson":
            parser = PlaintextParser.from_string(http_text, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = EdmundsonSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            summary=summarizer(parser.document, SENTENCES_COUNT)

            reference = PlaintextParser.from_file("C:\\Users\\42wol\\Desktop\\ITRA\\GUISummar\\Django-Project\\summar\\reference_summary.txt", Tokenizer(LANGUAGE)).document.sentences
            #print(summary)
            rouge=rouge_n(summary, reference, 2)
            print(http_option)
            print("Rouge score for n=2",rouge)
        elif http_option=="Sumy KL":
            parser = PlaintextParser.from_string(http_text, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = KLSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            summary=summarizer(parser.document, SENTENCES_COUNT)
            reference = PlaintextParser.from_file("C:\\Users\\42wol\\Desktop\\ITRA\\GUISummar\\Django-Project\\summar\\reference_summary.txt", Tokenizer(LANGUAGE)).document.sentences
            #print(summary)
            rouge=rouge_n(summary, reference, 2)
            print(http_option)
            print("Rouge score for n=2",rouge)

##        elif http_option=="Sumy Reduction":
##            parser = PlaintextParser.from_string(http_text, Tokenizer(LANGUAGE))
##            stemmer = Stemmer(LANGUAGE)
##
##            summarizer = ReductionSummarizer(stemmer)
##            summarizer.stop_words = get_stop_words(LANGUAGE)
##
##            summary=summarizer(parser.document, SENTENCES_COUNT)




    time=datetime.datetime.utcnow()
    if not exsum:
        for sentence in summary:
            exsum=exsum+" "+str(sentence)
    data = [
    {
        "measurement": "data_table",
        "time": str(time),
        "fields": {
            "http_option":http_option,
            "summary":str(exsum),
            "Efficiency":str(rouge),
        }
    }
    ]
    if exsum and rouge:
        try:
            client.write_points(data)
            result = client.query('select * from data_table;')
            print(result)
        except False:
            print("Error while writing")
    return render(request, 'dashboard.html',{"options":options,"summary":exsum,"input_text":http_text})

    
    
def DSummarView(request):
    http_text=''
    http_option=request.POST.get('option')
    http_sen=request.POST.get('sen')
    summary=""
    exsum=""
    LANGUAGE = "english"
    if http_sen:
        SENTENCES_COUNT = http_sen
    else:
         SENTENCES_COUNT = 10
    rouge="0"
    if http_option and http_sen:
        try:
            client = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database='kml1')
        except:
            print("Error Occured")
        client.create_database('kml1')
        
        result = client.query('select * from kml_data;')
        for i in result.get_points(measurement='kml_data'):
            if i['Text']:
                http_text+=" "+i['Text']+". "
        print(http_text)
##        result=client.query('select text from xml_data where time > now() - 30m;')
##        text=list(result.get_points(measurement='xml_data'))
##        for i in range(len(texst)):
##            http_text=http_text+str(text[i]['text'])
##        print(http_text)
        #dbs = client.get_list_database()
        if http_option=="My Summarizer":
            exsum,efi=Summarizer(http_text)
            reference = PlaintextParser.from_file("C:\\Users\\42wol\\Desktop\\ITRA\\GUISummar\\Django-Project\\summar\\reference_summary.txt", Tokenizer(LANGUAGE)).document.sentences
            candidate = PlaintextParser.from_string(exsum, Tokenizer(LANGUAGE)).document.sentences
            #print(exsum)
            rouge=rouge_n(candidate, reference, 2)
            print(http_option)
            print("Rouge score for n=2",rouge)
        elif http_option=="Sumy Lsa":
            # or for plain text files
            parser = PlaintextParser.from_string(http_text, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = LsaSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            summary=summarizer(parser.document, SENTENCES_COUNT)
            reference = PlaintextParser.from_file("C:\\Users\\42wol\\Desktop\\ITRA\\GUISummar\\Django-Project\\summar\\reference_summary.txt", Tokenizer(LANGUAGE)).document.sentences
            #print(summary)
            rouge=rouge_n(summary, reference, 2)
            print(http_option)
            print("Rouge score for n=2",rouge)
        elif http_option=="Sumy Lex Rank":
            parser = PlaintextParser.from_string(http_text, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = LexRankSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            summary=summarizer(parser.document, SENTENCES_COUNT)

            reference = PlaintextParser.from_file("C:\\Users\\42wol\\Desktop\\ITRA\\GUISummar\\Django-Project\\summar\\reference_summary.txt", Tokenizer(LANGUAGE)).document.sentences
            #print(summary)
            rouge=rouge_n(summary, reference, 2)
            print(http_option)
            print("Rouge score for n=2",rouge)
        elif http_option=="Sumy Text Rank":
            parser = PlaintextParser.from_string(http_text, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = TextRankSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            summary=summarizer(parser.document, SENTENCES_COUNT)
            reference = PlaintextParser.from_file("C:\\Users\\42wol\\Desktop\\ITRA\\GUISummar\\Django-Project\\summar\\reference_summary.txt", Tokenizer(LANGUAGE)).document.sentences
            #print(summary)
            rouge=rouge_n(summary, reference, 2)
            print(http_option)
            print("Rouge score for n=2",rouge)
        elif http_option=="Sumy Luhn":
            parser = PlaintextParser.from_string(http_text, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = LuhnSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            summary=summarizer(parser.document, SENTENCES_COUNT)
            reference = PlaintextParser.from_file("C:\\Users\\42wol\\Desktop\\ITRA\\GUISummar\\Django-Project\\summar\\reference_summary.txt", Tokenizer(LANGUAGE)).document.sentences
            print(summary)
            rouge=rouge_n(summary, reference, 2)
            print(http_option)
            print("Rouge score for n=2",rouge)
        elif http_option=="Sumy Edmundson":
            parser = PlaintextParser.from_string(http_text, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = EdmundsonSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            summary=summarizer(parser.document, SENTENCES_COUNT)

            reference = PlaintextParser.from_file("C:\\Users\\42wol\\Desktop\\ITRA\\GUISummar\\Django-Project\\summar\\reference_summary.txt", Tokenizer(LANGUAGE)).document.sentences
            #print(summary)
            rouge=rouge_n(summary, reference, 2)
            print(http_option)
            print("Rouge score for n=2",rouge)
        elif http_option=="Sumy KL":
            parser = PlaintextParser.from_string(http_text, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = KLSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            summary=summarizer(parser.document, SENTENCES_COUNT)
            reference = PlaintextParser.from_file("C:\\Users\\42wol\\Desktop\\ITRA\\GUISummar\\Django-Project\\summar\\reference_summary.txt", Tokenizer(LANGUAGE)).document.sentences
            #print(summary)
            rouge=rouge_n(summary, reference, 2)
            print(http_option)
            print("Rouge score for n=2",rouge)

##        elif http_option=="Sumy Reduction":
##            parser = PlaintextParser.from_string(http_text, Tokenizer(LANGUAGE))
##            stemmer = Stemmer(LANGUAGE)
##
##            summarizer = ReductionSummarizer(stemmer)
##            summarizer.stop_words = get_stop_words(LANGUAGE)
##
##            summary=summarizer(parser.document, SENTENCES_COUNT)




    time=datetime.datetime.utcnow()
    if not exsum:
        for sentence in summary:
            exsum=exsum+" "+str(sentence)
    data = [
    {
        "measurement": "data_table",
        "time": str(time),
        "fields": {
            "http_option":http_option,
            "summary":str(exsum),
            "Efficiency":str(rouge),
        }
    }
    ]
    if exsum and rouge:
        try:
            client.write_points(data)
            result = client.query('select * from data_table;')
            print(result)
        except False:
            print("Error while writing")
    
    return render(request, 'dashboard_auto.html',{"options":options,"summary":exsum})



def ParameterView(request):
    http_blevel=request.POST.get('blevel')
    http_lsummary=request.POST.get('slength')
    http_window=request.POST.get('window')
    try:
        client = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database='kml1')
    except:
        print("Error Occured")
    time=datetime.datetime.utcnow()
    data = [
    {
        "measurement": "parameter_table",
        "time": str(time),
        "fields": {
            "blevel":http_blevel,
            "lsummary":http_lsummary,
            "window":http_window,
        }
    }
    ]
    if http_blevel and http_lsummary and http_window:
        client.query('drop measurement parameter_table')
        client.write_points(data)
    return render(request, 'parameter_page.html')


def Auto_SummaryView(request):
    http_utc1=request.POST.get('utc1')
    http_utc2=request.POST.get('utc2')
    if http_utc1 and http_utc2:
        try:
            client = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database='kml1')
        except:
            print("Error Occured")

        utc1=datetime.datetime.strptime(http_utc1,'%Y-%m-%dT%H:%M:%SZ')
        utc2=datetime.datetime.strptime(http_utc2,'%Y-%m-%dT%H:%M:%SZ')
        
        squery='select summary from auto_summary where time > '+ "'"+str(utc1)+"'" + ' and time < '+ "'"+str(utc2)+"'" + ';'
        #print(squery)
        result=client.query(squery)
        text=list(result.get_points(measurement='auto_summary'))
        #print(text[0]['summary'])
        summary=[]
        cluster=[]
        cluster_center=[]
        s={}
        c=[]
        c_c=[]
        temp=[]
        #print("Length",len(eval(str(text))))
        #print(text)
        print("==============================")
        for i in range(len(eval(str(text)))):
            x=eval(text[i]['summary'])
            for j in x:
                #print(j)
                s['cluster']=j[0]
                s['sumy']=j[1].strip()
                s['cluster_center']=j[2]
                s['time']=text[i]['time']
                temp.append(s)
                s={}
            summary.append(temp)
            temp=[]
##                s.append(j[1].strip())
##                c.append(j[0])
##                c_c.append(j[2])
##
##            summary.append(s)
##            cluster.append(c)
##            cluster_center.append(c_c)
##            c=[]
##            s=[]
##            c_c=[]

        #print(summary)
##        print(cluster)
##        print(cluster_center)
            
        
        if summary:
            return render(request, 'auto_summary_utc.html',{"summary":summary,"cluster":cluster,"cluster_center":cluster_center})
        else:
            exsum='No data found please try other timestamps'
            return render(request, 'auto_summary_utc.html',{"summary":summary})
    return render(request, 'auto_summary_utc.html')
