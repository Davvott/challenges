## Code Challenge 03 - PyBites blog tag analysis

Instructions [here](http://pybit.es/codechallenge03.html).

<strong> Given our RSS feed what tags does PyBites mostly use and which tags should be merged (based on similarity)?
</strong>

<pre>
$ python tags.py
* Top 10 tags:
python               10
learning             7
tips                 6
tricks               5
github               5
cleancode            5
best practices       5
pythonic             4
collections          4
beginners            4

* Similar tags:
game                 games
challenge            challenges
generator            generators
</pre>
* Hint: for word similarity feel free to use NLTK, or your favorite language processing tool. 
However, stdlib does provide a nice way to do this. Using this method we came to 0.87 as a
 threshold to for example not mark 'python' and 'pythonic' as similar. 
 
Previous challenges and About [here](http://pybit.es/pages/challenges.html).
