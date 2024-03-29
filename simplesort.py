# -*- encoding: utf-8 -*-
"""
@File    : simplesort.py
@Time    : 2019/9/3 14:57
@Author  : HeKai
@Email   : hek@corp.21cn.com
@Software: PyCharm
"""

def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items