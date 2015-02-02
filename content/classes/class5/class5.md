Title: Class 5: DigiCash
Date: 2015-01-28

   <div class="phighlight">
   [PDF version for printing](|filename|./class5.pdf)
   </div>

## Schedule 

   <div class="todo">
[Project 1](|filename|../../pages/projects/project1/project1.md) is due **Friday, 30 January** (11:59pm).

**Upcoming office hours:**  Thursday 4-5pm (Dave, Rice 507); Friday (Nick, noon-2pm in Hackcville).
   </div>

<center> 
<iframe src="//www.slideshare.net/slideshow/embed_code/44010587" width="476" height="400" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe><br>
<div class="caption">Note: due to a bug in
slideshare's updated player, ink markings no longer appear in the
viewer.  <br>If you download the slides, they are present though.
Hopefully, the player will be fixed someday. </div>
</center>


## Cryptographic Hash Functions

A _cryptographic hash function_, <span class="math">_H_(_x_)</span>, must satisfy these two properties:

- **one-way** (preimage resistance): given <span class="math">_h_= _H_(_x_)</span> it is hard to find preimage <span class="math">_x_</span>.
- **strong collision-resistance**: hard to find any pair <span class="math">_x_</span> and <span class="math">_y_</span> where <span class="math">_H_(_x_) = _H_(_y_)</span>

If we use SHA-256 for <span class="math">_H_</span>, how many 258-bit
messages would be expected to hash to a given value <span
class="math">_x_</span>?
<div class="gap">

</div>

## Signing Message Digests

**Sign:** Sign(<span class="math">m</span>) = <span class="math">_E_(_KR_<sub>A</sub>, _H_(_m_))</span>

Given <span class="math">_KU_<sub>A</sub></span>, <span
class="math">_m_</span>, and <span class="math">_S_</span>, how does Bob
verify that <span class="math">_S_</span> is a valid signature from
Alice for <span class="math">_m_</span>?

<div class="gap">

</div>

A bitcoin address for public key _K_ is RIPEMD160(SHA256(_K_)) where both
RIPEMD160 and SHA256 are cryptographic hash functions.  

Is this more or less secure than just using _K_?  
<div class="gap">


</div>

Suppose someone finds a way to find collisions for RIPEMD160.  How
serious of a risk would this pose to bitcoin?  
<div class="gap">

</div>

Suppose someone finds a way to find preimages for RIPEMD160.  How
serious of a risk would this pose to bitcoin?
<div class="gap">

</div>

## Untraceable Electronic Cash

[High Trust Bank](https://www.fdic.gov/bank/individual/failed/hightrust.html) must be trusty!

David Chaum, Amos Fiat, and Moni Naor.  [_Untraceable Electronic
Cash_](|filename|./ecash.pdf).  CRYPTO 1988.

**Simple RSA Signatures**  
Public Key = <span class="math">(_e_, _n_)</span>
Private Key = <span class="math">_d_</span>

Identity: <span class="math">_M_<sup>_de_</sup> = _M_ mod _n_</span>

<span class="math">Sign(_m_) = _m_<sup>_d_</sup> mod _n_</span>

**Blind Signatures**
Alice picks random <span class="math">_k_</span> in <span class="math">[1, _n_)</span>  
<span class="math">_t_ = _mk_<sup>_e_</sup> mod _n_</span>  
Sends <span class="math">_t_</span> to signer.

Signer returns <span class="math">_t_<sup>_d_</sub></span>.


Signer returns <span class="math">_t_<sup>_d_</sup></span>.

<span class="math">_t_<sup>_d_</sup> = (_mk_<sup>_e_</sup> mod _n_)<sup>_d_</sup> mod _n_</span>  
&nbsp;&nbsp;&nbsp; <span class="math">= _m_<sup>_d_</sup>_k_<sup>_ed_</sup> mod _n_</span>  
&nbsp;&nbsp;&nbsp; <span class="math">= _m_<sup>_d_</sup>_k_ mod _n_</span>  

Dividing by <span class="math">_k_</span> gives <span class="math">Sign(_m_) = _m_<sup>_d_</sup> mod _n_</span>.


What should a signer know before signing a random-looking string?
<div class="gap">
#
#
</div>

**Cut-and-Choose**

Suppose Alice sends 256 copies and the Bank checks 255 of them.  What is the probability Alice can cheat without getting caught?
<div class="gap">
#
</div>

What should the maximimum bill size be to prevent cheating?
<div class="gap">
#
</div>

### Identity Strings

_I_ = "alice@alice.org"  

<span class="math">_M_<sub>_i_</sub></span> = "Bill #[r<sub>i</sub>] : Bear’s Turns Bank owes the holder of this message $100."  
&nbsp;&nbsp;&nbsp; + identity strings:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="math">_I_<sub>1</sub> = (_h_(_I_<sub>1L</sub>), _h_(_I_<sub>1R</sub>)), ..., _I_<sub>_n_</sub> = (_h_(_I_<sub>nL</sub>), _h_(_I_<sub>nR</sub>))</span>  
&nbsp;&nbsp;&nbsp; where <span class="math">_h_</span> is a one-way hash function and each <span class="math">_I_<sub>iL</sub> &oplus; _I_<sub>iR</sub> = _I_</span> (but <span class="math">_I_<sub>iL</sub> is choosen randomly).

To spend a bill, the reciever chooses either L or R for each pair for spender to open.

What is the probability Alice can spend a bill twice without revealing her identity?
<div class="gap">
#
</div>


[Before Bitcoin: The Rise and Fall of DigiCash](http://globalcryptonews.com/before-bitcoin-the-rise-and-fall-of-digicash/)

> _By all accounts Chaum was a charismatic leader with an interesting management style, but he refused to compromise his artistic vision in any area against the best advice of his employees. He was suspicious of everyone and 'paranoid' with a habit of suddenly changing his mind without warning. At one time, Microsoft had offered DigiCash $180 million to allow them to preinstall Ecash software on Windows computers and the deal was on the verge of completion, but Chaum suddenly decided that his product was worth more and the deal collapsed. If the deal had gone through, cryptocurrency would now be as ubiquitous as Internet Explorer._

