f = open('numerology.html', 'r', encoding='utf-8')
c = f.read()
f.close()

marker = 'id="grand-master"'
idx = c.find(marker)
print('id=grand-master at:', idx)
if idx != -1:
    print(repr(c[idx:idx+300]))
else:
    print('NOT FOUND')

# Also check for data-program
marker2 = 'data-program="grand-master"'
idx2 = c.find(marker2)
print('data-program=grand-master at:', idx2)
if idx2 != -1:
    print(repr(c[idx2:idx2+100]))

# Check for Advanced
adv = c.find('(Advanced)')
print('(Advanced) at:', adv)
if adv != -1:
    print(repr(c[adv-50:adv+50]))

# Check for tier-grand-master
tgm = c.find('tier-grand-master')
print('tier-grand-master at:', tgm)

# Check for col-grand-master
cgm = c.find('col-grand-master')
print('col-grand-master at:', cgm)

# Check for Extended 48
e48 = c.find('Extended 48')
print('Extended 48 at:', e48)
