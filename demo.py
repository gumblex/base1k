#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base1k
import bottle

html_template = '''
<!DOCTYPE html>
<html><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Base1k/4k Demo</title>
<style type="text/css">
body{font-family:Helvetica,Arial,FreeSans,sans-serif;padding:2em;background-color:#FFF}
body,textarea,input,select{margin:0}
label>*{display:inline}form>*{margin-bottom:.625em}
textarea,input,select,button{padding:.2em .3em;outline:0;font-size:100%}textarea,input,select{border:1px solid #ccc}textarea:focus,input:focus,select:focus{border-color:#19E}textarea,input[type=text]{-webkit-appearance:none;width:13em;box-sizing:border-box}
#container{max-width:60em;margin:0 auto}h1{color:#000;padding-bottom:.5em;font-size:2em;margin:.5em 0}p,blockquote,ul,ol,dl,li,table,pre{margin:.5em 0;line-height:1.25em}
form{font-size:1em;color:#777}
header, main{text-align:center;}#content{max-width:768px;margin:0 auto;}#content span{display:inline-block;padding:0 1em;}textarea{width:100%;height:30em;line-height:1.25em;font-size:14px}textarea,input,select,button{border-radius:2px}.bsubmit{border-color:#AAA;}.bsubmit:focus{border-color:#19E;}</style>
</head>
<body>
<header id="top"><h1>Base1k/4k Demo</h1></header>
<main id="wrapper">
<div id="content">
<form action="/" method="post">
<textarea rows="30" name="q">{{result}}</textarea>
<span>
<input type="radio" id="opta1" name="base" value="1k"{{b1kchk}}>
<label for="opta1">Base1k</label>
</span>
<span>
<input type="radio" id="opta2" name="base" value="4k"{{b4kchk}}>
<label for="opta2">Base4k</label>
</span><br>
<span>
<input type="radio" id="optb1" name="style" value="s"{{sschk}}>
<label for="optb1">Simplified</label>
</span>
<span>
<input type="radio" id="optb2" name="style" value="t"{{stchk}}>
<label for="optb2">Traditional</label>
</span>
<p>
<input type="submit" name="a" value="Encode" class="bsubmit">
<input type="submit" name="a" value="Decode" class="bsubmit">
</p>
</form>
</div>
</main>
</body>
</html>
'''


@bottle.get('/')
@bottle.post('/')
def root():
    query = bottle.request.forms.get('q')
    base = bottle.request.forms.get('base')
    action = bottle.request.forms.get('a')
    if bottle.request.forms.get('style') == 't':
        style = 't'
        sschk, stchk = '', ' checked'
    else:
        style = 's'
        stchk, sschk = '', ' checked'
    if base == '4k':
        b1kchk, b4kchk = '', ' checked'
        b4k = True
    else:
        b4kchk, b1kchk = '', ' checked'
        b4k = False
    if not query:
        return bottle.template(
            html_template, result='',
            b1kchk=b1kchk, b4kchk=b4kchk, sschk=sschk, stchk=stchk)
    if action == 'Decode':
        decoder = base1k.b4kdecode if b4k else base1k.b1kdecode
        result = decoder(query.encode('latin1').decode('utf-8'),
                         style).decode('utf-8', 'replace')
    else:
        encoder = base1k.b4kencode if b4k else base1k.b1kencode
        result = encoder(query.encode('latin1'), style, 30)
    bottle.response.set_header('X-XSS-Protection', '0')
    return bottle.template(html_template, result=result,
                           b1kchk=b1kchk, b4kchk=b4kchk, sschk=sschk, stchk=stchk)


@bottle.post('/b1kencode')
def b1kencode():
    query = bottle.request.forms.get('q', '').encode('latin1')
    style = 't' if bottle.request.forms.get('style') == 't' else 's'
    bottle.response.set_header('Content-Type', 'text/plain; charset=UTF-8')
    if query:
        return base1k.b1kencode(query, style, 35) + '\n'
    else:
        return ''


@bottle.post('/b4kencode')
def b4kencode():
    query = bottle.request.forms.get('q', '').encode('latin1')
    style = 't' if bottle.request.forms.get('style') == 't' else 's'
    bottle.response.set_header('Content-Type', 'text/plain; charset=UTF-8')
    if query:
        return base1k.b4kencode(query, style, 35) + '\n'
    else:
        return ''


@bottle.post('/b1kdecode')
def b1kdecode():
    query = bottle.request.forms.get('q', '').encode('latin1').decode('utf-8')
    style = 't' if bottle.request.forms.get('style') == 't' else 's'
    bottle.response.set_header('Content-Type', 'application/octet-stream')
    if query:
        return base1k.b1kdecode(query, style)
    else:
        return b''


@bottle.post('/b4kdecode')
def b4kdecode():
    query = bottle.request.forms.get('q', '').encode('latin1').decode('utf-8')
    style = 't' if bottle.request.forms.get('style') == 't' else 's'
    bottle.response.set_header('Content-Type', 'application/octet-stream')
    if query:
        return base1k.b4kdecode(query, style)
    else:
        return b''

if __name__ == '__main__':
    bottle.run(port=8081)
