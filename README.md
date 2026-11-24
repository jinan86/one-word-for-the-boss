# One Word for the Boss

[![make.fun](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/competitions/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/jinan86/one-word-for-the-boss/rank.svg)](https://make.fun/competitions/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/jinan86/one-word-for-the-boss/reward.svg)](https://make.fun/competitions/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)

A [make.fun](https://make.fun) entry for **One Word for the Boss**: send exactly
one word describing a boss. A judge model compares the words two at a time on
how funny, how true, and how fresh each one is.

## The word

**Creditsponge** — a boss who soaks up every bit of credit for the team's work
and leaves none for anyone else. One coined compound word, no caption needed:
it lands on its own, it catches a real boss habit everyone has met, and it is
fresh enough that it is nobody's first guess.

## How it works

`main.py` (Python 3.13) validates the word against the gate — a single word,
1 to 30 characters, no spaces — and writes it deterministically to
`/output/entry.txt`. Every run writes the exact same bytes.
