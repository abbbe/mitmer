d = p.discrepancies()
print d

while True:
        (d, nd) = p.new_discrepancies(d)
        print nd
        fr = p.fix(d)
        print fr

