# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json

class BaiduTranslate:
    appid = ''  # 填写你的appid
    secretKey = ''  # 填写你的密钥
    httpClient = None


    def __init__(self, appid, secretKey):
        self.appid = appid
        self.secretKey = secretKey


    def translate(self,q):
        myurl = '/api/trans/vip/translate'

        fromLang = 'auto'  # 原文语种
        toLang = 'zh'  # 译文语种
        salt = random.randint(32768, 65536)
        q = q
        sign = self.appid + q + str(salt) + self.secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + self.appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            print (result)
            return result['trans_result'][0]['dst']
        except Exception as e:
            print (e)
        finally:
            if httpClient:
                httpClient.close()