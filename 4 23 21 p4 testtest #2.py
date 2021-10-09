listconv = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '00', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def alphabetize(x):
    b = []
    c = []
    e = []
    g = []
    h = []
    i = []
    j = ''
    k = []
    l = []
    v = []
    q = []
    aa = []
    ab = []
    ac = []
    ad = []
    ae = []
    af = []
    ag = []
    ah = ''
    aj = []
    longestword = max(x, key = len)
    a = len(longestword) + 1
    for y in range(0,len(x)):
        if not len(x[y]) == a:
            while not len(x[y]) == a:
                x[y] += ' '
        elif len(x[y]) == a:
            y += 1
    for y in range(0,len(x)):
        b += [list(x[y])]
        y += 1
    for y in range(0, len(x)):
        for d in range(0, len(x[y])):
            c += [listconv.index(x[y][d])]
            d += 1
        y += 1
    for y in range(0, len(c)):
        c[y] = c[y] + 27
        e += [c[y]]
        y += 1
    for y in range(0, len(c)):
        g += [listconv[c[y]]]
        y += 1
    for y in range(0, len(g)):
        h += [g[y:a+y]]
        y += a
    for y in range(0, len(x)):
        i += [h[( (len(x)-(1+y)) )*a]]
        y += 1
    for y in range(0, len(i)):
        j += ''.join(i[y]) + ' '
        y += 1
    for y in range(0, len(x)):
        k = j.index(' ')
        l += [int(j[0:k])]
        j = j[k+1:]
        y += 1
    while len(v) in range (0, len(x)):
        m = min(l)
        n = l.index(m)
        v += [l[n]]
        l = l[0:n] + l[n+1:]
    for y in range (0, len(x)):
        q += [str(v[y])]
        y = y + 1
    for y in range (0, len(q)):
        for d in range (0, len(q[y])):
            aa += [q[y][d:(d+2)]]
            d += 1
        y += 1
    for y in range (0, a*len(q)):
        ab += [aa[y*2]]
        y += 1
    for y in range (0, a*len(q)):
        ac += [listconv.index(ab[y])]
        y += 1
    for y in range (0, a*len(q)):
        ac[y] = ac[y] - 27
        ad += [ac[y]]
        y += 1
    for y in range (0, a*len(q)):
        ad[y] = listconv[ad[y]]
        ae += [ad[y]]
    for y in range(0, a*len(q)):
        af += [ae[0:a]]
        ae = ae[a:]
        y += 1
    ag = (af[0:len(x)])
    for y in range(0, len(x)):
        for o in range(0, a):
            ah += str(ag[y][o])
            o += 1
        ai = ah.replace('   ', '')
        y += 1
        aj = ai.replace('  ', ' ')
        ak = aj.replace(' ', ', ')
        al = ak[0:len(ak)-2]
    return(al)
print(alphabetize(['create', 'ascertain', 'bear', 'infinity', 'violence', 'hotdog', 'sweep', 'ascend']))
