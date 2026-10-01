import math

def solution(fees, records):
    in_time = {}
    total_minute = {}
    for r in records:
        time, car_num, status = r.split()
        h, m = map(int, time.split(":"))
        
        if status == 'IN':
            in_time[car_num] = h * 60 + m
        else:
            total_minute[car_num] = total_minute.get(car_num, 0) + h * 60 + m - in_time[car_num]
            in_time.pop(car_num)

    for car_num, time in in_time.items():
        total_minute[car_num] = total_minute.get(car_num, 0) + 23 * 60 + 59 - in_time[car_num]
    
    base_time, base_fee, unit_time, unit_fee = fees
    result = []
    for key, value in sorted(total_minute.items()):
        
        if value <= base_time:
            result.append(base_fee)
        else:
            calc_fee = base_fee + (math.ceil(((value - base_time) / unit_time)) * unit_fee)
            result.append(calc_fee)
            
    return result