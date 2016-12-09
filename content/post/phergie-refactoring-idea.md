+++
title = "Phergie refactoring idea"
date = "2012-11-29T14:14:00"
tags = [ "code", "engineering", "The Performance of Open Source Applications" ]
+++

I'm taking a course this semester on software architecture — the high
level design principles that go into building high-quality, maintainable
software. The class is generally pretty decent, but the best part of it
is the project. Over the course of the semester, teams have to learn and
describe the architecture of an open source project; analyze how design
patterns and design principles are applied; critique parts of the
project that could benefit from refactoring; and then actually refactor
the code -- and if you're feeling brave -- submit the change back to the
project.

My group is studying [Phergie](http://phergie.org/), an
[IRC](http://en.wikipedia.org/wiki/Internet_Relay_Chat) bot that can
moderate and perform administrative tasks on IRC channels. It can also
do a few other fun things like pretend to "serve beer" to channel users,
look up documentation for PHP code, etc.

We're encouraged to get on project mailing lists and bug trackers and
introduce ourselves to the developers. I did so and [Matthew
Turland](https://groups.google.com/forum/?fromgroups=#!topic/phergie/pb9IuHdAOhE/discussion)
was kind enough to give us suggestions on how to contribute back to the
project — and even give me feedback on my homework!

I'll post that homework here with some context. The goal is to find a
["code smell"](http://en.wikipedia.org/wiki/Code_smell) or some other
kind of architectural defect; describe it; and then suggest a fix (a
"refactoring"). We're given points for ambition and we don't actually
have to *implement* the change — so we're not limited by our ability to
actually refactor the code.

### Refactoring a large class in Phergie

![Most often changed files. The blue line is the mean and the red line
is one standard deviation above the
mean.](/img/phergie/commits.png)

Figure 1. Most often changed files. The blue line is the mean and the
red line is one standard deviation above the mean.

I began my search for code smells by ranking the files by the number of
commits in the git log that touched each file (see Figure 1.) **(Edit:
This idea comes from Michael Feathers's talk
[here](http://www.youtube.com/watch?v=0eAhzJ_KM-Q) and if you think this
sort of thing is cool, you should read his blog
[here](http://michaelfeathers.typepad.com/).)** The most committed-to
file is also one of the largest at 740 lines of code ---
`Phergie/Driver/Streams.php`, which contains the
`Phergie_Driver_Streams` class. Ostensibly, this class is for handling
the TCP connection to the IRC server. I noticed two things immediately:

1.  `Phergie_Driver_Streams` is the sole child class of
    `Phergie_Driver_Abstract`. In my opinion, this is an
    over-generalization: there appears to be no reason (nor a plan) to
    have a non-streams-based implementation.
2.  `Phergie_Driver_Streams` is not only responsible for handling the
    connection to the server; it is also responsible for parsing and
    formatting IRC commands. The class is so large because it contains
    methods pertaining to both responsibilities, and methods that are
    (arguably) too large because they perform both duties as well.

For 1), the obvious solution is to flatten the hierarchy and use only
the `Streams` class. For 2), my proposed solution is (see the provided
UML diagrams):

1.  Move the parsing logic from `getEvent()` to its own method called
    `parseEvent()`
2.  Move the `parseEvent()` method to a new class called
    `Phergie_IRC_Command_Handler`.
3.  Move the formatting logic from `send()` to its own method called
    `formatCommand()`.
4.  Move the `formatCommand()` method and all methods starting with `do`
    to `Phergie_IRC_Command_Handler`.

My best estimate is that this would split the class into two files with
lengths of approximately 400 lines of code. This is closer to the mean
(227 LOC) and in my opinion much more manageable and understandable ---
each class has more clearly defined responsibility.

![Current architecture of the IRC/TCP subsystem in
Phergie](/img/phergie/refactor-1.png)

Figure 2. Current architecture of the IRC/TCP subsystem in Phergie

![Proposed refactoring of the IRC/TCP subsystem in
Phergie](/img/phergie/refactor-2.png)

Figure 3. Proposed refactoring of the IRC/TCP subsystem in Phergie

### What did the lead Phergie developer think of it?

I
[posted](https://groups.google.com/forum/?fromgroups=#!topic/phergie/pb9IuHdAOhE)
an earlier draft of this to the mailing list and Matthew Turland, the
lead developer responded:

> I agree that Phergie\_Driver\_Streams handling parsing and generation
> of IRC commands is part of why it's so large, which is why I'm moving
> those into separate classes (and even libraries) in Phergie 3. See
> https://github.com/phergie/phergie-irc-parser and
> https://github.com/phergie/phergie-irc-generator. (These also use a
> Phergie\\Irc subnamespace, in anticipation of one or more Jabber
> drivers also being developed.) See also
> https://github.com/phergie/phergie-irc-client-react, which is still
> very much in development but is an example of a driver implementation
> that still makes use of streams, but in a somewhat different way
> (because it uses the React library).

So, that's cool: I accidentally anticipated a change that he had already
made for Phergie 3 (which I didn't realize existed). He decided to split
the new class into a parser and a generator — something I chose not to
do in my report for the sake of simplicity.

I'm also really pleased at how welcoming Matt's been so far; he's
getting practically nothing in return except a bug fix or two (maybe)
and he's still more than willing to take the time to coddle newcomers
like us. What a nice guy!

### What a cool project!

This is a really great idea for a project; although not everyone is
going to feel like sticking their neck out and embarrassing themselves
on the internet like I did, it's still a great opportunity to learn from
more experienced developers and think about theory in the context of
actual software. I certainly learned a lot and had a blast doing it.

Now if only the course also spent some time looking at [more systems, as
described by their developers...](http://aosabook.org)
