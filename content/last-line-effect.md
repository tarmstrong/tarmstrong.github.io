Title: The Last Line
Date: 2015-05-24 21:42
Author: Tavish Armstrong
Tags: engineering

Greg Wilson posted a [list of papers worth reading][gvwilson-paperlist] from
the 2015 *International Conference on Software Engineering*.  One of the
abstracts that caught my eye was from [*The Last Line Effect*][last-line] [^cite]:

> Abstract: Micro-clones are tiny duplicated pieces of code; they
> typically comprise only a few statements or lines. In this paper,
> we expose the “last line effect,” the phenomenon that the last
> line or statement in a micro-clone is much more likely to contain
> an error than the previous lines or statements. We do this by
> analyzing 208 open source projects and reporting on 202 faulty
> micro-clones.

It might be easier to just look at an example of what they're talking about:

```
x += other.x;
y += other.y;
z += other.y;
```

Here, the last line reads `other.y` instead of `other.z`.

I think this is a great example of the kind of software engineering research
paper I really enjoy. The paper isn't claiming that much: in the software they
studied using their tool, they found a bunch of copy pasta. Among that copy
pasta, they found that the last, er, noodle is more likely to be buggy. 
Many engineers could guess at this result, but having evidence to back up your
anecdote is useful.

The other part that I like is that it's *useful*. Next time
I'm reviewing code, I'm probably going to look more suspiciously at "micro-clones",
and when I do, I'll know where to focus my efforts -- on the last line.


[gvwilson-paperlist]: http://software-carpentry.org/blog/2015/05/icse2015.html
[last-line]: http://www.st.ewi.tudelft.nl/~mbeller/publications/2015_beller_zaidman_karpov_the_last_line_effect_preprint.pdf

[^cite]: Beller, Zaidman, and Karpov, 2015.
