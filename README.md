# pyTED

## _Aut viam inveniam aut faciam_

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Dependabot](https://badgen.net/badge/icon/dependabot?icon=dependabot&label)](https://dependabot.com/)
[![Build Status](https://travis-ci.com/ch0ppy35/pyTed.svg?branch=dev)](https://travis-ci.com/ch0ppy35/pyTed)

Here's a README for an obscure project.

### What is it?

This is a Flask app that's being written as a front-end for
[TED - The Energy Detective](https://www.theenergydetective.com/).

Using api information found [here](http://files.theenergydetective.com/docs/TED5000-API-R330.pdf).

A neat gadget, check it out.

### Who's behind it?

[ch0ppy35](https://github.com/ch0ppy35) and [JustBeanie](https://github.com/JustBeanie)

### Why?

We want/need a dashboard for mobile, and we didn't want to write an Android app _and_ an iOS app. 
We found that other apps for iOS or Android weren't being maintained. 

After a phone upgrade we were left with no simple mobile app for Ted!
So we turned to Python and Flask.

### What it needs to run

Python3, check requirements.txt.  You'll need a Postgres endpoint too.

Runs on Mac and Linux, the latter preferably in prod. 
Hadn't bothered to test this running on Windows (If you want to run on Windows, just run a *nix VM of sorts).


---

### License

```license
MIT License
Copyright (c) 2020 Mike Miller

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```