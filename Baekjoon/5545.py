num_of_topping = int(input())
cost_of_dough, cost_of_topping = map(int, input().split(' '))
cal_of_dough = int(input())

cal_of_topping_list = []
for _ in range(num_of_topping):
    cal_of_topping_list.append(int(input()))

cal_of_topping_list.sort(reverse=True)

total_cal = cal_of_dough
total_cost = cost_of_dough

cal_per_cost = total_cal // total_cost
for cal_of_topping in cal_of_topping_list:
    total_cal += cal_of_topping
    total_cost += cost_of_topping

    if cal_per_cost > total_cal // total_cost:
        break
    cal_per_cost = total_cal // total_cost

print(cal_per_cost)