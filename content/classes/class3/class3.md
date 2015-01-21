Title: Class 3: Eliptic Curves
Date: 2014-01-21

## Schedule 

   <div class="todo">
[Project 1](|filename|../../pages/projects/project1/project1.md) is due **Friday, 30 January**.

Before the next class (Monday, Jan 26): **Read:** Satoshi Nakamoto,
[_Bitcoin: A Peer-to-Peer Electronic Cash
System_](https://bitcoin.org/bitcoin.pdf), 2008.  The is the original
bitcoin paper </div>

<!--
<center> <iframe
src="//www.slideshare.net/slideshow/embed_code/43552674" width="476"
height="400" frameborder="0" marginwidth="0" marginheight="0"
scrolling="no"></iframe><br> 
<div class="caption"> Note: due to a bug in
slideshare's updated player, ink markings no longer appear in the
viewer.  <br>If you download the slides, they are present though.
Hopefully, the player will be fixed someday.  </div>

</center>
-->

### Asymmetric Cryptosystems Recap

For asymmetric cryptography, we need a one-way function with a trapdoor:
a function that can be easily inverted given a secret key, but is hard
to invert without knowledge of that key.

**Signatures:** Signer encrypts a message with her own private key.
  Verifier checks the message using the signer's public key.

## Elliptic Curve Cryptography

Elliptic curve: points satisfying an equation like <span
class="math">y<sup>2</sup> = x<sup>3</sup> + 7</span> (this is the curve
used in bitcoin).

For real numbers, this is [easy to solve](http://www.wolframalpha.com/input/?i=y%5E2+%3D+x%5E3+%2B+7):
<span class="math">y = sqrt(x<sup>3</sup> + 7)</span>.







