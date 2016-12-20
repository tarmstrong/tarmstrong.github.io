+++
title = "The Maeslant Kering: BOS development"
date = "2012-01-31T14:25:00"
tags = [ "code", "engineering", "school" ]
+++

I came across [this
paper](http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.24.5280)
(found via Lambda the Ultimate) on the development of BOS, the control
system for The Maeslant Kering, which is "the movable dam which has to
protect Rotterdam from floodings while, at (almost) the same time, not
restricting ship traffic to the port of Rotterdam". The development team
used formal methods (such as formal models and proofs) to ensure the
quality of the finished product. It's an interesting look at a much
different style of development than the one I'm used to. Whereas most of
my experience is in projects where the requirements remained unknown for
the length of the project and where getting the right design was more
crucial than a controlled development cycle, in the case of BOS figuring
out the requirements (and testing their logical consistency) ahead of
time was worth the cost.

Software Engineering with Formal Methods: The Development of a Storm
Surge Barrier Control System - Seven Myths of Formal Methods Revisited
(2001), by Jan Tretmans, Klaas Wijbrans, Michel Chaudron:

> The control system, called BOS, completely autonomously decides about
> closing and opening of the barrier and, when necessary, also performs
> these tasks without human intervention. BOS is a safety-critical
> software system of the highest Safety Integrity Level according to IEC
> 61508. One of the reliability increasing techniques used during its
> development is formal methods. This paper reports experiences obtained
> from using formal methods in the development of BOS. These experiences
> are presented in the context of Hall’s famous “Seven Myths of Formal
> Methods”.

As far as I can tell, it would be quite difficult to measure the
effectiveness of the formal methods used in this case. The finished
product was remarkably bug-free -- no faults have been found in the
mission-critical subsystems since deployment. But it does seem like an
attractive development model to me. Writing buggy software sucks. It's
annoying, and it's costly. We can't write perfect software, even with
formal methods, but we should work towards writing better software.

Also, it's awesome to see such a badass application of control systems.
If my prof had opened the class with this as an example I would have
been much more interested.