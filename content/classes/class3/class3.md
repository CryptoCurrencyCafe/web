Title: Class 3: Elliptic Curves
Date: 2014-01-21

   <div class="phighlight">
   [PDF version for printing](|filename|./class3.pdf)
   </div>

## Schedule 

   <div class="todo">
[Project 1](|filename|../../pages/projects/project1/project1.md) is due **Friday, 30 January**. 

Before the next class (Monday, Jan 26): 

- **Read:** Satoshi Nakamoto, [_Bitcoin: A Peer-to-Peer Electronic Cash
System_](https://bitcoin.org/bitcoin.pdf), 2008.  The is the original
bitcoin paper, which is quite readable.

- **Read:** [_Chapter 5:
    Transactions_](https://github.com/aantonop/bitcoinbook/blob/develop/ch05.asciidoc)
    from Andreas Antonopoulos' book.
   </div>

<center> 
<iframe src="//www.slideshare.net/slideshow/embed_code/43761680" width="476" height="400" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe><br>
<div class="caption"><font size="-2">Note: due to a bug in
slideshare's updated player, ink markings no longer appear in the
viewer.  <br>If you download the slides, they are present though.
Hopefully, the player will be fixed someday. </div>
</center>

### Asymmetric Cryptosystems Recap

For asymmetric cryptography, we need a one-way function with a trapdoor:
a function that can be easily inverted given a secret key, but is hard
to invert without knowledge of that key.

**Signatures:** Signer encrypts a message with her own private key.
  Verifier checks the message using the signer's public key.

## Elliptic Curve Cryptography

**Elliptic curve:** points satisfying an equation like <span
class="math">_y_<sup>2</sup> = _x_<sup>3</sup> + 7</span> (this is the curve
used in bitcoin).

For real numbers, this is [easy to solve](http://www.wolframalpha.com/input/?i=y%5E2+%3D+x%5E3+%2B+7):
<span class="math">_y_ = sqrt(_x_<sup>3</sup> + 7)</span>.

In a finite field, it is complex enough to form the basis of cryptographic operations.

## Crash Course in Group Theory

**Group:** A group is a set, <span class="math">_G_</span>, on which the operation <span class="math">&oplus;</span> is defined with the following properties:

1. _Closure_: for all <span class="math">_a_, _b_ &isin; _G_</span>, <span class="math">_a_ &oplus; _b_ &isin; _G_</span>.

2. _Associative_: for all <span class="math">_a_, _b_, _c_ &isin; _G_</span>, <span class="math">(_a_ &oplus; _b_) &oplus; _c_ = _a_ &oplus; (_b_ &oplus; _c_)</span>.

3. _Identity_: there is some element, <span class="math"><b>0</b> &isin; _G_</span>, such that for all <span class="math">a &isin; _G_</span>, <span class="math">_a_ &oplus; <b>0</b> = <b>0</b> &oplus; _a_ = _a_<span>.

4. _Inverse_: for all <span class="math">_a_ &isin; _G_</span>, there exists an inverse, <span class="math">-_a_ &isin; _G_</span>, such that <span class="math">_a_ &oplus; (-_a_) = <b>0</b></span>.

**Abelian Group:** An abelian (or commutative) group has this additional property:

- _Commutative_: for all <span class="math">_a_, _b_ &isin; _G_</span>, <span class="math">_a_ &oplus; _b_ = _b_ &oplus; _a_</span>.

Are the integers and addition an abelian group?
<div class="gap">
</div>

Are the whole numbers and addition an abelian group?
<div class="gap">
</div>

**Finite Field:** A finite field is a set <span class="math">_F_</span> of <span class="math">_N_ &ge; 2</span> elements on which the operators <span class="math">&oplus;</span> and <span class="math">&times;</span> are defined with these properties:

1. <span class="math">_F_</span> is an _abelian group_ with identity <span class="math"><b>0</b></span> under the <span class="math">&oplus;</span> operation.  

2. The set <span class="math">_F_ - { 0 }</span> is an _abelian group_ with identity <span class="math"><b>1</b></span> under the <span class="math">&times;</span> operation.

3. Distributive: For all <span class="math">_a_, _b_, _c_ &isin; _F_</span>, <span class="math">(_a_ &oplus; _b_) &times; _c_ = (_a_ &times; _c_) &oplus; (_b_ &times; _c_)</span>.

(Note that this requires for all <span class="math">_a_</span>, <span class="math">_a_ &times; <b>0</b> = <b>0</b></span>.)

**Prime Field Theorem:** For every prime number <span
  class="math">_p_</span>, the set <span class="math">{ 0, 1, &hellip;, _p_
  - 1 }</span> forms a finite field with the operations addition and
  multiplication modulo <span class="math">p</span>.

Demonstrate that <span class="math">_F_<sub>3</sub></span> is a finite field.
<div class="gap">

</div>

See [_Introduction to Finite
Fields_](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-451-principles-of-digital-communication-ii-spring-2005/lecture-notes/chap7.pdf)
(notes from David Forney's [MIT 6.451
course](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-451-principles-of-digital-communication-ii-spring-2005/index.htm))
for a proof that all prime fields, <span
class="math">F<sub>p</sub></span> are finite fields, and more thorough
introduction to finite fields.

## Operations on Elliptic Curves

"Addition" on an elliptic curve is done by finding the a point on the
line between the two inputs points, and reflecting that point over the
x-axis.

Here's what this looks like for real numbers (but don't be mislead
&mdash; elliptic curves over finite fields do not look anything like
these simple curves):

   <center>
   <img src="http://media.coindesk.com/2014/10/point-addition.png"><br>
Image source: Eric Rykwalder, [_The Math Behind Bitcoin_](http://www.coindesk.com/math-behind-bitcoin/).
   </center>

<span class="math">_P_ + _Q_ = _R_</span>

Doing addition on elliptic curves over finite fields is more complex,
and there has been a lot of research into how to do these operations
efficiently.  See the
[btcec.Add](https://github.com/btcsuite/btcec/blob/master/btcec.go#L431)
code for how it is done in the library.

Doubling (e.g., <span class="math">_P_ + _P_ = _R_</span>) is the same idea,
except instead of finding the intersection of the line formed by the two
addends (which doesn't exist for the single point), finds the
intersection between the tangent of the curve.

"Multiplication" is just repeated addition: <span class="math">_kP_ = _P_ +
_P_ + ... + _P_</span>.

Is there a more efficient way to compute <span class="math">9_P_</span> than using 8 additions?  
<div class="gap">

</div>







