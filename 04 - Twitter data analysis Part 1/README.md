## Code Challenge 04 - Twitter data analysis Part 1: get the data

Coders note - Some trouble with csv writing and unicode expressions translation. Managed to get aorund it
but it was a little tricky

Instructions [here](http://pybit.es/codechallenge04.html).

## Write a class to retrieve tweets from the Twitter API

In this 3 part challenge you will analyze Twitter Data. 
This week we will automate the retrieval of data. 
In Part 2 we will task you with finding similar tweeters, 
and for Part 3 you will do a full sentiment analysis.

<h2>The challenge</h2>
<ul>
<li>Define a class called UserTweets that takes a Twitter handle / user in its constructor. it also receives an 
optional max_id parameter to start from a particular tweet id.
<li>Create a tweepy API object using the tokens imported from config.py (again, you can use another package 
if you prefer).
<li>Create an instance variable to hold the last 100 tweets of the user.
<li>Implement len() and getitem() magic (dunder) methods to make the UserTweets object iterable.
Save the generated data as CSV in the data subdirectory: 
data/some_handle.csv, columns: id_str,created_at,text
</ul>

<h2>Background</h2>
We posted two articles this week you might find useful in this context: 
    <a href="https://pybit.es/oop-primer.html">
    oop primer</a> and <a href="https://pybit.es/python-data-model.html">
    Python's data model.</a>
    If you decide to use Tweepy, you might want to check its <a href="http://docs.tweepy.org/en/v3.5.0/api.html">
    API reference.</a>

<h2>Tests</h2>

For developers that like to work towards tests we included test_usertweets.py:
<pre>
<code>
$ python test_usertweets.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
</code>
</pre>
<h2>Example output</h2>

We used a namedtuple here, this is not required. Also note the tweets can differ, yet in the unittests we test a fix set (using the optional max_id parameter in the constructor):
<pre><code>
$ python
>>> from usertweets import UserTweets
>>> pybites = UserTweets('pybites')
>>> len(pybites)
100
>>> pybites[0]
Tweet(id_str='825629570992726017', created_at=datetime.datetime(2017, 1, 29, 9, 0, 3), text='Twitter digest 2017 week 04 https://t.co/L3njBuBats #python')
>>> ^D
(venv) [bbelderb@macbook 04 (master)]$ ls -lrth data/
...
-rw-r--r--  1 bbelderb  staff    14K Jan 29 21:49 pybites.csv
(venv) [bbelderb@macbook 04 (master)]$ head -3 data/pybites.csv
id_str,created_at,text
825629570992726017,2017-01-29 09:00:03,Twitter digest 2017 week 04 https://t.co/L3njBuBats #python
825267189162733569,2017-01-28 09:00:05,Code Challenge 03 - PyBites blog tag analysis - Review https://t.co/xvcLQBbvup #python
</code></pre>

Previous challenges and About [here](http://pybit.es/pages/challenges.html).
