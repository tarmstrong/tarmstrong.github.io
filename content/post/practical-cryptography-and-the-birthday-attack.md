+++
title = "Practical Cryptography and the Birthday Attack"
date = "2011-02-06T14:31:00"
tags = [ "books", "code", "tech" ]
+++

The other day I took *Practical Cryptography* out of the library. In
this slim book, Bruce Schneier and Niels Ferguson cover what you need to
know about cryptography so you don't shoot yourself in the foot. So far
I've only read the part on basic cryptographic theory, where they
discuss basic functions (authentication, encryption, signing), and basic
attacks (chosen plaintext, meet-in-the-middle and birthday).

The second attack I mentioned -- the Birthday Attack -- is really neat,
because it's based on the equally neat Birthday Paradox, which I will
explain: Consider a room of 23 people. What is the likelihood that two
people in that room will have the same birthday? Turns out it's 50%.
There are 253 pairs you can make with 23 people [1], and the likelihood
that a single pair share the same birthday is 1/356. Multiply 253 by
1/356 and you get the probability of two people in a room of 23 people
having the same birthday.

How can we apply this to cryptography? Well, if there are 256 different
values a cryptographic key can take on [2], that means you only need to
try around 17 of them to find two that are the same. That means if
you're listening to two computers send cryptographically signed messages
to each other, and every time they send a message they use a different
key, you only need to wait for around 17 messages to be sent before you
find one that has been signed with a key that was used to sign an
earlier message. Basically, you can repeat old messages and the
receiving computer will think they are legitimate. If you saved a "pay
$10 to user X" message, you can make the receiving computer pay user X
$10. This is bad news.

This is why it's important to use long cryptographic keys -- they can
take on more values, and decrease the collision rate. Keys need to be
long enough to evade not only current attacks, but the attacks of 50
years from now. However, size doesn't matter as much as correct use of
cryptography. A long key that doesn't need to be attacked is about as
useless as a wall that blocks half of a castle from attack. And that is
what this book is about. I'll let you know how it is when I'm done.

[1] Protip: google "23 choose 2" and it will calculate this for you.

[2] This means an 8-bit key. Don't use 8-bit keys.
