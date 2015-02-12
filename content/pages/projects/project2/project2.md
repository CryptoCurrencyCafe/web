Title: Project 2 - Mining Points
Date: 2015-02-10
Category: PS
Tags: Problem Sets, mining
Slug: project1

   <div class="due">
Due: TODO
   </div>

## Purpose

Understand how cryptocurrency mining works by building and running a
miner for a new cryptocurrency.  

Explore some potential threats to bitcoin by attempting attacks on our
class cryptocurrency.

### Collaboration Policy

For Part 1 of this assignment, everyone should create and run their own
PointCoin miner, and writeup their own answers to the questions.

You may, and are encouraged to, discuss all of the problems with anyone
else you want (both on-line using the course web site or any other means
you choose, and in person), and it is okay to share code with others so
long as you understand everything in all of the code you use.

For Part 2, you may work with others in the class (indeed, part of your
goal for part 2 is to form a mining coallition with enough power to
disrupt the normal behavior of the network).  You should not start Part
2 or make any attempts to (intentionally) disrupt the PointCoin network
until the announced starting time for Part 2 (which will be announced
later in class).

# Part 1: Mining PointCoin

<div class="exercise"> **Set up your pointcoind node.** Following the
instructions from [Starting Project
2](|filename|../../../announcements/project2.md), set up your pointcoind
node and wallet.  After finishing this, [post a comment
here](|filename|./pointcoin-nodes.md) with the public IP address of your
EC2 node.  </div>

The main goal for this part is for everyone to write your own PointCoin
miner.  We have provided some code for you to get started:

- [miner.go](TODO:github) - an initial template for a PointCoin miner.
  You will implement your miner by modifying this file.
- [support.go](TODO:github) - some functions that you will find useful
  in implementing your miner.  (You are not expected to change these
  functions, but can change them if you want to.)

Next, we provide some hints that may be helpful in building your miner.

### Coinbase Transaction

Although some people might mine cryptocurrency for purely altruistic
reasons, the main economic incentive for mining is that the miner who
finds a new block can add a transaction to that block transfering the
mining fee to their address.

We have provided the `createCoinbaseTx` function in `support.go` to
create this transaction.  In includes this code for setting up the
inputs and outputs of the transaction:

```go
        tx.AddTxIn(&btcwire.TxIn{
                // Coinbase transactions have no inputs, so previous outpoint is
                // zero hash and max index.
                PreviousOutPoint: *btcwire.NewOutPoint(&btcwire.ShaHash{},
                                                       btcwire.MaxPrevOutIndex),
                SignatureScript: coinbaseScript,
                Sequence:        btcwire.MaxTxInSequenceNum,
        })
        tx.AddTxOut(&btcwire.TxOut{
                Value: blockchain.CalcBlockSubsidy(nextBlockHeight,
                                                   &btcnet.MainNetParams),
                PkScript: pkScript,
        })
```

In PointCoin, the 


# Part 2: Investigating Mining

In the second part of this project, you will explore ways to attack the
PointCoin network.  For this part, you may collude with other students
in the class and use any external resources you want.  

The only rules are:

1. You must disclose honestly everything that you did when you submit
the assignment (and in response to any questions before this).

2. You may not do anything that violates any law or the University honor
code.  This means you should not attempt to log into anyone elses
computer and you should not attempt to distribute malware.

3. You should not do anything a reasonable person would consider
unethical or in violation of the spirit of this assignment.  This is a
very vaugue statement.  What it really means is that if you are
uncertain about whether something you plan to do is consistent with the
spirit of this project, you should consult with Dave before doing it.

Your goal for Part 2 is to acquire ownership of as many PointCoins as
you can.  Your grade for this part will be based on (1) the number of
PointCoins you control (you will prove control over your PointCoins by
transferring them to a given address); and (2) your written description
of the things you tried and what you learned from them.


### Submission

<!-- 
Submit the [Project 1 Submission Form](http://goo.gl/forms/kdIbZ33ryo) (by 11:59pm
on **Friday, 30 January**):

<iframe src="https://docs.google.com/forms/d/1I2a2T9owqTvLx7GAT8EIVf-qAhR2NU2113cSvwVOOAE/viewform?embedded=true" width="760" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>
-->

<p><br></br></p>

<div class="disqus">
<div id="disqus_thread"></div>
</div>
