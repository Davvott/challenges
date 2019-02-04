from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_N = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open('rss.xml') as f:
        data = [line.strip() for line in f]
    tags = TAG_HTML.findall(''.join(data))
    return tags

def get_top_tags(tags):
    """Get the TOP_N of most common tags
    Hint: use most_common method of Counter (already imported)"""
    count = Counter(tag for tag in tags).most_common(n=TOP_N)
    # count = count.most_common(n=10)
    return count

def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    tag_list = list(product(tags, tags))

    test = SequenceMatcher(None, 'python', 'pythonic').ratio()
    print('\nTest ratio of python and pythonic is: ',  round(test, 3))

    temp = {}
    for tup in tag_list:
        if tup[0][0] != tup[1][0] or tup[0] == tup[1]:
            continue
        else:
            seq = SequenceMatcher(None, tup[0], tup[1]).ratio()
            if seq > SIMILAR:
                temp[tup[0]] = tup[1]
    return temp


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)

    print('* Top {} tags:'.format(TOP_NUMBER))

    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))

    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')

    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
