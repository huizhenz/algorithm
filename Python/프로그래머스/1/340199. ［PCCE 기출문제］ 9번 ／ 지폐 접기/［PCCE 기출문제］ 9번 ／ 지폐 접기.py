def solution(wallet, bill):
    wallet.sort()
    bill.sort()
    answer = 0

    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
        bill.sort()
        
    return answer