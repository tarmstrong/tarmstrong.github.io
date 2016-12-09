+++
title = "The Git Harness"
date = "2013-11-24T16:30:00"
tags = [ "coding", "git" ]
+++

Git's usefulness far surpasses the frustration caused by its clunky interface, so I don't like to bash it. It was the first version control system I learned, and I learned it before I could program much more than CS101 assignments. Throughout the years, I've used various languages and various version control systems, but Git is the only one I've used seriously for any amount of time. So not only do I not like to bash it — I lack the perspective necessary for critique.

That said, most people can agree on one thing: the interface sucks. Git is a powerful tool, but it's almost impossible to learn how all the commands and their options work. The arguments have inconsistent orders, and the flags mean different things in different contexts. Some of the commands share duties with others. I've learned to deal with it — it involves reading the man pages every time you want to use `git branch` — but it is a struggle.

Complaining is fun, but it isn't going to get us anywhere —  how do we go about fixing this problem instead? Is the answer a slick GUI like the GitHub desktop client? For some people, sure. But too many GUIs solve the wrong problem: *affordance*.

Affordance is the idea that you should be able to figure out how to use parts of an interface intuitively. Buttons should look like they can be pressed, editable text should look like it can be edited, etc. Command line tools generally solve this problem with man pages and usage messages — and that's a powerful mechanism.

However, it doesn't let you predict the outcome of your actions. Git forces you to have a solid mental model of how a Git history works. You have to understand what the various commands do to that mental model, and be able to simulate a proposed action in your head. Most of us developed this mental model through using Git and making a lot of mistakes.

Practice makes perfect, but there is no virtue in unnecessary struggle. We *could* build a Git interface that helps novices develop their mental models faster, with less pain. We could do it without hiding the complexities of Git, too. And I think we should.

*This* is the Git interface that I would actually want to use:

## The Napkin Sketch

Most people who know how to use Git have a conceptual model of a Git log that looks something like this:

![](/img/git-diagrams/basic-vis.png)

First, you've got the initial state of the repository -- the files that were there when you started. Then you have a set of commits (or "changes") that transform those initial files into what they are today in the `HEAD` version. The state of the working directory is indicated by the `HEAD` ref. In the above diagram, our `HEAD` is pointed at `master`.

If you use Git, you probably understand this. You might visualize it differently — maybe your arrows go the other way, or maybe you like a vertical graph. In any case, this visualization helps you make decisions about what to do next, depending on your goals.

Let's say you have some unstaged changes in your working directory. You start typing `git commit -a`...

![](/img/git-diagrams/adding-a-commit-start-typing.png)

... and when the interface realizes what command you're typing in, it shows you a preview of what will happen if you hit enter. First, it creates a new commit.

![](/img/git-diagrams/adding-a-commit-pre-refmove.png)

And then it updates `master` and `HEAD` to point to it.

![](/img/git-diagrams/adding-a-commit.png)

But you haven't hit enter yet. This lets you understand the change you're about to make. If it's not what you wanted, you have a chance to avoid running that command and having to correct your mistake — which is especially difficult for novices.

Here's another situation. You have a `dev` branch and you want to take a look at the files in it.

![](/img/git-diagrams/basic-branch-vis.png)

You try `git checkout dev`:

![](/img/git-diagrams/checking-out-a-branch-typing.png)

It fades the current `HEAD` and shows you where your new `HEAD` will be after hitting enter. If that's what you want, you can run that command and feel confident you're doing the right thing.

Let's say that you don't want to check it out, though. Instead, you want to merge `dev` into `master`. This is what the preview shows you:

![](/img/git-diagrams/git-merge.png)

Interpreting this is a challenge, and probably gives little solace to a bewildered novice. Once you get over the conceptual hurdles behind Git, though, you can start to experiment a bit, without fear of breaking your repository. It means you can try out a command and figure out for yourself whether it's going to do what you want without having to ask your friend the Git wizard if it's going to break stuff.

This idea reminds me of [figure skating harnesses](http://www.jumpharness.com/skate%20harness%20system.jpg). When you're learning to do a double salchow, your coach will often strap you into one of those. You are then free to throw yourself into the jump without fear of falling on your ass. You get to try things out without suffering the consequences, so that you can develop good habits before it hurts.

With Git, the idea is the same, but instead of falling on your ass,
you're avoiding an hour of sifting through your reflogs.

So: who wants to build the Git harness?
