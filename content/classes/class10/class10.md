Title: Class 10: More Mining
Date: 2015-02-16

## Schedule 

   <div class="todo"> 

- [Project 2](|filename|../../pages/projects/project2/project2.md), Part 1 is due **Sunday, 22 February**.  Part 2 will begin afte class on Monday, 23 February and is due on Thursday, 5 March.

- Start (continue!) thinking of ideas for your final project.  I've posted a few starting ideas [on the course site](|filename|../../pages/ideas.md).  The first major deliverable for the final project will be a project proposal (due **20 March**)

- Reading: finish reading through [_Chapter 8: Mining and Consensus_](https://github.com/aantonop/bitcoinbook/blob/develop/ch08.asciidoc).

   </div>

<center> 
<iframe src="//www.slideshare.net/slideshow/embed_code/44794648" width="476" height="400" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>
</center>
<div class="caption">Note: due to a bug in
slideshare's updated player, ink markings no longer appear in the
viewer.  <br>If you [download the slides](|filename|./class10-inked.pptx), they are present though.
Hopefully, the player will be fixed someday. </div>
</center>

# Final Project

Your main assignment after finishing Project 2 will be an open-ended
project.  You can work on anything you want that is related to
cryptocurrency (loosely defined), so long as you can convince me it will
be interesting and worthwhile.  My hope is everyone will do a project
that will have significant value beyond just our class.

You can work alone or in a team of any size.  The impressiveness of your
project should scale with the size of your team (but not linearly, since
there is added communication overhead as your team size increases).  It
should scale as at least <span class="math">_N_<sup>2/3</sup></span>
where <span class="math">_N_</span> is the number of students in the
course on your team.  (You are welcome to enlist help from people not in
the class, and they don't count towards your <span
class="math">_N_</span> value.)

# Forking PointCoin

What causes a blockchain to fork?
<div class="gap">

</div>

If all the trans-pacific network cables (there are [only about
12](http://www.submarinecablemap.com/)) were cut, what would happen to
the bitcoin blockchain?
<div class="gap">

</div>

# Asymptotic Analysis

When is asymptotic analysis useful?
<div class="gap">
</div>

When is asymptotic analysis useless?
<div class="gap">
</div>

The measured time to compute one SHA-256 hash on my EC2 node (2.5 GHz
processor) is 750 ns.  Approximately how many instructions execute to
compute on SHA-256 hash?
<div class="gap">

</div>

# Mining Cost

**Assumption.** SHA-256 produces a uniform random output.  (We know this
  is not really true, but it is a reasonable approximation, and
  necessary for the analysis.)  So, we can model SHA-256 on any (new)
  input <span class="math">_x_</span> as drawing randomly from 2<sup>256</sup> possible outputs:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SHA-256(<span class="math">_x_) &larr; [0, 2<sup>256</sup>)

<span class="math">Target = T<sub>max</sub> / Difficulty</span>  
<span class="math">T<sub>max</sub> = (2<sup>16</sub> – 1)2<sub>256<sub> &approx; 2<sub>224</sub>

Current (15 Feb) Bitcoin Difficulty = 44,455,415,962

```Python
>>> target = 2 ** 224 / 44455415962
606449092506427232846302685260647042725721699378946247123L
>>> success_probability = target / 2**256
5.237396582969569e-21
>>> expected_hashes = 1 / success_probability
1.9093455768686638e+20
>>> nanos_needed = expected_hashes * 760
>>> seconds_needed = nanos_needed / 10**9
145110263842018.44
>>> days = seconds_needed / (60 * 60 * 24)
1679516942.6159542
>>> years = days / 365
4601416.2811396
>>> years * 2
~ 9.2 M years to find one block on EC2 (assuming difficulty doesn’t increase)
```

# Energy

Why is energy/hash so much less for custom ASICs? 
<div class="gap">

</div>

In an ASIC, it is possible to build an XOR using 4 transistors.  How
many transistors have to flip to do an XOR on a general purpose
processor like an Intel i7?
<div class="gap">

</div>

[Mining Hardware](https://en.bitcoin.it/wiki/Mining_hardware_comparison)
- current ASIC miners achive >5 Billion hashes per seconds and over 1500
Million hashes per Joule (the energy required to lift an apple one
meter).

[_Inside a Chinese Bitcoin Mine_](http://www.thecoinsman.com/2014/08/bitcoin/inside-chinese-bitcoin-mine/), The Coinsman, 11 August 2014.

> The first thing you notice as you approach the warehouse is the noise. It begins as soon as you step out of the car, at which point it sounds like massive swarm of angry bees droning away somewhere off in the distance. It becomes louder and louder the closer you get to the building, and as you step through the doors it becomes a deafening and steady roar...

Estimate for total energy use of bitcoin network with current hashrate:
```Python
>>> expected_hashes
1.9093455768686638e+20
>>> hashes_per_second = expected_hashes / 600
3.18224262811444e+17
>>> # according to blockchain.info: 309,384,699.96 GH/s
>>> 309384699.96 * 10**9
3.0938469996e+17
>>> _ / hashes_per_second
0.9722222222361415
>>> Mhash_per_J = 1500
>>> Mhash_per_second = hashes_per_second / 10**6
>>> J = Mhash_per_second / Mhash_per_J
212149508.54096264
```
212 MJ per second = 212 MW

Our nearest nuclear plant, the [North Anna Power
Station](https://www.dom.com/corporate/what-we-do/electricity/generation/nuclear/north-anna-power-station)
(Lake Anna) generates 1892 MW, "enough to power 450,000 homes" or about
9x the amount needed to power the current bitcoin network (only counting
the miners themselves; additional power needed for cooling, etc.)

How does the energy use of bitcoin compare to what is used by the
current financial infrastructure for comparable service?  (This is a
very difficult question to answer, would be a good project idea, not
something to answer in the blank below!)

<div class="gap">

</div>
