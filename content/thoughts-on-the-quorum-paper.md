Title: Thoughts on the Quorum paper
Date: 2011-12-04 15:00
Author: Tavish Armstrong
Tags: code, engineering, school, tech, Thoughts

Recently on the ["It Will Never Work In Theory"
blog](http://www.neverworkintheory.org/?p=197) Greg Wilson blogged about
a paper by Andreas Stefik, Susanna Siebert, Melissa Stefik, and Kim
Slattery on "An Empirical Comparison of the Accuracy Rates of Novices
using the Quorum, Perl, and Randomo Programming Languages"
([pdf](http://www.cs.siue.edu/~astefik/papers/StefikPlateau2011.pdf)).
The paper compares Perl, a popular programming language, to two others
created by the researchers. One of the created languages is Quorum, a
language they constructed specifically to be easy to use; and the other
is Randomo, a language they constructed randomly as a "placebo"
language. An empirical study showed that Quorum was significantly easier
to learn than Perl and Randomo. Perl did not perform significantly
better than Randomo, which should surprise anyone who read the paper.
Randomo looks like complete garbage to anyone who knows how to program.
I can make all kinds of jokes about Perl, but to me it looks much better
than Randomo. However, the study showed that a programmer's intuition on
which language is easier to learn is not necessarily correct.

Here's the sample of Perl from the study:

    :::text
    $x = &z(1, 100, 3);
    sub z{
      $a = $[0];
      $b = $[1];
      $c = $[2];
      $d = 0.0;
      $e = 0.0;
      for ($i = $a; $i <= $b; $i++){
        if ($i % $c == 0) {
          $d = $d + 1;
        }
        else {
          $e = $e + 1;
        }
      }
      if ($d > $e) {
        $d;
      }
      else {
        $e;
      }
    }

And here's the Randomo:

    :::text
    ^ Main {
      ~ x \ z(1, 100, 3)
    }
    ^ z(@ a % @ b % @ c) |  ~ {
      ~ d \ 0.0
        ~ e \ 0.0
        @ i \ a
    # (b - a) {
      : i ; c ! 0 {
        d \ d + 1
      }
      , {
        e \ e + 1
      }
      i \ i + 1
    }
    : d ` e {
      d
    }
    , {
      e
    }

If you are new to programming, and I asked you to pick one of the above
languages based on which one you thought would afford you more accuracy,
which one would you choose? I would choose the former, but the results
of the study couldn't determine with stastical significance that it
affords novices any more accuracy.

The resulting discussion on [Hacker
News](http://news.ycombinator.com/item?id=3152147) was pretty sad. I
don't think I saw any outright name-calling, but there were a tonne of
emotionally charged responses that largely ignored the limited scope of
the study. The study was not saying that Perl is a bad language. It was
not saying that you are stupid if you use Perl. It is not even saying
that Perl is a bad language for teaching; other factors like 'how easy
is it to run language X on my computer?' need to be considered before
making such a claim. The point is simple; now we know something more
about the learnability of programming languages. This isn't an anecdote,
and can't be dismissed by a pithy counter-anecdote.

We need more studies like this done, so we can start to talk about
programming languages as if they are tools, not religions.
