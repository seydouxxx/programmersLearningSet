# 20210518
def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)

    for i in range(len(completion)):
        if (participant[i] != completion[i]): return participant[i]
    return participant[len(participant)-1]