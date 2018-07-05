#coding:utf-8
import math
import operator

def item_similarity(train):
    '''
    计算物品相似度算法
    :param train:
    :return:
    '''
    C = dict()
    N = dict()
    for u, items in train.items():
        for i in items:
            N.setdefault(i,0)
            C.setdefault(i,{})
            N[i] += 1
            for j in items:
                C[i].setdefault(j,0)
                if i == j:
                    continue
                C[i][j] += 1
    W = dict()
    for i, related_items in C.items():
        W.setdefault(i,{})
        for j, cij in related_items.items():
            W[i].setdefault(j,0)
            W[i][j] = cij / math.sqrt(N[i] * N[j])
    return W

def item_recommendation(user, train, W, N, K):
    '''
    基于物品的协同过滤推荐
    :param user:
    :param train:
    :param W:
    :param N:
    :param K:
    :return:
    '''
    rank = dict()
    interacted_items = train[user]
    for i, rvi in train[v].items():
        for v, wuv in sorted(W[user].items(), key = operator.itemgetter(1), reverse = True)[0:K]:
            if v in interacted_items:
                continue
            rank.setdefault(v, 0)
            rank[v] += wuv * rvi
    result = dict()
    for item, rvi in sorted(rank.items(), key = lambda rank:rank[1], reverse=True)[0:N]:
        result[item] = rvi
    return result