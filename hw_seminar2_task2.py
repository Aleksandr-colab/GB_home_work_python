# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f =  ((not x or y ) and (not y or w)) or (z == ( x or y))
                if not f: print(x,y,z,w)