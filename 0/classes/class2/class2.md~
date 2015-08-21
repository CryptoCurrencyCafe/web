Title: Class 2: Cryptography
Date: 2015-01-14

   <div class="phighlight">
   [PDF version for printing](|filename|./class2.pdf)
   </div>

## Schedule 

   <div class="todo">
Before the next class (Wednesday, Jan 21):

1. **Read:** 
[_Chapter 3: The Bitcoin Client_](https://github.com/aantonop/bitcoinbook/blob/develop/ch03.asciidoc)
and
[_Chapter 4: Keys, Addresses, Wallets_](https://github.com/aantonop/bitcoinbook/blob/develop/ch04.asciidoc)
from Andreas M. Antonopoulos, [_Mastering Bitcoin: Unlocking Digital
Cryptocurrencies_](https://github.com/aantonop/bitcoinbook) book (also
available [in
print](http://www.amazon.com/Mastering-Bitcoin-Unlocking-Digital-Crypto-Currencies/dp/1449374042)).  

2. Pay attention to your email.  <strike>You should receive an email by Sunday,
and it will include some other things to do before Wednesday's class.</strike> [Change in plans: I haven't sent out the email yet.  I expect to do this Tuesday, and there will not be anything new due on Wednesday. Sorry for the delay!]
   </div>

<center> <iframe
src="//www.slideshare.net/slideshow/embed_code/43552674" width="476"
height="400" frameborder="0" marginwidth="0" marginheight="0"
scrolling="no"></iframe><br> 
<div class="caption"> Note: due to a bug in
slideshare's updated player, ink markings no longer appear in the
viewer.  <br>If you download the slides, they are present though.
Hopefully, the player will be fixed someday.  </div>

</center>

<!--
how is it possible to own something digital?

- copyright!

England

1662 - Licensing of the Press Act

guild of printers, "Stationer's Company" (formed in 1403, royal charter in 1557)
granted monopoly on printing [cf. Chinese granting monopoly on salt production]
exclusive right to print - responsible for censoring

ended in 1694 - no restrictions	       


Act of Queen Anne
-->

## Cryptography

_kryptos_ is a Greek root meaning hidden ("secret")

_crypto_ + _graphy_ = "secret writing"

_Decryption_ is what the intended receiver does.  
_Cryptanalysis_ is what an attacker does.  

How are cryptography and security related?
<div class="gap">

</div>

### Simple Message Cryptosystem

Two functions:

- **Encrypt:** <span class="math">_E_(_m_: byte[]) &rarr; byte[]</span>.  The input is called the
    **plaintext**; the output is called the **ciphertext**.

- **Decrypt:** <span class="math">_D_(_c_: byte[]) &rarr; byte[]</span>.

Required properties:

- **Correctness:** for all possible messages, <span class="math">_m_, _D_(_E_(_m_)) = _m_</span>
- **Security:** given the output of <span class="math">_E_(_m_)</span>, it is "hard" to learn anything interesting about <span class="math">_m_</span>.  

[_Goldwasser and Micali win Turing Award: Team honored for
‘revolutionizing the science of
cryptography'_](http://web.mit.edu/newsoffice/2013/goldwasser-and-micali-win-turing-award-0313.html),
MIT News, 13 March 2013. 

Their paper that introduced semantic security notions is:
[_Probabilistic Encryption and How to Play Mental Poker Keeping Secret
All Partial
Information_](http://groups.csail.mit.edu/cis/pubs/shafi/1982-stoc.pdf),
ACM Symposium on Theory of Computing, 1982.  (We will not get into
formal security definitions or proofs in this class, but you should take
[Mohammad Mahmoody](http://www.cs.virginia.edu/~mohammad/)'s class to
learn them.)

### Keyed Symmetric Cryptosystem

Claude Shannon, [_Communication Theory of Secrecy Systems_](http://netlab.cs.ucla.edu/wiki/files/shannon1949.pdf), 1949 (work done during World War II, but declassified later).

Two functions:

- **Encrypt:** <span class="math">_E_(_<font color="red">k</font>_: byte[], _m_: byte[]) &rarr; byte[]</span>. 

- **Decrypt:** <span class="math">_D_(_<font color="red">k</font>_, _c_: byte[]) &rarr; byte[]</span>.

Required properties:

- **Correctness:** for all possible messages, <span class="math">_m_</span>, and keys, <span class="math">_k_</span>, <span class="math">_D_(_<font color="red">k</font>_, _E_(_<font color="red">k</font>_, _m_)) = _m_</span>.
- **Security:** given <span class="math">_E_</span>, <span class="math">_D_</span>, and the output of <span class="math">_E_(<font color="red">_k_</font>, _m_)</span> it is "hard" to learn anything interesting about <span class="math">_m_</span> (without knowing <span class="math"><font color="red">_k_</font></span>).

Are these properties enough to be secure against an active attacker?
<div class="gap">

</div>

### Jefferson's Wheel Cipher

There are, of course, better ways to break a message encrypted using
Jefferson's Wheel cipher than just trying all possible keys as in a
brute force attack.  Here's how Geoff Stoker solved it: [_Jefferson
Wheel Challenge
solved!_](http://www.cs.virginia.edu/~evans/cs588-fall2001/challenges/wheel-solved.html).

**Keyspace:** the set of all possible keys.  Assume (hopefully for
  user!) that key is drawn randomly from this set.

**Brute Force Attack:** try for all possible keys, <span
  class="math">_k<sub>i</sub>_</span>, computing <span
  class="math">_D_(_k_<sub>i</sub>)</span> and see if it looks like a
  reasonable plaintext.  

In order for a brute force attack to succeed, what properties are
necessary about (1) the keyspace and (2) the message space?

<div class="gap">

</div>

### Asymmetric Cryptosystems

**Asymmetric cryptosystems** use _different functions_ for encrypting
  and decrypting, with the property that revealing the encryption
  function does not reveal the decryption function.  With Kerckhoff's
  Principle, this means there are different keys for encryption and
  decryption.

- **Generate:** produce key pair, <span class="math">(_<font color="green">KU<sub>X</sub></font>_, _<font color="red">KR<sub>X</sub></font>_)</span>, and publish the public key, <span class="math">_<font color="green">KU<sub>X</sub></font>_</span>.

- **Encrypt:** <span class="math">_E_(_<font color="green">KU<sub>X</sub></font>_: byte[], _m_: byte[]) &rarr; byte[]</span>. 

- **Decrypt:** <span class="math">_D_(_<font color="red">KR<sub>X</sub></font>, _c_: byte[]) &rarr; byte[]</span>.

**Messages:** Sender encrypts a message with the recipient's public key.
  Recipient decrypts the message using her private key.

**Signatures:** Signer encrypts a message with her own private key.
  Verifier checks the message using the signer's public key.

How can we use asymmetric cryptosystems to _prove_ ownership?
<div class="gap">
</div>

How can we use asymmetric cryptosystems to _transfer_ ownership?
<div class="gap">
</div>

Assuming we have a strong asymmetric cryptosystem, what hard problems are left
to solve to make a cryptocurrency?

<div class="gap">
</div>

### Martin Luther King at the University

There's no class on Monday to honor Martin Luther King day.  Students
are encouraged to use the class time to read Paul Gaston's [_Honor to
the Class of 1969_](http://www.virginia.edu/woodson/pubs/aa.htm) and to
learn about [_Desegregation at the University of Virginia and its
Surrounding
Communities_](https://web.archive.org/web/20100615104829/http://cti.itc.virginia.edu/~hius316/desegregation/deseghome50s.html)
(including [President Darden's
letter](https://web.archive.org/web/20070503051645/http://cti.itc.virginia.edu/~hius316/desegregation/pace1.html)).

Why is [Edgar
Shannon](http://www.nytimes.com/1997/08/26/us/e-f-shannon-jr-79-dies-forceful-chief-of-u-of-virginia.html)
the only past-president of UVa with nothing significant at the
University named after him?  Why does the University still have
courtyards and schools named after Colgate Darden and none for [Gregory
Swanson](http://www.virginia.edu/woodson/projects/kenan/swanson/swanson.html)
or [Sarah Patton
Boyle](http://artsandsciences.virginia.edu/meredithwoo/blog/the-desegregated-heart/)?

<div class="gap">
</div>

How do the actions of our current administration (especially in response
to recent events) compare to those of the 1960s?  

<div class="gap">
</div>

Will there be justification for an _Honor to the Class of
2015/2016/2017/2018_ essay?
<div class="gap">
</div>
