
#coding:utf-8

def deal_tags():
    root = 'G:/idea-space/ml-20m/'
    file = 'tags.csv'

    user_tags_num = {}
    movie_tags_num = {}
    data = open(root+file).readlines()
    for ev in data:
        tmp = ev.split(",")
        if len(tmp) != 4:
            continue
        user_tags_num.setdefault(tmp[0],0)
        movie_tags_num.setdefault(tmp[1],0)
        user_tags_num[tmp[0]] += 1
        movie_tags_num[tmp[1]] += 1


    user_num = sorted(user_tags_num.items(), key= lambda user_tags_num:user_tags_num[1], reverse=True)
    print user_num[0]
    print user_num[-1]

    movie_num = sorted(movie_tags_num.items(), key= lambda movie_tags_num:movie_tags_num[1], reverse=True)
    print movie_num[0]
    print movie_num[-1]


def deal_ratings():
    root = 'G:/idea-space/ml-20m/'
    file = 'ratings.csv'
    f = open(root+file)
    user_ratings_num = {}
    user_ratings_avg = {}
    movie_ratings_num = {}
    movie_ratings_avg = {}
    for line in open(root+file):
        line = f.readline()
        tmp = line.split(",")

        if tmp[0] == 'userId':continue
        if len(tmp) != 4:
            continue
        user_ratings_num.setdefault(tmp[0],0)
        movie_ratings_num.setdefault(tmp[1],0)
        user_ratings_avg.setdefault(tmp[0],0)
        movie_ratings_avg.setdefault(tmp[1],0)
        user_ratings_num[tmp[0]] += 1
        movie_ratings_num[tmp[1]] += 1
        rating = float(tmp[2])
        user_ratings_avg[tmp[0]] += rating
        movie_ratings_avg[tmp[1]] += rating

    for ev in user_ratings_avg:
        user_ratings_avg[ev] /= user_ratings_num[ev]
    for ev in movie_ratings_avg:
        movie_ratings_avg[ev] /= movie_ratings_num[ev]

    # file = 'user_ratings_avg.csv'
    # f = open(root+file,'w')
    # for key,value in user_ratings_avg.items():
    #     f.write(key+","+str(value) + "\n")
    #
    # file = 'movie_ratings_avg.csv'
    # f = open(root+file,'w')
    # for key,value in movie_ratings_avg.items():
    #     f.write(key+","+str(value) + "\n")

    user_num = sorted(user_ratings_num.items(), key= lambda user_ratings_num:user_ratings_num[1], reverse=True)
    print user_num[0]
    print user_num[-1]
    print len(user_num)

    movie_num = sorted(movie_ratings_num.items(), key= lambda movie_ratings_num:movie_ratings_num[1], reverse=True)
    print movie_num[0]
    print movie_num[-1]
    print len(movie_num)





if __name__ == '__main__':
    # deal_tags()
    deal_ratings()
    pass