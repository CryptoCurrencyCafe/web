Title: Project 2 - Mining Points
Date: 2015-02-10
Category: PS
Tags: Problem Sets, mining
Slug: project2

   <div class="due">
Part 1 Due: **Sunday, 22 February**; Part 2 Due: **Thursday, 5 March**
   </div>

## Purpose

- Understand how cryptocurrency mining works by building and running a
miner for a new cryptocurrency.  

- Explore some potential threats to bitcoin by attempting attacks on our
class cryptocurrency.

- Get some experience using cloud computing resources and understanding 
  computing costs in practice.

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

   <div class="exercise"> 

**Set up your pointcoind node.** Following the instructions below, set
up your pointcoind node and wallet.  After finishing this, [post a
comment here](|filename|./pointcoin-nodes.md) with the public IP address
of your EC2 node.

   </div>

To set up your pointcoind node:

1. Setup an EC2 instance, install go and pointcoin following these directions: [Installing
  PointCoin on
  AWS](https://github.com/PointCoin/pointcoind/wiki/Installing-PointCoin-on-AWS).

2. Setup your node and wallet: [Using PointCoin](https://github.com/PointCoin/pointcoind/wiki/Using-PointCoin-Binaries)

The main goal for this part is for everyone to write your own PointCoin
miner.  We have provided some code in the [Project 2
repo](https://github.com/CryptoCurrencyCafe/project2) for you to get
started:

- [miner.go](https://github.com/CryptoCurrencyCafe/project2/blob/master/miner.go) - an initial template for a PointCoin miner.
  You will implement your miner by modifying this file.
- [support.go](https://github.com/CryptoCurrencyCafe/project2/blob/master/support.go) - some functions that you will find useful
  in implementing your miner.  (You are not expected to change these
  functions, but can change them if you want to.)

Next, we provide some hints that may be helpful in building your miner.

### Coinbase Transaction

Although some people might mine cryptocurrency for purely altruistic
reasons, the main economic incentive for mining is that the miner who
finds a new block can add a transaction to that block transfering the
mining fee to their address.

We have provided the [`createCoinbaseTx`](https://github.com/CryptoCurrencyCafe/project2/blob/master/support.go#L84) function in `support.go` to
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

In PointCoin, the mining reward is 1 pointcoin (see [this
commit](https://github.com/PointCoin/pointcoind/commit/5c81f47ea739baf7841cbc0e7b7c3aa06b986067)
for how it was modified from how it is set in bitcoin).

If you want to receive the rewards for your mining efforts, you need to
set the address used in the coinbase transaction to be the address for
your PointCoin wallet.

### Merkle Root

The block header contains the Merkle Root of all the transactions in the
block.  This should be all the valid transactions submitted to the
network, with your coinbase transaction added.

We have provided the [`createMerkleRoot`](https://github.com/CryptoCurrencyCafe/project2/blob/master/support.go#L196) function in `support.go` for
computing the Merkle root of a list of transactions:

```go
func createMerkleRoot(txs []*btcwire.MsgTx) *btcwire.ShaHash {
	txutil := []*btcutil.Tx{}
	for _, tx := range txs {
		convtx := btcutil.NewTx(tx)
		txutil = append(txutil, convtx)
	}

	store := blockchain.BuildMerkleTreeStore(txutil)
	merkleRoot := store[len(store)-1]
	return merkleRoot
}
```


### Creating a Block

A block in PointCoin is similar to a block in bitcoin.  It contains a
header consisting of:

- The hash of the previous block
- The hash of the Merkle tree of all the transactions
- The difficulty
- A nonce (32 bits)

In addition to the header, it includes the list of transactions.

We have provided the `CreateBlock` function in `support.go` to build a
block given these inputs:

```go
func CreateBlock(prevHash string, merkleRoot *btcwire.ShaHash, difficulty big.Int, 
                 nonce uint32, txs []*btcwire.MsgTx) *btcwire.MsgBlock {
	prevH, _ := btcwire.NewShaHashFromStr(prevHash)
	d := blockchain.BigToCompact(&difficulty)
	header := btcwire.NewBlockHeader(prevH, merkleRoot, d, nonce)

	msgBlock := btcwire.NewMsgBlock(header)
	for _, tx := range txs {
		msgBlock.AddTransaction(tx)
	}

	return msgBlock
}
```

### Mining a Block

Of course, the block you create is unlikely to be valid with a randomly
selected nonce.  To find a valid block, it is necessary to find a nonce
such that the hash of the block header (with that nonce included) is
below the target difficulty.

The block nonce is a uint32 in `block.Header.Nonce`.  You can update
this value with a simple assignment to try a different nonce value.

The function
[`BlockSha`](https://github.com/btcsuite/btcd/blob/master/wire/blockheader.go#L48)
returns the Double-SHA256 hash of the block header, so you can compute
the hash of your block using `block.Header.BlockSha()`.

Because of the different ways numbers and hashes are represented, the
difficulty comparison is more awkward than one would like.  You can use
the provided `lessThanDiff` function to check if the returned hash is
less than the target difficulty:

```go
func lessThanDiff(hash btcwire.ShaHash, difficulty big.Int) bool {
	bigI := blockchain.ShaHashToBig(&hash)
	return bigI.Cmp(&difficulty) <= 0
}
```

If you've succeeded in finding a good nonce, submit the block!

This code will submit the block (since `client` is setup as an RPC to
the node running on your own instance, it is submitting it to your own
node first, which, if the block is valid, will submit it to the rest of
the network):

```go
   err := client.SubmitBlock(btcutil.NewBlock(block), nil)
   if err != nil { // something failed
```

Note that one reason your submission may fail is if the blockchain has
already advanced.  This would happen if another miner found and
submitted a block (that was received by your node) since the call you
made to `client.GetBlockTemplate(&btcjson.TemplateRequest{})` to obtain
the previous block (used in the template header).

### Becoming a PointCoin Tycoon

You should start by making your miner as simple as possible, and getting
a simple miner working before attempting to do anything more
complicated.  

If you are ambitious, though, there are lots of ways to improve the
performance of your miner (still running on the low-powered micro EC2
node).

Here are a few possibilities:

- Explore the tradeoff between frequently checking the network to update
  your block template, and computing lots of hashes (that might be
  wasted if the blockchain has advanced).  Your miner will not perform
  well if you update your template after every hash attempt, or if you
  keep trying until you find a good block without ever updating your
  template.  

- Even the micro instances have more than one core.  You are missing out
  on a lot of potential mining power if you are only using one thread.


   <div class="problem"> 
**Problem 1.** Use your miner to acquire PointCoin.  You will receive
  full credit for acquiring at least 100 PointCoin.
   </div>

   <div class="problem"> 
**Problem 2.** Estimate the cost of mining PointCoin given the current
difficulty level, and assuming you are using your mining code running on
an EC2 node.  A good answer would include an analysis of the expected
number of hashes that must be computed for a given difficulty level.  
   </div>


   <div class="problem"> 

**Problem 3.** What prevents a greedy miner from transfering more coin
  to the miner's address in a newly found block by increasing the value
  of the output of the coinbase transaction?

   </div>

   <div class="problem"> 

**Problem 4.** Why is there an extra nonce along with the next block
  height included in the coinbase transaction?  (Hint: how is the
  coinbase transaction different from normal transactions?)

   </div>

Submit the [Project 2/Part 1 Submission
Form](http://goo.gl/forms/nz3WSwVPU4) (by 11:59pm on **Sunday, 22
February**).  (You can submit your answers to Problems 1-4 above either
by submitting text in the form, or submitting a link to a PDF containing
all of your answers).

# Part 2: Investigating Mining

   <div class="exercise">
In Part 2, we'll explore attacked on the PointCoin network.  You should not attempt to actually launch any attacks until after class on **Monday, 23 February**.
   </div>

In the second part of this project, you will explore ways to attack the
PointCoin network.  For this part, you may collude with other students
in the class and use any external resources you want.  

The only rules are:

1. You must disclose honestly everything that you did when you submit
the assignment (and in response to any questions before this).

2. You may not do anything that violates any law or the University honor
code.  This means you should not attempt to log into anyone elses
computer and you should not attempt to distribute malware.  

3. It is, however, considered fair (indeed, encouraged) to "lie" or
"mislead" your fellow students regarding your mining behavior.  For
example, it would be totally okay and encouraged for you to attempt to
trick others into joining your mining pool by offering them a share of
the points mined, but the not to deliver those points.  For the purposes
of this assignment, you should consider your classmates to be mutually
distrusting individuals.

4. You should not do anything a reasonable person would consider
unethical or in violation of the spirit of this assignment.  This is a
very vague statement.  What it really means is that if you are uncertain
about whether something you plan to do is consistent with the spirit of
this project, you should consult with Dave before doing it.

Your goal for Part 2 is to acquire ownership of as many PointCoins as
you can.  Your grade for this part will be based on (1) the number of
PointCoins you control (you will prove control over your PointCoins by
transferring them to a given address); and (2) your written description
of the things you tried and what you learned from them.

### Submission

Submit the [Project 2 Submission Form](http://goo.gl/forms/notyet) (by
11:59pm on **Thursday, 5 March**).

<!--
<iframe src="https://docs.google.com/forms/d/1I2a2T9owqTvLx7GAT8EIVf-qAhR2NU2113cSvwVOOAE/viewform?embedded=true" width="760" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>
-->

<p><br></br></p>

<div class="disqus">
<div id="disqus_thread"></div>
</div>
