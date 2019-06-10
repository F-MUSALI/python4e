
str = 'XDSpan. CONFIDENTIAL: 8095'
nstr = str.find(':')
print(nstr)

nnstr = str[nstr+2 :]
print(nnstr)

numstr = float(nnstr)
nnumstr = numstr + 7000
print(nnumstr)
