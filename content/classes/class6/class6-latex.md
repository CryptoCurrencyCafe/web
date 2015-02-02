% Class 6: Proofs of Work
% 2015-02-02

<!--
   <div class="phighlight">
   [PDF version for printing](|filename|./class6.pdf)
   </div>
-->

## Schedule 

   <div class="todo">

- If you didn’t get full credit for Project 1 because of failure to post
  something interesting, you can (and should!) redeem yourself and earn
  full credit by **posting an interesting comment by Thursday**.  It can
  be on (1) Discussion questions from Project 1 (2) notes from classes,
  or (3) general forum.

- **Read:** [_Chapter 6: The Bitcoin
Network_](https://github.com/aantonop/bitcoinbook/blob/develop/ch06.asciidoc),
[_Chapter 7: The
Blockchain_](https://github.com/aantonop/bitcoinbook/blob/develop/ch07.asciidoc)
from Andreas Antonopoulos' book.  (Ideally, you should finish these
before Wednesday's class, but at the latest by Monday, 9 Feb.)
   </div>

<!--
<center> 
<iframe src="//www.slideshare.net/slideshow/embed_code/43918186" width="476" height="400" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe><br>
<div class="caption">Note: due to a bug in
slideshare's updated player, ink markings no longer appear in the
viewer.  <br>If you download the slides, they are present though.
Hopefully, the player will be fixed someday. </div>
</center>
-->

# Trust

What are valid sources of _trust_?
<div class="gap">
#
</div>

What are invalid sources of _trust_?
<div class="gap">
#
</div>

What mechanisms have humans evolved or constructed to enhance trust among strangers?
<div class="gap">
#
</div>

# Distributed Consensus

How well does the 2-out-of-3 network consensus public ledger protocol work?
<div class="gap">
#
#
</div>

\clearpage

# Proof-of-Work

Cynthia Dwork and Moni Naor.  [_Pricing via Processing or Combatting Junk Mail_](|filename|./pvp.pdf), CRYPTO 1992.

**Pricing Function**: ($f$)
- moderately easy to compute
- cannot be amortized 
- computing $f(m_1),..., f(m_l)$ costs $l$ times as much as computing $f(m_i)$. 
- easily verified: given $x$, $y$ easy to check $y = f(x)$.

Adam Back. [_Hash Cash Postage Implementation_](http://www.hashcash.org/papers/announce.txt)

**Interactive Hashcash**:  
1. Sender to Receiver: `Hello`  
2. Receiver to Sender: $r$ (random nonce)  
3. Sender to Receiver: $x$, `Mail` where $x = f(r)$  
4. Receiver verifies $x = f(r)$.  

How well does this protocol work for sending mail?
<div class="gap">
#
</div>

Suppose we use SHA-256 for $f$?
<div class="gap">
#
</div>

How can we make this protocol non-interactive?
<div class="gap">
#
</div>

# Bitcoin Mining

Proof-of-work: Find an $x$ such that: SHA-256(SHA-256($r$ + $x$)) < $T/d$.

$d$ is the "difficulty" (varies).  
$T$ is a fixed target (256-bit number).  
$r$ depends on hash of previous block, transactions, and other information.

What does it mean for the bitcoin difficulty to go down?
<div class="gap">
#
</div>

\clearpage

[BitcoinMiner](https://github.com/bitcoin/bitcoin/blob/master/src/miner.cpp) (code from core Bitcoin implementation)

```c
//
// ScanHash scans nonces looking for a hash with at least some zero bits.
// The nonce is usually preserved between calls, but periodically or if the
// nonce is 0xffff0000 or above, the block is rebuilt and nNonce starts over at
// zero.
//
bool static ScanHash(const CBlockHeader *pblock, uint32_t& nNonce, uint256 *phash)
{
    // Write the first 76 bytes of the block header to a double-SHA256 state.
    CHash256 hasher;
    CDataStream ss(SER_NETWORK, PROTOCOL_VERSION);
    ss << *pblock;
    assert(ss.size() == 80);
    hasher.Write((unsigned char*)&ss[0], 76);

    while (true) {
        nNonce++;

        // Write the last 4 bytes of the block header (the nonce) to a copy of
        // the double-SHA256 state, and compute the result.
        CHash256(hasher).Write((unsigned char*)&nNonce, 4).Finalize((unsigned char*)phash);

        // Return the nonce if the hash has at least some zero bits,
        // caller will check if it has enough to reach the target
        if (((uint16_t*)phash)[15] == 0)
            return true;

        // If nothing found after trying for a while, return -1
        if ((nNonce & 0xfff) == 0)
            return false;
    }
}
```
[BitcoinMiner](https://github.com/bitcoin/bitcoin/blob/master/src/miner.cpp#L438): (excerpted, most error checking code removed)

```c
void static BitcoinMiner(CWallet *pwallet)
{
    SetThreadPriority(THREAD_PRIORITY_LOWEST);
    CReserveKey reservekey(pwallet);
    unsigned int nExtraNonce = 0;

    try {
        while (true) {
            // Create new block
            unsigned int nTransactionsUpdatedLast = mempool.GetTransactionsUpdated();
            CBlockIndex* pindexPrev = chainActive.Tip();

            auto_ptr<CBlockTemplate> pblocktemplate(CreateNewBlockWithKey(reservekey));
            CBlock *pblock = &pblocktemplate->block;
            IncrementExtraNonce(pblock, pindexPrev, nExtraNonce);

            int64_t nStart = GetTime();
            arith_uint256 hashTarget = arith_uint256().SetCompact(pblock->nBits);
            uint256 hash;
            uint32_t nNonce = 0;
            while (true) {
                // Check if something found
                if (ScanHash(pblock, nNonce, &hash))
                {
                    if (UintToArith256(hash) <= hashTarget)
                    {
                        // Found a solution
                        pblock->nNonce = nNonce;
                        assert(hash == pblock->GetHash());

                        SetThreadPriority(THREAD_PRIORITY_NORMAL);
                        LogPrintf("proof-of-work found  \n  hash: %s  \ntarget: %s\n", 
	                          hash.GetHex(), hashTarget.GetHex());
                        ProcessBlockFound(pblock, *pwallet, reservekey);
                        SetThreadPriority(THREAD_PRIORITY_LOWEST);
                        break;
                    }
                }

                if (nNonce >= 0xffff0000) break;
                // ... other breaking conditions elided
                // Update nTime every few seconds
                UpdateTime(pblock, pindexPrev);
            }
        }
    }
    catch (const boost::thread_interrupted&)
    {
        LogPrintf("BitcoinMiner terminated\n");
        throw;
    }
}
```


