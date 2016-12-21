+++
title = "Building for reliability: feature flags"
date = "2016-12-21T00:00:00"
tags = [ "code", "software engineering" ]
+++

A while back I started writing about [everything I learned][bio] before I got my current job. My original intention was to make an exhaustive list of all the random things I learned, and then work through it to figure out which of those skills was essential to my job, which were merely useful for social signaling, and which were merely good for passing interviews. I still want to finish writing that, but I also want to write more about what I've learned since I left school. None of what I've learned is that novel or impressive; I just hope it's useful to students or people who have had different work experience. I also want to write it down to test my own understanding.

Today I'll write about a technique for improving reliability that I learned on the job: feature flags.

Before I start explain what these are, I'll talk a bit about why you would even care about reliability, and in the sorts of situations you might want to use feature flags.

First, context matters and reliability is not inherently virtuous. If you operate an API that delivers cat gifs to clients on request and all the users are hobby projects that can go down without upsetting anyone, you probably don't need to care about reliability that much. If you push a bad commit and take down your site, people will not see cats for a few minutes while you try to fix it. That's probably fine.

There are plenty of situations where you might want to care about reliability. The boring examples involve money: if you go down you don't make money or your customers don't make money. This is a really easy reason to care about reliability because you can trade off software developer time against potential lost money. If you want the dollars lost to go down, you can pay more engineers to make your reliability better [^tradeoffs]. 

[^tradeoffs]: software engineering, like all engineering, is about making tradeoffs. One thing to keep in mind, though, is that no one really knows how to make these tradeoffs with any level of precision. You might think you can dump $X bazillions of dollars of engineering time into making your thing Y% more reliable and then end up with less reliable software because you replaced the database with a crappier database and didn't realize it was going to be crappier until 6 months after you finished your project.

There are more exciting reasons to care about reliability. You might want your software to be reliable if it is important for the medical treatment of people in your hospital. Let's say, for example, that your electronic medical record system helps save X lives per year by being more efficient and less error-prone than the paper-based equivalent. That marginal improvement (X) probably goes away if the system is down for a 48-hours straight at some point in that month because your doctors will have to do more guesswork. This is more important than lost money because lives are on the line; the tradeoff is just harder to make.

Let's talk about a hypothetical example. Let's say I have too many cats and would like to capitalize upon this surplus of fluff. I don't know how to teach these cats how to do my bidding, so I have to capitalize on these cats in some other way. I know one thing: cats love to pose for photos. I have the perfect solution: I develop an API that serves cat gifs in response to payments. This API is adopted by struggling social media apps to keep their user engaged. In exchange for referrals, I give the social media companies a commission on every sale.

Let's say in the begging I started by writing my app in Ruby. I'm pretty comfortable with Ruby, after all, and it made getting set up pretty fast. This Ruby on Rails app talks to another server inside my VPN that operates a remote webcam pointed at these cats. It's going great and the cats are thrilled. Here's what that code looks like:

```ruby
def handle_successful_payment
  client = CatCamClient.new(host: 'https://cats.tavi.sh')
  cat_photo = client.get_cat!
  # return a 200 with the cat!
  [200, cat_photo]
end
```

Unforunately, the masses want more cats from more angles. I make a new backend server that operates multiple cameras: a helmet cam for Alice the cat, a motion-sensing robot camera that follows Bob the cat around, etc. This new server is much more complicated but I've tested it pretty well.

When I switch traffic over to the new backend server, I discover that the database on my cat server is not well indexed, which slows down my API to the point where most requests are timing out. The social networks are now mad at me because the cats were the only reason people were still using their apps, and the cats are mad at me because they want more attention.

```ruby
def handle_successful_payment
  client = CatCamClient.new(host: 'https://fancycats.tavi.sh')
  cat_photo = client.get_cat!
  # return a 200 with the cat!
  [200, cat_photo]
end
```

In future I resolve to do better. The next time I make my change I write some code that looks like this:

```ruby
def handle_successful_payment
  url = if CatApp.flag_on?('fancy_cats')
    'https://fancy-cats.tavi.sh'
  else
    'https://cats.tavi.sh'
  end
  client = CatCamClient.new(host: url)
  cat_photo = client.get_cat!
  # return a 200 with the cat!
  [200, cat_photo]
end
```

In this example, before I make my request to the backend server, I first check to see which backend server to use. To do so, the `CatApp.flag_on?` helper checks the database to see if the confuration flag is on. If so, we use the `https://fancy-cats.tavi.sh` url to fetch a cat.

What does this get me? It means that I no longer need to deploy my code in order to change which backend server my web frontend server is talking to. I can just flip a switch in the database (maybe I'm fancy enough to have an administrative web app for employees where I can put it) and have the new backend run. Now when I run into problems with the backend server being slow, I can immediately fix it without having to write or deploy code. That makes the downtime shorter. Nice!

I could even go one step further and have the flag be a _probability_ rather than a boolean. In that case, I could set the feature flag to only go hit the new backend 10% of the time. That way, if there's a problem with the new backend, I've only broken cats for 10% of people. It's definitely not nice to break things for 10% of people, but I've mitigated a pretty serious failure. In the event of downtime, I lose 90% less money, which makes it easier for me to afford more helmet cams for my cats.

What are some other fun things you can do with feature flags?

* You could profile both paths and figure out which one is faster. That way you can tell whether you are actually making something faster with your new database (instead of trusting the hype). 
  * Github's Scientist library has support for this!
* You can display new features of your product to a smaller portion of your visitors to see whether or not it works well before rolling it out completely.
* You could use feature flags on desktop software (which would probably talk to a server you control) in order to slowly roll out risky changes while mitigating the risk of bricking a few billion dollars worth of computers.

Here are more tips for using feature flags:

* In my example I suggested using a database field to determine whether a flag is on. Using a database can cause you a lot of pain if it shares a database with the rest of your app, because a problematic change to the main app could harm your ability to change the feature flag.
* Adding feature flags makes it harder to write tests, because you now have to test both code paths. Even though the feature flag decreases the risk of your new code path taking down your site, it doesn't help much if the new code path does the same calculation incorrectly. (In the best case scenario, it raises an exception and quits; in the worst, it silently fails while your tests gleefully pass).

There you go: feature flags. They are so much fun!!!

Is there anything I missed out on? Does anybody have great reference implementations that I can look at? Send me emails!
