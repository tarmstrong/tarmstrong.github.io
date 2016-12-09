+++
title = "How I applied for a job at SeatGeek"
date = "2010-11-21T12:39:00"
tags = [ "code" ]
+++

On Friday I was nerd-sniped by SeatGeek. They're looking for a new
programmer, and instead of going through Monster or other online job
sites, they made their own job application. To apply, you had to hack
into it. I couldn't resist the challenge, even though I'm in school and
I don't need a job.

When you go to [http://apply.seatgeek.com/](http://apply.seatgeek.com/),
you see a message that says:

> This page must be viewed using the SeatGeek browser.

![User agent
challenge](/img/photos/seatgeek/useragent.png)

Websites don't actually test what browser you're using. Your browser
just tells the website what its name is (well, there are probably other
ways to test, but you get the point). When you go to a website in
Firefox, Firefox will happily say "Hey Google, my name is Firefox 3.6 on
Linux!" Your browser is under your control, so you can change this quite
easily (directions are for Firefox):

1.  Open a new tab. Type about:config into the address bar, and hit
    enter.
2.  Search for `useragent`. You'll see a setting called
    `general.useragent.extra.firefox`.
3.  Change the value to "SeatGeek".

Now, if you refresh the page, you'll see the full job application form.

![Full job
application](/img/photos/seatgeek/ignorethis.png)

But wait! There's a problem: "only 'admin' users may submit new
applicants."

This took me about an hour to figure out. First, I viewed source (ctrl-u
on firefox) and saw the following:

    <input name="_csrf" value="this is required (and this value is incorrect)" type="hidden">

They were dropping me pretty big hints here. I tried changing the value
to 'admin' in [Firebug](http://getfirebug.com/), but when I submitted my
application, all I got was a blank page (it was actually a 403 Forbidden
error page).

I tried to remember what CSRF stood for. Ah, right: Cross-Site Request
Forgery. Basically, this is how a lot of phishing works: they put a
login form for GMail on their website that looks a lot like the real
GMail login form, you type in your credentials, and they forward you on
to GMail *after they've read your credentials*. This is why looking at
the address bar and making sure you're on the site you think you're on
is useful.

So, with that in mind, I checked my cookies. This is what I found:

    sg.session=%7B%22admin%22%3A0%2C%22admin%22%3A0%2C%22csrf.token%22%3A%22UMZF2REa8eojqIgxaxI3z8267tcb1b%2F0NzfnNSu2qvQ%3D%22%7D;

If that doesn't make sense to you, you're not alone. But, if you look
closely, you'll notice that "csrf" and "admin" are in there. Aha! We're
getting warmer.

I opened the PHP prompt and URLDecoded the cookie string. (If you don't
know how to do that, go
[here](http://www.string-functions.com/urldecode.aspx).) This is what I
got:

    sg.session={"admin":0,"admin":0,"csrf.token":"UMZF2REa8eojqIgxaxI3z8267tcb1b/0NzfnNSu2qvQ="};

Awesome. When I'm submitting this form, my browser is telling the
website "hey, I'm not an admin (0 is false), and my csrf token is [that
long string of text up there]". This is really bad security, since, as I
said before, you control your browser. So you can tell the website
whatever you want, if you know how to open up your browser. Naturally, I
can [edit my cookie](https://addons.mozilla.org/af/firefox/addon/4510/)
to say `"admin":1` instead. That csrf token is what I want to put into
the HTML input tag I was talking about earlier, like this:

    <input name="_csrf" value="UMZF2REa8eojqIgxaxI3z8267tcb1b/0NzfnNSu2qvQ=" type="hidden">

The reason why websites do this (usually automatically -- they don't
want you to have to edit the HTML to log in!) is so that they know the
login form (or job app form) you're using was authorized by them. The
server knows about that long string of characters, and will make sure
that any job applications include one of these "tokens" they've issued.

Now I could fill out the form and hit submit. And it worked!

![Win!](/img/photos/seatgeek/seatgeek_win.png)

So, there you have it. This is a pretty contrived example of hacking
(they made it easy on purpose), but this is actually how a lot of it
happens. The server expects you to tell the truth, and doesn't have
safeguards in place to make sure you are honest.

Hopefully this has been an interesting look into the world of hacking.
Let me know if you don't understand something. I was trying to make this
somewhat comprehensible for a non-programmer, so if you don't get it,
let me know.

* * * * *

Notes:

1.  The image of the filled-out form doesn't match the image of me being
    successful, since the success image is from when I submitted using
    my real name and resume.
2.  If you're following along, make sure you change your `useragent`
    back to the default, or you'll get funny messages on certain
    websites.

