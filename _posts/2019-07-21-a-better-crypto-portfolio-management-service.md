---
layout: post
title:  "A better crypto portfolio service"
date: 2019-07-21 21:36:45 +0200
categories:
  - software
---
I started to make a crypto portfolio management application from scratch. Not
because there are not enough services already, there are a lot of them actually.
But none of them can make me 100% satisfied: there always seems to be something
missing. After being waiting and thinking about it for two years, I have decided
this is the time to make one of my own. Hopefully more people can find it
useful.

Another "minor" reason for it is that I want to build a web service from scratch
using Scala and React, but let's skip that for now :P

## Who is this service for?
People who is not professional trader, but quite active in trading compares to
average users. Typically there is about 2 to 5 transactions per month. Most of
the trades are just buy and hodl. For example, buy Bitcoin and hodl it for
longer than 2 years. They would like to pay monthly instead of yearly.

## Simple ROI?
Both Delta and Cryptocompare portfolio couldn't get my total fiat ROI right. I
am not sure why. But the plan is just to treat all exchanges and wallets as one
blackbox, counts the fiat that went in and how much all the crypto worth at the
moment. And probably you should be able to get the ROI for a certain time
period.

## Tracking ICOs
Some portfolio services support monitoring crypto wallets, but I haven't found
any service that can figure out if a transaction is ICOs or not yet. So what you
see in the transactions is that some coins, usually ETH, disappeared and after
fews days some other coins show up. Made it very difficult to track ROI.

## Tracking transactions among exchanges and wallets automatically
Since I usually start my trade from an exchange that accept fiat deposit, buy
some BTC and move on to some other exchange, I really want to know which
transaction is going to which exchange. You could do that manually of course.
But wouldn't it be great if the system is smart enough to figure that out?

## Other things I am not so happy with
* Duplicated transactions. Perhaps can be fixed by simply introducing an
  external id for each transaction.
* User experience. Service like CoinTracker requires user to manually click
  refresh button every time I update transactions. This should happens
  automatically. Details, just details.
* Would be great to have both web and mobile services. It's kinda of hard to add
  new transactions on a small device.

## Other Crypto Portfolio I have tried
* CoinTracker (Great features, bad UX, expensive for none professional traders.
  No monthly option)
* Delta (Great UI, good features, expensive for the features it offers. No web service.)
* Cyptocompare Portfolio (Limited features, cannot really track your ROI. Free)
