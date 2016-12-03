Title: What they didn't teach me in school
Date: 2015-07-26 04:28
Author: Tavish Armstrong
Tags: engineering, school, open source

Mike Hoye has some [good advice][mhoye] for university professors hoping to
incorporate open source development into their courses:

> [W]e’re grateful any effort put in, large or small, to making Firefox better
> and supporting a free and open Web. Only this: there are a couple of things
> that make working with Firefox in an academic context challenging and you
> should be aware of them.

The main problem he talks about is the disconnect between the cadence of the
university project and of an open source release. Sometimes a small bug can
turn into a large one, and open source developers won't merge patches
willy-nilly just to appease an impatient professor. It's hard for developers to
find bugs that will be easily fixed within that short time frame, and it's made
much harder by the lack of warning they're given by professors. His advice is
good, and if you're hoping to unleash a bunch of hapless undergrads onto
an open source project you should follow it.

The post reminded me of a few things that I've been thinking about lately,
especially things that are way harder than I understood when I was in school.

In the case of open source development, I never truly understood what was so
damn hard about it when you're starting out. When I was in first year, I read
a bunch of ideologically-charged essays by Stallman, Doctorow, and friends.
Easy -- just download the source code to an open source project you use. Muck
around with the source code and you'll learn how to code. Before you know it,
you'll be submitting patches. Great. This all sounded reasonable to me back then.
On the internet, no one knows you're a dog, and so I pulled myself onto my hind
legs and compiled `nano` and tried to figure out how the source code worked [^1].
But it never seemed to stick; I didn't actually learn how the internals worked,
I never actually got around to fixing any bugs, and I thought it was all because
I was too dumb to be a developer.

Over the next few years I would occasionally convince myself that I could make
it happen. And it never really did.

Part of the problem was that I didn't really know how to program all that well,
and you need to know how to program pretty well to be able to contribute
anything meaningful to, say, Firefox. Or maybe you don't, but you sure as hell need
to be able to figure out the build system.

But I think you can overcome that, especially if you're brave enough to ask for help
on the internet. The hardest part is that people who run open source projects are
working engineers, and they expect you to also be a working engineer. They expect
you to understand the social norms around software development and to have familiarity
with the tools necessary to keep up with them.

I first started making open source patches when I was an intern at a Drupal
consulting company. Here's [one][drupalpatch]. And that took a lot of hand-holding
from some very good mentors who I am very grateful for. It wasn't just the code
that was hard to figure out. I needed to figure out how to create an actual `.patch`
file. I needed to understand how to interpret test output. And I needed to do all
of the above enough times to appease the reviewers. It takes many different skills
to work with other developers, and it's difficult to learn these skills independently
of the others.

The point about mentors is, I guess, what this whole post is really about. The
thing that has been most useful to me when learning to write software has
been sitting down with someone who is better than me and watching them work.
This is still true today: whenever I can, I try to watch how my peers do their
work and it's staggering how much I can learn in a few minutes. I imagine
some people don't need to watch over other people's shoulders to learn the
trade, but it really works for me.

If I was going to give advice to a more junior developer, I guess it'd be this:
find someone more experienced and try to convince them to let you watch them
work.  Ask questions when you don't understand something. And try to mimic them
when you write software yourself. If you're a more experienced engineer, offer
this to people more junior to you. I know it's hard to work when someone's
looking over your shoulder, but do it anyways.

[mhoye]: http://exple.tive.org/blarg/2015/06/15/september-never-changes/

[^1]: To this day I receive the nano-devel mailing list to my inbox; it baffles
      me that I ever thought this would help launch my open source career.

[drupalpatch]: https://www.drupal.org/node/1260528
