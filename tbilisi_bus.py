import requests
import xmltodict
import json
from  xml.etree import ElementTree
import xml


def bus_route(id):
    try:
        url = "http://transfer.ttc.com.ge:8080/otp/routers/ttc/routeInfo?routeNumber={}&type=bus&forward=0".format(id)
        headers = {'accept': 'application/xml;q=0.9, */*;q=0.8'}
        resp = requests.get(url=url,headers=headers)

        parse = xmltodict.parse(resp.text)
        str_to_json=json.dumps(parse,indent=4,ensure_ascii=False)
        json_load=json.loads(str_to_json)

        result=[]
        for i in json_load["Route"]["RouteStops"]:
            result.append(i["Name"])
        return result
    except xmltodict.expat.ExpatError:
        return "მარშუტი არ არსებობს"


a=bus_route(73)
print(a)


def bus_time(id):
    try:
        url="http://transfer.ttc.com.ge:8080/otp/routers/ttc/stopArrivalTimes?stopId={}".format(id)
        headers = {'accept': 'application/xml;q=0.9, */*;q=0.8'}
        resp = requests.get(url=url, headers=headers)

        parse = xmltodict.parse(resp.text)
        str_to_json = json.dumps(parse, indent=4, ensure_ascii=False)
        json_load = json.loads(str_to_json)

        result=[]
        for i in json_load["ArrivalTimes"]["ArrivalTime"]:
            text="მარშუტი -> {}, ავტობუსის ნომერი -> {}, მოსვლის დრო -> {} წუთი".format(i['DestinationStopName'],i["RouteNumber"],i["ArrivalTime"])
            result.append(text)
        return result
    except xmltodict.expat.ExpatError:
        return "არ მოიძებნა გაჩერება"
b=bus_time(1113)
print(b)