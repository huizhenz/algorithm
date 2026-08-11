def solution(participant, completion):
    players = {}
    
    for name in participant:
        players[name] = players.get(name, 0) + 1
    
    for name in completion:
        players[name] -= 1
        
    for name in players:
        if players[name] > 0:
            return name