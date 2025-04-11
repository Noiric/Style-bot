from database import create_tables
import dao

create_tables()
# dao.create_product('NewBalance', 'top', 2000, 'ddd', 4, 'ff', 'rr')
print(999999999999999)
print(str(dao.get_all_product()))
p = dao.get_product_by_name('bAl')
if p:
    for m in p:
        print(True, m.name)
else:
    print(False)

o = dao.get_product_by_price(2000)
if o:
    for m in o:
        print(True, m.price)
else:
    print(False)


t = dao.get_product_by_type('rr')
if t:
    for m in t:
        print(True, m.category_clothing)
else:
    print(False)


