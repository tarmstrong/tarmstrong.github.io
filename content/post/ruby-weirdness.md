+++
title = "Time.utc in ruby"
slug = "timeutc-in-ruby"
date = "2016-07-20T20:09:00"
tags = [ "code" ]
+++

A coworker pointed out this strange behaviour in Ruby today:

```
irb(main):003:0> Time.utc(2016, 2, 29)
=> 2016-02-29 00:00:00 UTC
irb(main):004:0> Time.utc(2015, 2, 29)
=> 2015-03-01 00:00:00 UTC
irb(main):005:0> Time.utc(2015, 1, 32)
ArgumentError: argument out of range
	from (irb):5:in `utc'
	from (irb):5
	from /usr/bin/irb:11:in `<main>'
irb(main):006:0> Time.utc(2015, 4, 31)
=> 2015-05-01 00:00:00 UTC
```

Clearly the authors made the effort to stop you from passing in obviously bad values. But I still find it so odd that it rolls over values that are just a little incorrect without telling you.
