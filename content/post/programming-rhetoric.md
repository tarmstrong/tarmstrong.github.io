+++
title = "Programming as argument"
date = "2015-05-09T14:26:00"
tags = [ "code", "engineering", "writing" ]
+++


Many people before me have argued that computer programs are secondarily about
making a machine perform a task and primarily about telling other humans what
you want the computer to do. Pseudocode takes this to the extreme --
humans can discuss what a pseudocode program *would* do and whether or not it
would be a good idea, without ever running the code on a computer.  The
pseudocode program is an argument -- it argues that a program could be
constructed to accomplish the task at hand. The problem with pseudocode
is *not* that it doesn't run on a computer. The problem with pseudocode is that it has no
way of convincing you that it would work if it *did* run on a computer.

The reason why a pseudocode program of any respectable size is not a convincing
argument is probably obvious to anyone who writes software for a living: it's
easy to write code that looks plausible to other humans, but unless you run
the program, it's hard to believe that it will actually work. Software that is easy to
run is more convincing because you can watch it work. You provide inputs, it
provides outputs. You can do this to prove or disprove hypotheses. In this case, though,
the code stops being an argument that a program *could* be constructed to perform
a task (as is the case with pseudocode). Instead, it becomes an argument that
the compiled program will perform the task correctly. Testing the program manually
is one way of convincing yourself that it will do that. But it is only one way.

An automated testing framework can be useful for making your code more convincing.
You can show that given *this* input and *that* input, the program will produce
the correct output. Other programmers can run the tests and feel more confident
that the program will behave that way.

A few arguments are implicit in every test: these fake inputs are
representative of real inputs. This is an accurate simulation of global state.
These expected outputs are the *correct* outputs.  When you use mocks or stubs
in your tests, you argue that the dependencies you are simulating
actually behave that way; a common mistake is over-mocking dependencies so much
that you have to just *trust* that the code will work when connected to real dependencies.
For example, if your tests don't open a socket
to a functioning server, can you really be sure that the code will do so correctly in
production?  If you can't, you have to *trust* that the networking code works. The
argument becomes "*if* we assume the networking code exists, the following code
will write this message over the socket." That *if* might be a very big *if*.

Code review makes this argumentation-model-of-programming more obvious. If you
write useless tests, a reviewer will often tell you that they are terrible
tests.  The point they are making is *not* that your code doesn't work.  The
point is that they have little reason to believe it will. They have not been
convinced by your argument.

If code is an argument, what does that mean for working programmers?  Well, it
means that the rules of rhetoric apply when writing software. If you want your
code to be merged, or you want your project to be adopted, you need it to be
[persuasive][influence].  This raises an important question: is *persuasive*
code the same thing as *good* code?



[influence]: http://en.wikipedia.org/wiki/Robert_Cialdini


