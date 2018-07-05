#coding:utf-8
import sys
import os
import random
import math
import operator


def loadTrainData():
    '''
    加载数据
    '''
    root = 'D:/'
    # scores = {}

    # for line in open(root + 'ml-20m/genome-scores.csv'):
    # 	(movie_id, tag_id, relevance) = line.split(",")
    # 	if movie_id is None or tag_id is None or relevance is None:
    # 		continue
    # 	scores.setdefault(movie_id, {})
    # 	scores[movie_id][tag_id] = relevance

    # tags = []
    # for line in open(root + 'ml-20m/genome-tags.csv'):
    # 	(tag_id, tag) = line.split(",")
    # 	tags.append((tag_id, tag))

    # movies = []
    # for line in open(root + 'ml-20m/movies.csv'):
    # 	if len(line.split(",")) != 3:
    # 		print line
    # 		continue
    # 	(movie_id, title, genres) = line.split(",")
    # 	movies.append((movie_id, title, genres))


    # user_movie_tag = {}

    # for line in open(root + 'ml-20m/tags.csv'):
    # 	if len(line.split(",")) != 4:
    # 		print line
    # 		continue
    # 	(user_id, movie_id, tag, timestamp) = line.split(",")
    # 	user_movie_tag.setdefault(user_id, {})
    # 	user_movie_tag[user_id][movie_id] = tag

    user_movie_rating = {}
    num = 100000
    for line in open(root + 'ml-20m/ratings.csv'):
        num -= 1
        if num == 0:
            break
        if len(line.split(",")) != 4:
            print line
            continue
        (user_id, movie_id, rating, timestamp) = line.split(",")
        if user_id == 'userId':
            continue
        user_movie_rating.setdefault(user_id, {})
        user_movie_rating[user_id][movie_id] = float(rating)

    return user_movie_rating
    pass


def split_data(data, M, k, seed):
    '''
    将原始数据分割为两份训练数据和测试数据
    :param data:	原始数据集
    :param M:		训练测试数据比
    :param k:		用于生成不同的训练测试数据
    :param seed:	随机种子
    :return:		训练数据、测试数据
    '''
    test = {}
    train = {}
    random.seed(seed)
    ts = 0
    tr = 0
    for user, item in data.items():
        test.setdefault(user, {})
        train.setdefault(user, {})
        for movie, rating in item.items():
            if random.randint(0,M) == k:
                test[user][movie] = rating
                ts += 1
            else:
                train[user][movie] = rating
                tr += 1

    print len(train.keys()), len(test.keys())
    print ts, tr
    return train, test


def recall(train, test, W, N, K):
    '''
    计算推荐算法的召回率
    :param train: 训练数据
    :param test:  测试数据
    :param W: 	  相似度矩阵
    :param N:     top-N推荐
    :param K:     选择最近邻的K个值
    :return:      召回率
    '''
    hit = 0
    all = 0
    for user in train.keys():
        if user not in test: continue
        tu = test[user]
        # print tu
        rank = recommend(user, train, W, N, K)
        # print rank
        for item, pui in rank.items():
            if item in tu:
                hit += 1
        all += len(tu)
    print "hit: %s, all: %s, recall:%s" %(hit, all, hit * 1.0 / all * 1.0)
    return hit * 1.0 / all * 1.0

    pass

def precision(train, test, W, N, K):
    '''
    计算准确率
    :param train: 训练数据
    :param test:  测试数据
    :param W: 	  相似度矩阵
    :param N:     top-N推荐
    :param K:     选择最近邻的K个值
    :return:      准确率
    '''
    hit = 0
    all = 0
    for user in train.keys():
        if user not in test: continue
        tu = test[user]
        rank = recommend(user, train, W, N, K)
        for item, pui in rank.items():
            if item in tu:
                hit += 1
        all += N
    print "hit: %s, all: %s, precision: %s" %(hit, all, hit * 1.0 / all * 1.0)
    return hit * 1.0 / all * 1.0
    pass

def coverage(train, test, W, N, K):
    '''
    计算覆盖率
    :param train: 训练数据
    :param test:  测试数据
    :param W: 	  相似度矩阵
    :param N:     top-N推荐
    :param K:     选择最近邻的K个值
    :return:      覆盖率
    '''
    recommend_set = set()
    all_items = set()
    for user in train.keys():
        for item in train[user].keys():
            all_items.add(item)
        rank = recommend(user, train, W, N, K)
        for item, pui in rank.items():
            recommend_set.add(item)
    print "recommend_set: %s, all_items: %s, coverage: %s" %(len(recommend_set), len(all_items), len(recommend_set) * 1.0 / len(all_items) * 1.0)
    return len(recommend_set) * 1.0 / len(all_items) * 1.0
    pass

def recommend(user, train, W, N, K):
    '''
    推荐算法
    :param user:
    :param train:
    :param W:
    :param N:
    :param K:
    :return:
    '''
    rank = dict()
    interacted_items = train[user]
    for v, wuv in sorted(W[user].items(), key = operator.itemgetter(1), reverse = True)[0:K]:
        for i, rvi in train[v].items():
            if i in interacted_items:
                continue
            rank.setdefault(i, 0)
            rank[i] += wuv * rvi
    result = dict()
    for user, rvi in sorted(rank.items(), key = lambda rank:rank[1], reverse=True)[0:N]:
        result[user] = rvi
    return result
