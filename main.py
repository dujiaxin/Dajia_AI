# coding=utf-8

from baiduTransAPI import *
from sys import argv
from os.path import exists
import time
import unicodedata

def formateDajia(sentence):
    sentence = unicodedata.normalize('NFKC', sentence)
    sentence = sentence.replace("。"," ")
    return sentence


if __name__ == '__main__':
    script, from_file, to_file = argv
    print(f"Reading from {from_file}  the result will be saved to {to_file}")
    if exists(to_file):
        print(f"The file {to_file} already exits, do you want to overwrite?")
        print("Ready, hit RETURN to overwrite, CTRL-C to abort.")
        input()

    appid = ''  # 填写你的appid
    secretKey = ''  # 填写你的密钥
    baidu = BaiduTranslate(appid,secretKey)

    with open(to_file,'w') as file_translated:
        with open(from_file) as f:
            read_data = f.read()
            lines = read_data.split('\n\n')
            for line in lines:
                qs = line.split("\n")
                if(len(qs)>3):
                    qs[2] = qs[2] + " " + qs[3]
                time.sleep(1)#you can change this if you can use higher version
                translated_q = baidu.translate(qs[2])
                formated_q = formateDajia(translated_q)
                file_translated.write(qs[0]+'\n'+qs[1]+'\n'+formated_q+'\n'+qs[2]+'\n\n')

