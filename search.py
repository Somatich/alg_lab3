#!/usr/bin/env python
# -*- coding: utf-8 -*-


def linear_search(data, value):
    for i, v in enumerate(data):
        if v > value:
            return None
        if v == value:
            return i
    return None


def binary_search(data, value):
    # Реализуйте алгоритм здесь
    if len(data) == 0:
        return None
    else:
        mn = 0
        mx = len(data)-1
#        f = False
        while mn<=mx:
            md = mn + (mx - mn)//2
#            print(mn, md, mx)
            if mn == mx and data[mn] != value:
                return None
            else:
                if data[md] == value:
#                    f = True
                    return md
                elif data[md] < value:
                    mn = md+1
                elif data[md] > value:
                    mx = md-1
#a=[]    
#a=[-568585,0,1,2,4,40,234,400,5464,23568,25798669,236776997697,667976896786798,326678968768969876976]
#print(binary_search(a, 400))
