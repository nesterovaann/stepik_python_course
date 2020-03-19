students = list()
with open('input.txt', 'r') as data:  
    for line in data:
        line = line.strip()
        if not line:
            continue
      
        parts = line.split(';')
        name = parts[0]
        rating = list(map(int, parts[1:]))
        mean = sum(rating) / len(rating)
      
        students.append(
            (name, rating, mean)
        )
with open('output.txt', 'w') as out:
    for st in students:
        out.write(str(round(st[-1], 9)))
        out.write('\n')
  
    for i in range(len(rating)):
        p = [s[1][i] for s in students]
        out.write(str(round(sum(p) / len(p), 9)))
        out.write(' ')
