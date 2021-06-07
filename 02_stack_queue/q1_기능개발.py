def solution(progresses, speeds):
    answer = []

    
    for i in range(len(progresses)):
        progresses[i] += speeds[i]

    return answer

print(solution([93, 30, 55], [1, 30, 5]))