## Code Challenge 05 - Twitter data analysis Part 2: how similar are two tweeters?

Coders Note - My initial implementation had lists of lists generated from get_tweets()call
Problematic for the arcane and black box corpus and vec_bow functions

The Gensim box needs greater amounts of data to provide similarities better than 1.0 or 0.0

Pybites uses tweet_dumper (which can get 3200 tweets per user via api), 
implementing twitterscraper might also be an option in the future. 


Instructions [here](http://pybit.es/codechallenge05.html).

Birds of a feather

A new week, more coding! In Part 2 of our Twitter data analysis we challenge you to find out how similar two tweeters are ...
Challenge

>Make a script that receives two command line args: user1 and user2

>$ similar_tweeters.py bbelderbos pybites
# ... some index of similarity ...

>Get the last n tweets of these users. You can use the code of Part 1.

>Tokenize the words in the tweets, filtering out stop words, URLs, digits, punctuation, words that only occur once or are less than 3 characters (and/or other noise ...)

>Extract the main subjects the users tweet about. You could use Gensim, an NLP package for Topic Modeling. However feel free to take your own approach! We are dropping the helper template and external libs (requirements.txt) for this challenge, we'd love to see different approaches to this problem ...

>Compare the subjects and come up with a similarity score.


Previous challenges and About [here](http://pybit.es/pages/challenges.html).
