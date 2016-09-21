---
title: Human readable base conversion
author: koblas
layout: post
date: 2010-10-04T19:00:02+00:00
url: /p/human-readable-base-conversion/319
aktt_notify_twitter:
  - no
pvc_views:
  - 2595
dsq_thread_id:
  - 161231162
categories:
  - General

---
Code review time&#8230; In a conversation about URL shorteners and &#8220;Coke Rewards&#8221; realized that there was a case where I needed to be able to generate safe character strings that had high reliability for input back by human beings. The typical Base62 systems where there is ambiguity between (O, o and 0) make things hard (along with all of those upper vs. lower case cases).

Here&#8217;s the quick module I put together that is a safe base converter to human readable numbers. 

[code language=&#8221;py&#8221;]
  
import types

class BaseConverter(object):
      
""" Convert a number between two bases of digits, by default it&#8217;s a human safe set 

>>> v = BaseConverter(BaseConverter.BASE10)
      
>>> v.to_decimal(22)
      
22
      
>>> v.from_decimal(22)
      
&#8217;22&#8217;

>>> v = BaseConverter(BaseConverter.BASE2)
      
>>> v.to_decimal(22)
      
Traceback (most recent call last):
          
&#8230;
      
ValueError: character &#8216;2&#8217; not in base
      
>>> v.to_decimal(10)
      
2
      
>>> v.to_decimal(&#8217;10&#8217;)
      
2
      
>>> v.from_decimal(22)
      
&#8216;10110&#8217;

>>> v = BaseConverter()
      
>>> v.to_decimal(22)
      
58
      
>>> v.from_decimal(123123)
      
&#8216;5h17&#8217;
      
>>> v.to_decimal(&#8216;5H17&#8217;)
      
123123

>>> v = BaseConverter(BaseConverter.BASE62)
      
>>> v.from_decimal(257938572394L)
      
&#8216;4XYBxik&#8217;
      
>>> v.to_decimal(&#8216;4XYBxik&#8217;)
      
257938572394

>>> v = BaseConverter(((&#8216;Zero &#8216;,),(&#8216;One &#8216;,)))
      
>>> v.from\_decimal(BaseConverter(BaseConverter.BASE2).to\_decimal(&#8216;1101&#8217;))
      
&#8216;One One Zero One &#8216;

"""

HUMAN_TABLE = (
          
(&#8216;0&#8242;,&#8217;O&#8217;,&#8217;o&#8217;,&#8217;Q&#8217;,&#8217;q&#8217;),
          
(&#8216;1&#8242;,&#8217;I&#8217;,&#8217;i&#8217;,&#8217;L&#8217;,&#8217;l&#8217;,&#8217;J&#8217;,&#8217;j&#8217;),
          
(&#8216;2&#8242;,&#8217;Z&#8217;,&#8217;z&#8217;),
          
(&#8216;3&#8217;,),
          
(&#8216;4&#8217;,),
          
(&#8216;5&#8242;,&#8217;S&#8217;,&#8217;s&#8217;),
          
(&#8216;6&#8217;,),
          
(&#8216;7&#8217;,),
          
(&#8216;8&#8217;,),
          
(&#8216;9&#8217;,),
          
(&#8216;a&#8217;,&#8217;A&#8217;,),
          
(&#8216;b&#8217;,&#8217;B&#8217;,),
          
(&#8216;c&#8217;,&#8217;C&#8217;,),
          
(&#8216;d&#8217;,&#8217;D&#8217;,),
          
(&#8216;e&#8217;,&#8217;E&#8217;,),
          
(&#8216;f&#8217;,&#8217;F&#8217;,),
          
(&#8216;g&#8217;,&#8217;G&#8217;,),
          
(&#8216;h&#8217;,&#8217;H&#8217;,),
          
(&#8216;k&#8217;,&#8217;K&#8217;,),
          
(&#8216;m&#8217;,&#8217;M&#8217;,),
          
(&#8216;n&#8217;,&#8217;N&#8217;,),
          
(&#8216;p&#8217;,&#8217;P&#8217;,),
          
(&#8216;r&#8217;,&#8217;R&#8217;,),
          
(&#8216;t&#8217;,&#8217;T&#8217;,),
          
(&#8216;u&#8217;,&#8217;U&#8217;,&#8217;V&#8217;,&#8217;v&#8217;),
          
(&#8216;w&#8217;,&#8217;W&#8217;,),
          
(&#8216;x&#8217;,&#8217;X&#8217;,),
          
(&#8216;y&#8217;,&#8217;Y&#8217;,),
      
)

BASE2 = "01"
      
BASE10 = "0123456789"
      
BASE62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
      
BASE16 = (
          
(&#8216;0&#8217;,),
          
(&#8216;1&#8217;,),
          
(&#8216;2&#8217;,),
          
(&#8216;3&#8217;,),
          
(&#8216;4&#8217;,),
          
(&#8216;5&#8217;,),
          
(&#8216;6&#8217;,),
          
(&#8216;7&#8217;,),
          
(&#8216;8&#8217;,),
          
(&#8216;9&#8217;,),
          
(&#8216;A&#8217;,&#8217;a&#8217;,),
          
(&#8216;B&#8217;,&#8217;b&#8217;,),
          
(&#8216;C&#8217;,&#8217;c&#8217;,),
          
(&#8216;D&#8217;,&#8217;d&#8217;,),
          
(&#8216;E&#8217;,&#8217;e&#8217;,),
          
(&#8216;F&#8217;,&#8217;f&#8217;,),
      
)

def \_\_init\_\_(self, digitset=HUMAN_TABLE):
          
if type(digitset) in (types.StringType, types.UnicodeType) :
              
self.digitset = [(v) for v in digitset]
          
else :
              
self.digitset = digitset

self.base = len(self.digitset)
          
self.output_map = {}

self.output_digits = [v[0] for v in self.digitset]
          
self.input_set = {}
          
for idx, l in enumerate(self.digitset) :
              
for k in l :
                  
self.input_set[k] = idx

#print &#8216;OUT DIGITS&#8217;, self.output_digits
          
#print &#8216;INPUT SET&#8217;, self.input_set

def from_decimal(self, i):
          
return self.convert(i, self.BASE10, self.output_digits)

def to_decimal(self, s):
          
return int(self.convert(s, self.input_set, self.BASE10))

def convert(self, number, fromdigits, todigits) :
          
fd = fromdigits
          
fbase = self.base
          
if type(fromdigits) in (types.StringType, types.UnicodeType) :
              
fbase = len(fromdigits)
              
fd = dict([(fromdigits[idx], idx) for idx in range(0,len(fromdigits))])

return self._convert(number, fbase, fd, todigits)

@staticmethod
      
def _convert(number, fbase, fromdigits, todigits) :
          
\# Based on http://code.activestate.com/recipes/111286/
          
number = str(number)

if number[0] == &#8216;-&#8216;:
              
number = number[1:]
              
neg = 1
          
else:
              
neg = 0

\# make an integer out of the number
          
x = 0
          
#print "fbase = ", len(fromdigits)
          
for digit in number :
              
try :
                  
x = x * fbase + fromdigits[digit]
              
except KeyError, e:
                  
raise ValueError("character &#8216;%s&#8217; not in base" % digit)

\# create the result in base &#8216;len(todigits)&#8217;
          
tbase = len(todigits)
          
if x == 0:
              
res = todigits[0]
          
else:
              
res = ""
              
while x > 0:
                  
#print "divmod(%d, %d) = %r" % (x, tbase, divmod(x,tbase))
                  
x, digit = divmod(x, tbase)
                  
res = todigits[digit] + res
              
if neg:
                  
res = &#8216;-&#8216; + res
          
return res

binary = BaseConverter(BaseConverter.BASE2)
  
hex = BaseConverter(BaseConverter.BASE16)
  
base62 = BaseConverter(BaseConverter.BASE62)
  
human = BaseConverter()

if \_\_name\_\_ == &#8216;\_\_main\_\_&#8217; :
      
import doctest
      
import random
      
doctest.testmod()
  
[/code]