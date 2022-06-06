directions = ['n', 's', 's', 's', 'e', 'w']
ns = 0
ew = 0
for dir in directions:
    if dir == 'n':
        ns += 1
    elif dir == 's':
        ns -= 1
    elif dir == 'e':
        ew += 1
    elif dir == 'w':
        ew -= 1
final_dir = []
if ns > 0:
    final_dir += ['n'] * ns
else:
    final_dir += ['s'] * ns
if ew > 0:
    final_dir += ['e'] * ew
else:
    final_dir += ['w'] * ew
