n, m = map(int, input().split())
grill_times = list(map(int, input().split()))

people_to_serve = m + 1


low = 1
high = min(grill_times) * people_to_serve
answer = high

while low <= high:
    mid_time = (low + high) // 2
    
    burgers_cooked = 0
    for cook_time in grill_times:
            burgers_cooked += mid_time // cook_time
            
    if burgers_cooked >= people_to_serve:
        answer = mid_time
        high = mid_time - 1
    else:
        low = mid_time + 1

print(answer)