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
  - Development
tags:
  - python

---
Code review time&#8230; In a conversation about URL shorteners and &#8220;Coke Rewards&#8221; realized that there was a case where I needed to be able to generate safe character strings that had high reliability for input back by human beings. The typical Base62 systems where there is ambiguity between (O, o and 0) make things hard (along with all of those upper vs. lower case cases).

Here&#8217;s the quick module I put together that is a safe base converter to human readable numbers. 

```python

import types

class BaseConverter(object):
    """ Convert a number between two bases of digits, by default it’s a human safe set

    >>> v = BaseConverter(BaseConverter.BASE10)
    >>> v.to_decimal(22)
    22
    >>> v.from_decimal(22)
    ’22’

    >>> v = BaseConverter(BaseConverter.BASE2)
    >>> v.to_decimal(22)
    Traceback (most recent call last):
    …
    ValueError: character ‘2’ not in base
    >>> v.to_decimal(10)
    2
    >>> v.to_decimal(’10’)
    2
    >>> v.from_decimal(22)
    ‘10110’

    >>> v = BaseConverter()
    >>> v.to_decimal(22)
    58
    >>> v.from_decimal(123123)
    ‘5h17’
    >>> v.to_decimal(‘5H17’)
    123123

    >>> v = BaseConverter(BaseConverter.BASE62)
    >>> v.from_decimal(257938572394L)
    ‘4XYBxik’
    >>> v.to_decimal(‘4XYBxik’)
    257938572394

    >>> v = BaseConverter(((‘Zero ‘,),(‘One ‘,)))
    >>> v.from_decimal(BaseConverter(BaseConverter.BASE2).to_decimal(‘1101’))
    ‘One One Zero One ‘

    """

    HUMAN_TABLE = (
        (‘0′,’O’,’o’,’Q’,’q’),
        (‘1′,’I’,’i’,’L’,’l’,’J’,’j’),
        (‘2′,’Z’,’z’),
        (‘3’,),
        (‘4’,),
        (‘5′,’S’,’s’),
        (‘6’,),
        (‘7’,),
        (‘8’,),
        (‘9’,),
        (‘a’,’A’,),
        (‘b’,’B’,),
        (‘c’,’C’,),
        (‘d’,’D’,),
        (‘e’,’E’,),
        (‘f’,’F’,),
        (‘g’,’G’,),
        (‘h’,’H’,),
        (‘k’,’K’,),
        (‘m’,’M’,),
        (‘n’,’N’,),
        (‘p’,’P’,),
        (‘r’,’R’,),
        (‘t’,’T’,),
        (‘u’,’U’,’V’,’v’),
        (‘w’,’W’,),
        (‘x’,’X’,),
        (‘y’,’Y’,),
    )

    BASE2 = "01"
    BASE10 = "0123456789"
    BASE62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    BASE16 = (
        (‘0’,),
        (‘1’,),
        (‘2’,),
        (‘3’,),
        (‘4’,),
        (‘5’,),
        (‘6’,),
        (‘7’,),
        (‘8’,),
        (‘9’,),
        (‘A’,’a’,),
        (‘B’,’b’,),
        (‘C’,’c’,),
        (‘D’,’d’,),
        (‘E’,’e’,),
        (‘F’,’f’,),
    )

    def __init__(self, digitset=HUMAN_TABLE):
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

        #print ‘OUT DIGITS’, self.output_digits
        #print ‘INPUT SET’, self.input_set

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
        # Based on http://code.activestate.com/recipes/111286/
        number = str(number)

        if number[0] == ‘-‘:
            number = number[1:]
            neg = 1
        else:
            neg = 0

        # make an integer out of the number
        x = 0
        #print "fbase = ", len(fromdigits)
        for digit in number :
            try :
                x = x * fbase + fromdigits[digit]
            except KeyError, e:
                raise ValueError("character ‘%s’ not in base" % digit)

        # create the result in base ‘len(todigits)’
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
            res = ‘-‘ + res
        return res

binary = BaseConverter(BaseConverter.BASE2)
hex = BaseConverter(BaseConverter.BASE16)
base62 = BaseConverter(BaseConverter.BASE62)
human = BaseConverter()

if __name__ == ‘__main__’ :
    import doctest
    import random
    doctest.testmod()
```
