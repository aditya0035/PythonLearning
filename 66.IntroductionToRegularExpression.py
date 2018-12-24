"""
Regular expression is a language not programming language
it has keyword and syntex which tell what we want
in regular expression first we have to find the  generic pattern
In regular expression we define a pattern for which we are looking for
to deal with regular expression in python we have Re module which provide various function
to work with Regular Expression in Regular Expression we have following Syntex/Keywords
--Regular Expression is written in formal language that can be interpreted by regular expression processor
--RE is wild form of search of specific pattern
--It Reduce the code and based on character
Below are the characters with there meaning
1.^ it tell start with(Matching the start of line)
2.$ it tell ends with(matching the end of line)
3..(dot):Matches any character(number,letter,white space) except new line
4.\s matches white space
5.\S matches any non-white space
6.*(star) Repeat a character zero or more number of time occurrence
7.*?(star with question mark) Repeat a character zero or more times with out a greedy match
8.+(plus) Repeat a character one or more times
9.+?(plush with question mark) Repeat a character one or more time without greedy match
10.?(Question Mark) limit Zero or one of
11.[abc] matches a string contains either a,b,c  so Matches a single character in the list
12.[^xyz] matches a string in which characters are not in x,y or z so matches a single character not in the list
13.[a-z 0-9] the set of character can include a-z or 0-9 range
14.(abc) Refer as group here ( represent from where to start the extraction of string and ) tells where to stop the
extraction of string in order to fetch the group
15.(abc)? it check if that group is occurred zero or one time
16.[A-Z \.]+ here it will check for A-Z and contains a . as .(dot) is a special character in regular expression
but in order to include that in part of pattern search we have to escape that using \
"""
'''
More About Regular expression
1. Regular expression is not global module but it comes with python installation so we need to import that using
import re
2. we will use re.search(pattern,string) method to check if that string contains the pattern it check if
match found it will return true else return false its similar to find method of string
3.We can use re.finall() to find all the occurrence of that pattern in the string
its like combination of find and slicing of string

Depending on how clean our data is and based on application type we need to narrow down the our pattern search
'''

