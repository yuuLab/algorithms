N = int(input())
players = list(map(int, input().split()))

def tournament(player_list):
    left_block_winner = max(players[:2**(N-1)])
    right_block_winner = max(players[2**(N-1):])
    if left_block_winner < right_block_winner:
        for i in range(len(player_list)):
            if player_list[i] == left_block_winner:
                print(i+1)
    else:
        for i in range(len(player_list)):
            if player_list[i] == right_block_winner:
                print(i+1) 
tournament(players)