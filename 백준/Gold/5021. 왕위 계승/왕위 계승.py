N, M = map(int, input().split())

anci = input()

family = {}

graph_people = [[0] * N for _ in range(N)]

for i in range(N):
    c, f, m = input().split()
    family[c] = (f, m)

king_score = {anci : 1,}

def get_score(name):
    if name in king_score:
        return king_score[name]
    
    if name not in family:
        return 0.0
    
    f, m = family[name]
    score = (get_score(f) + get_score(m)) / 2
    king_score[name] = score
    return score

is_king = []
for person in range(M):
    peop = input()
    is_king.append(peop)

king = ''
score = 0

for person in is_king:
    now_king = get_score(person)
    if score < now_king:
        score = now_king
        king = person
        
print(king)