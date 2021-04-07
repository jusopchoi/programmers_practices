def solution(genres, plays):
    answer = []
    songs = {}
    total = {}
    for idx in range(len(genres)):
        try:
            songs[genres[idx]].append([plays[idx], idx])
            total[genres[idx]] += plays[idx]
        except:
            songs[genres[idx]] = [[plays[idx], idx]]
            total[genres[idx]] = plays[idx]
    total = sorted(total.items(), key=lambda x:x[1], reverse=True)
    for s in total:
        genre = s[0]
        lists = songs[genre]
        lists = sorted(lists, key=lambda x:x[0], reverse=True)
        answer.append(lists[0][1])
        if len(lists) > 1:
            answer.append(lists[1][1])
    return answer
