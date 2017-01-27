#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import json

RE_UCJK = re.compile(
    '[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff'
    '\U00020000-\U0002A6DF\U0002A700-\U0002B73F'
    '\U0002B740-\U0002B81F\U0002B820-\U0002CEAF'
    '\U0002F800-\U0002FA1F]'
)

stdict = {}
tsdict = {}
trad = set()

# known differences from other sources or manual blacklist
ambigous = set('檐咤瞭𬬻𬬭𬭶腭醯丨葢麽')

with open('TSCharacters.txt', 'r', encoding='utf-8') as f:
    for ln in f:
        l, r = ln.strip().split('\t')
        if len(r) != 1:
            ambigous.add(r)
        elif r in stdict:
            ambigous.add(r)
            tsdict[l] = r
        else:
            if l != r:
                trad.add(l)
            stdict[r] = l
            tsdict[l] = r

with open('STCharacters.txt', 'r', encoding='utf-8') as f:
    for ln in f:
        l, r = ln.strip().split('\t')
        if len(r) != 1:
            ambigous.add(l)
        elif l in stdict:
            if stdict[l] != r:
                ambigous.add(l)
        else:
            stdict[l] = r
        for ch in r.split(' '):
            if ch != l:
                trad.add(ch)
            tsdict[ch] = l

for varients in ('HKVariants.txt', 'TWVariants.txt'):
    with open(varients, 'r', encoding='utf-8') as f:
        for ln in f:
            l, r = ln.strip().split('\t')
            ambigous.add(l)
            ambigous.add(tsdict.get(l))
            for ch in r.split(' '):
                ambigous.add(ch)
                ambigous.add(tsdict.get(ch))

# other available dicts
with open('Source1.txt', 'r', encoding='utf-8') as f:
    slist = f.readline().strip()
    tlist = f.readline().strip()
    assert len(slist) == len(tlist)
    for s, t in zip(slist, tlist):
        try:
            if stdict[s] != t or tsdict[t] != s:
                ambigous.add(s)
        except KeyError:
            if s != t:
                ambigous.add(s)

with open('Source2.txt', 'r', encoding='utf-8') as f:
    slist = f.readline().strip()
    tlist = f.readline().strip()
    assert len(slist) == len(tlist)
    for s, t in zip(slist, tlist):
        try:
            if tsdict[t] != s:
                ambigous.add(s)
        except KeyError:
            if s != t:
                ambigous.add(s)

for s, t in json.load(open('tongwen-st.json', 'r', encoding='utf-8')).items():
    try:
        if stdict[s] != t:
            ambigous.add(s)
            # print(s, stdict[s], t)
    except KeyError:
        if s != t:
            ambigous.add(s)

for t, s in json.load(open('tongwen-ts.json', 'r', encoding='utf-8')).items():
    try:
        if tsdict[t] != s:
            ambigous.add(s)
            # print(s, t, tsdict[t])
    except KeyError:
        if s != t:
            ambigous.add(s)
            # print(s, t)

chrlist = []

with open('charfreq_zhs.txt', 'r', encoding='utf-8', errors='replace') as f:
    for ln in f:
        l, r = ln.rstrip('\n').split(' ', 1)
        if r not in ambigous and r not in trad and RE_UCJK.match(r):
            chrlist.append(r)

chrlist = chrlist[:4096]

for i in range(0, len(chrlist), 35):
    print("'%s'" % ''.join(chrlist[i:i + 35]))
    pass
