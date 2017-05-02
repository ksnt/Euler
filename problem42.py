#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ksnt

def main():
    f = open("words.txt","r")
    data = f.read()
    data_split = data.split(',')
    str_data = []
    f.close()
    for i in data_split:
        str_data.append(i.strip("\"")) # '"'を取り除く
    result = []
    for i in str_data:
        result.append(sum(map(transfer_word_into_wordvalue, i))) # wordごとのword valueを足して数列をつくる
    tri_num = triange_number(30) # max(result)=192なのでこれくらいの大きさをつくっておけばok
    final_result = []
    for i in tri_num:
        final_result.append(result.count(i)) # result中にtriange_numberがいくつあるか数える
    print sum(final_result) # triangle numberの個数の和をとって、結果を表示
    return sum(final_result)

def transfer_word_into_wordvalue(str):
    """ wordをword valueに変換する関数 A=>1, B=>2, ..."""
    return ord(str)-64
    
def triange_number(n):
    """ n個のtriangle numberの数列を作り出す関数"""
    result = []
    for i in range(1,n):
        result.append(i*(i+1)/2)
    return result

if __name__ == '__main__':
    main()
