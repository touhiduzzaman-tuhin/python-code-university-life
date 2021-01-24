from collections import deque

bank = deque([])

bank.append(1)
bank.append(2)
bank.append(3)
bank.append(4)
bank.append(5)

print(bank)

bank.popleft()

print(bank)

bank.popleft()
bank.popleft()
bank.popleft()
bank.popleft()

if not bank:

    print("Empty List")