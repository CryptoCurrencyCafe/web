% Class 4: Verifiably Random?
% 2015-01-26

## Schedule 

   <div class="todo">
[Project 1](|filename|../../pages/projects/project1/project1.md) is due **Friday, 30 January** (11:59pm).

**Scheduled office hours:**  
Dave --- after class Mondays, Thursdays 4-5pm (both in Rice 507)  
Nick --- Mondays 5-7pm (in Rice 442), Fridays (noon-2pm in Hackcville, #9 Elliewood Ave)
   </div>


## Signing with Elliptic Curves

**Elliptic curve discrete logarithm problem:** given points <span class="math">_P_</span> and <span class="math">_Q_</span>
  on an elliptic curve, it is hard to find an integer <span class="math">_k_</span> such that <span class="math">_Q_ = _kP_</span>.

**Parameters:** curve, _G_ (a point on curve), (large) _n_ such that <span class="math">_nG_ = 0</span>. 

**Key pair:**  
&nbsp;&nbsp;&nbsp;_Private key_: <span class="math">_d_</span> = pick a random integer in <span class="math">[1, _n_-1]</span>  
&nbsp;&nbsp;&nbsp;_Public key_: point on the curve, <span class="math">_Q_ = _dG_</span>

**Signing:**  
&nbsp;&nbsp;&nbsp;pick random integer <span class="math">_k_</span> in <span class="math">[1, _n_-1]</span>  
&nbsp;&nbsp;&nbsp;compute curve point: <span class="math">(_x_, _y_) = _kG_</span>  
&nbsp;&nbsp;&nbsp;signature = <span class="math">(_x_ mod _n_, _k_<sup>-1</sup>(_z_ + _rd_) mod _n_)</span>

What are the reasons for prefering ECC for signatures in bitcoin over RSA-based signature algorithms?
<div class="gap>
#
#
</div>


For an interesting history of improvements in factoring, see Carl Pomerance, [_A Tale of Two Sieves_](http://www.ams.org/notices/199612/pomerance.pdf), Notices of the AMS, December 1996: 

> _John Pollard in 1988 circulated a letter to several people outlining an idea of his
> for factoring certain big numbers via algebraic number fields. His
> original idea was not for any large composite, but for certain "pretty"
> composites that had the property that they were close to powers and had
> certain other nice properties as well. He illustrated the idea with a
> factorization of the number $2^{2^{7}}$ + 1, the seventh Fermat number.
> I must admit that at first I was not too keen on Pollard's method, since it seemed to be applicable
> to only a few numbers. ... 
> But what of general numbers? In the summer of 1989 I was to give a talk at the meeting of the
> Canadian Number Theory Association in Vancouver. It was to be a survey talk on factoring,
> and I figured it would be a good idea to mention Pollard's new method. On the plane on the way
> to the meeting I did a complexity analysis of the method as to how it would work for general
> numbers, assuming myriad technical difficulties did not exist and that it was possible to run
> it for general numbers. I was astounded. The complexity for this algorithm-that-did-not-yet exist
> was of the shape_ <span class="math">exp(_c_(log _n_)$^{1/3}$ (log log _n_)$^{2/3}$). 

Erich Wenger and Paul Wolfger, [_Solving the Discrete Logarithm of a
113-bit Koblitz Curve with an FPGA
Cluster_](http://eprint.iacr.org/2014/368.pdf). 

> _It is possible to repeatedly fold a standard letter-sized sheet of
> paper at the midway point about six to seven times. In 2012, some MIT
> students were able to fold an 1.2 kilometer long toilet paper 13
> times. And every time the paper was folded, the number of layers on
> top of each other doubled. Therefore, the MIT students ended up with
> 213 = 8192 layers of paper on top of each other.  And poor Eve’s job
> was to manually count all layers one by one.  Similar principles apply
> in cryptography, although bigger numbers are involved.  In Elliptic
> Curve Cryptography (ECC), where_ <span class="math">log<sub>2</sub>
> _n_</span>_-bit private keys are used, Eve does not have to iterate
> through all possible_ <span class="math">_n_</span> _keys. Instead, Eve
> would use the more efficient parallelizable Pollard’s rho algorithm
> that finishes in approximately_ <span class="math">sqrt(_n_)</span>
> _steps. The omnipresent question is how big _<span class="math">_n_</span> _has to be such that even
> the most powerful adversaries are not able to reconstruct a private
> key. Especially in embedded, cost-sensitive applications, it is
> important to use keys that are only as large as necessary._


## Bitcoin's Curve

Standards for Efficient Cryptography: [_SEC 2: Recommended Elliptic
Curve Domain Parameters_](http://www.secg.org/sec2-v2.pdf) (Certicom
Research, 27 January 2010)

> _Verifiably random parameters offer some additional conservative features. These parameters are
> chosen from a seed using SHA-1 as specified in ANSI X9.62 [X9.62]. This process ensures that
> the parameters cannot be predetermined. The parameters are therefore extremely unlikely to
> be susceptible to future special-purpose attacks, and no trapdoors can have been placed in the
> parameters during their generation. When elliptic curve domain parameters are chosen verifiably
> at random, the seed S used to generate the parameters may optionally be stored along with the
> parameters so that users can verify the parameters were chosen verifiably at random._

What does it mean for parameters to be "verifiably random"?
<div class="gap">

</div>

\clearpage

# Randomness

**Kolmogorov Complexity:** <span class="math">_K_(_s_)</span> = the length of the shortest description of <span class="math">_s_</span>.

**Kolmogorov's Definition of Random:** A sequence <span
  class="math">_s_</span> is random, if <span class="math">_K_(_s_) =
  |_s_| + _C_</span> 

What is the Kolmogorov Complexity of the string `0001000010000011111111100111...`?
<div class="gap">
#
</div>

\raggedright
What is the Kolmogorov Complexity of the string: 1MRigEo5423vycLnUdSnA4C6Ts691fUiYu 18UikW89q9VgGDftQW3Gmuhe4sQDCFP5kD 19ZQwQmfAsgy47ErehfkW3SeSzNGFfH9iN 1AZCH1insc6JrT2Z9SiNvgtTugXg8sF8yd 15qYggRJvmyZfpchxvNqr6h3pNjw6bGBV9 1C943NwPPffUFY7VDzi3kt7KikXwc2vdkN 1JBhLLCgNYhR8f6AZcRS3mjfEAmMzPvwyf 1JvDrBSYm6o4ZTQUhwUE4FhPFxd2wuXWUR 1KcBM1RNhcp1oENycoD4AezA5Se4SrsZnA 16JZWC433XRxjWwR7X65uxRVFdLTmoPr4t 149LB8VYaT1BdMLyQUL92Kj6KrJfNwcp64 16zDGuzbwkHjW8dNYMw9stDjRbTzVSLZU1 1HfMaZn53ZDWKgmhWxk1UPZMjQ6QmpW6m...?
<!-- 14gZWnuwKpRLTCUFCAgTZMciRaEdrkmEpr 1BZ2ateDPugmqLzYsXVy9EK5BguvXa2Bnj 1rCdRyMVcZHJaHA2LKUvRqYBcHqvAfQkc 1Ak8VwX6x4FPbA6aXTC3BQGQHnnhfaJuB8 129sBvF6Jternwdn5XcoA37LinQRcmAD5U1H2in 1HxEzSKHssPtog2krjFPiPfrKSiw4... ?
-->
<div class="gap">
#
</div>
\justifying

\noindent Daniel J. Bernstein, Tung Chou, Chitchanok Chuengsatiansup, Andreas
H&uuml;lsing, Tanja Lange, Ruben Niederhagen, and Christine van Vredendaal.
[_How to Manipulate Curve Standards: A White Paper for the Black  Hat_](https://eprint.iacr.org/2014/571.pdf), 2014.


\noindent How likely is it that the parameters for the secp256k1 curve used by bitcoin have a trapdoor?
<div class="gap">
#
</div>

How should ECC parameters be generated for an important curve in a standard?
<div class="gap">  
#
#
</div>

[_Root Zone DNSSEC KSK Ceremonies
Guide_](http://www.root-dnssec.org/wp-content/uploads/2010/02/draft-icann-dnssec-ceremonies-00.txt).
If you have a few hours to spare, you can watch a key signing for the
DNSSEC (Domain Name System): [DNSSEC KSK Ceremony
20](https://www.iana.org/dnssec/ceremonies/20)

\clearpage

## Dual-EC PRNG 

[NIST Special Publication 800-90A Recommendation for Random Number
Generation Using Deterministic Random Bit
Generators](http://csrc.nist.gov/publications/nistpubs/800-90A/SP800-90A.pdf)

\noindent
$P$ and $Q$ are points on the curve, specified by the standard (but not
explained how $Q$ is choosen).  $P$ is a generator, so there exists some
$e$ such that $Q^e = P$.

\noindent $s_0 =$ initalize with seed randomness  
\noindent $s_{i+1} = \varphi(s_i \times P)$

\noindent$r_i = \varphi(s_i \times Q)$
$o_i = $ the low-order 16 bits of the $x$-coordinate of $r_i$.

\noindent Given $o_i$, how much work is it to find all the possible $r_i = (x, y)$ values?
<div class="gap">
#
#
</div>

\noindent Given $e$, what is $\varphi(e \times A)$ where $A$ is a possible $r_i$ value?
<div class="gap">
#
</div>


\noindent Dan Shumow, Niels Ferguson.  [_On the Possibility of a Back Door in the
NIST SP800-90 Dual Ec Prng_](http://rump2007.cr.yp.to/15-shumow.pdf).
CRYPTO 2007 Rump Session.

\noindent Michael Wertheimer (NSA), [_Encryption and the NSA Role in International
Standards_](http://www.ams.org/notices/201502/rnoti-p165.pdf), Notices
of the American Mathematical Society, February 2015.

\noindent Wertheimer's letter is an attempt to respond to [_Mathematicians Discuss the
Snowden Revelations_](http://www.ams.org/notices/201406/rnoti-p623.pdf).

> _The recent revelations about the NSA’s spying
programs are both dismaying and encouraging.
What is encouraging is that they might lead not
just to a reform of the intelligence agencies but
also to a more serious look at what the ongoing
and inevitable erosion of privacy is doing to our
society. What is dismaying is less the intrusive data
collection itself and more what it reveals about the
decision-making processes inside the government._ (Andrew Odlyzko)


\noindent How satisfying is the NSA's response?  Are you more dismayed or encouraged?
<div class="gap">
#
</div>
