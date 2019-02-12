import os, sys, re, pprint
from string import punctuation
from gensim import models
from gensim import similarities
from gensim import corpora
from collections import defaultdict
import logging

from usertweets_help import UserTweets

# punctuation = '!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'
regex_punc = re.compile('[%s]' % re.escape(punctuation))  # re.escape all chars in pattern
IS_LINK_OBJ = re.compile(r'^(?:@|https?://)')  # re.search( returns T/F
stoplist = set('for a of the and to in'.split())


def similar_tweeters(primary, *users):
    """ :params: must be string of handle for twitterer
        "user1" = the vec_bow to be compared against all other users
    """

    data = []

    for i, user in enumerate([*users]):  # [*args] unpacks but not list(*args)
        data.append(get_tweets(user))  # Concat lists, not append [] != [[]]
        # data = data + [li for li in (get_tweets(user))]


    save_corpus('all', data)
    dictionary, corpus = load_corpus('all')

    tokens = []
    tokens = tokens + (get_tweets(primary))  # vec_bow needs strings

    # Similariites
    lda = models.ldamodel.LdaModel(corpus, num_topics=5, id2word=dictionary)
    index = similarities.MatrixSimilarity(lda[corpus])

    vec_bow = dictionary.doc2bow(tokens)
    vec_lda = lda[vec_bow]

    sims = index[vec_lda]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])

    for i, sim in sims:
        print([*users][i], sim)

    pass

def get_tweets(user):
    # UserTweets creates 'user'.csv file in data folder
    user_Tweet= UserTweets(user)
    user_tweets = user_Tweet._tweets  # Tweet attr

    # Alternative - Tweet_dumper - saves to csv, read from and append words

    # Convert _tweets attr
    tweets = [[str(regex_punc.sub('', word)) for word in tweet.text.split()
               if word not in stoplist]
             for tweet in user_tweets]

    # Count tweets
    frequency = {}
    for tweet in tweets:
        for token in tweet:
            if token not in frequency:
                frequency[token] = 1
            else:
                frequency[token] += 1

    # Filter out one-off words

    tweets = [' '.join(word.lower() for word in tweet
              if frequency[word] > 1 and len(word) > 2
              and 'http' not in word and not word.isdigit())
             for tweet in tweets]


    final_tweets = []

    # final_tweets = final_tweets + [tweet_li for tweet_li in tweets]

    return tweets

def save_corpus(handle, texts):
    """ :param: texts; list of words"""
    cwd = os.path.abspath('.')
    dictionary = corpora.Dictionary(texts)
    dictionary.save('{}\data\{}.dict'.format(cwd, handle))
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('{}\data\{}.mm'.format(cwd, handle), corpus)

def load_corpus(file_name):
    cwd = os.path.abspath('.')
    if (os.path.exists("{}\data\{}.dict".format(cwd, file_name))):
        dictionary = corpora.Dictionary.load("{}\data\{}.dict".format(cwd, file_name))
        corpus = corpora.MmCorpus('{}\data\{}.mm'.format(cwd, file_name))
        return dictionary, corpus
    else:
        return False

def tweet_exists(user_handle):
    cwd = os.path.abspath('.')
    if (os.path.exists('{}\data\{}.csv').format(user_handle)):
        return True
    else:
        return False

similar_tweeters('pybites', 'bbelderbos', 'talkpython')

#
# if __name__ == "__main__":
#
#     # similar_tweeters(user1, user2)
#
#
#     if len(sys.argv) > 1:
#         primary = sys.argv[1]
#     else:
#         primary = 'bbelderbos'
#     if len(sys.argv) > 2:
#         diff_users = sys.argv[1:]
#
#     # Compile data list for all other users
#     data = []
#     for user in diff_users:
#         data = data + (get_tweets(user))
#     dictionary = corpora.Dictionary(data)
#     corpus = [dictionary.doc2bow(text) for text in data]
#
#     # Similariites
#     lda = models.ldamodel.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)
#     index = similarities.MatrixSimilarity(lda[corpus])
#
#     # Get
#     tokens = get_tweets(primary)
#     vec_bow = dictionary.doc2bow(tokens)
#     vec_lda = lda[vec_bow]
#
#     sims = index[vec_lda]
#     sims = sorted(enumerate(sims), key=lambda item: -item[1])
#     for i, sim in sims:
#         print(diff_users[i], sim)
#
