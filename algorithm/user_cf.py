#coding:utf-8

def user_simlarity(train):
    '''
    传统计算用户相似度算法
    :param train:
    :return:
    '''
    W = dict()
    for each in train.keys():
        for ev in train.keys():
            if each == ev:
                continue
            W[each][ev] = len(train[each] & train[ev])
            W[each][ev] /= math.sqrt(len(train[each]) * len(train[ev]) * 1.0)
    return W

def user_simplarity_1(train):
    '''
    改进的计算用户相似度方法
    :param train:
    :return:
    '''
    item_users = dict()
    for u, item in train.items():
        for i in item.keys():
            if i not in item_users:
                item_users[i] = set()
            item_users[i].add(u)

    C = dict()
    N = dict()

    for i, users in item_users.items():
        for u in users:
            N.setdefault(u, 0)
            N[u] += 1
            C.setdefault(u, {})
            for v in users:
                if u == v:
                    continue
                C[u].setdefault(v, 0)
                C[u][v] += 1

    W = dict()
    for u, related_users in C.items():
        W.setdefault(u, {})
        for v, cuv in related_users.items():
            W[u].setdefault(v, 0)
            W[u][v] = cuv/ math.sqrt(N[u]*N[v])
    return W