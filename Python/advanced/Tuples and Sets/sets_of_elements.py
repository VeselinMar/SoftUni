n, m = input().split()

n_set = set()
m_set = set()

for _ in range(int(n)):
    n_set.add(input())

for _ in range(int(m)):
    m_set.add(input())


nm_set = n_set & m_set
for x in nm_set:
    print(x)
