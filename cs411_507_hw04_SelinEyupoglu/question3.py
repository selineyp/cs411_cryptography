n=11034161487924008937888796288635594662305126611335525532797034697845509223571277728323048152953068310859531889586217296715035312600843481743618690136264262700496164000119632383307688421790374437199120749531557591772271826954626172921932880153434766388699019537547728601006133987955409466414998624572957814418671716173114423991630349679058041627982381923256451621799559969296055454582455483052696861907245917938633986768518699318279981766966170781110844132095633681139589567818310285671505684210661452328098494053325629231247961415770546673634839221164242922757395108801581855418166879733623567828470384034830029933687
e=65537
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

cp=3873680249623467826367539364615622589341354860958676387978659380263546197984522526560815271059808890968051330871282433149509587198357995235098402597562394532942248440785823812744245775541457429705400656431200565210880345454073114392081573852975647397894188392554441729200872482027630124098341536309658821020887879754305515982200459718246770965592051443891902975413068576099241022023087113547866192282458339642152774673429640500380196758464923112739607056897968627591289881579460166394238775676402099831162820645802017259999853129954464949014713129189051795007415064128397315657343793939830810688657224114493477678984
p = egcd(n,cp)[0]
print("here is p:", p)
print("also q:", n//p)
