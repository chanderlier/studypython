import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/guonei/index?key=9b38d9d57e0facf1229cf2779012ac41&num=10')
    data_model = json.loads(resp.text)
    print(data_model)
    for news in data_model["newslist"]:
        print(news["title"])


if __name__ == '__main__':
    main()

