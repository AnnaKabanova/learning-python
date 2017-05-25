X = int(input())
H = int(input())
M = int(input())
sleeping_minutes = (M + X) % 60
sleeping_hours = H + (M + X) // 60 
print(sleeping_hours)
print(sleeping_minutes)
