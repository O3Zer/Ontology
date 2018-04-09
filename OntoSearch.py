from owlready2 import*
# Загрузка онтологии  
onto = get_ontology("file://C:/onto.owl").load()
while True:
    n = input ("Enter the query: ")
    k = onto.search(iri = "*" + n + "*")
    f = len(k)
    i = 0
    while i < f:
        print(i+1,'. ',k[i])
        i = i + 1
    num = int(input ("Enter the number: "))
    obj = k[num-1]
    if obj.comment:
        print(obj, " - ", obj.comment)
    # предыдущий субкласс:
    anc = list(obj.ancestors())
    print("Ancestors: ")
    f = len(anc)
    i = 0
    count = 1
    while i < f:
        if (anc[i] != obj) and (anc[i] != owl.Thing):
            print(count,'. ',anc[i])
            count = count + 1
        i = i + 1
    # последующий субкласс:
    des = list(obj.descendants())
    print("Descendants: ")
    f = len(des)
    i = 0
    count = 1
    while i < f:
        if (des[i] != obj) and (des[i] != owl.Thing):
            print(count,'. ',des[i])
            count = count + 1
        i = i + 1
