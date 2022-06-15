# 프로그래머스

## [2022 신고 결과 받기](https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3)



```python
def solution(id_list, report, k):
    dic = {}            # {ids : reported_user}
    dic_reverse = {}    # {ids : users_reported_cnt}
    dic_answer = {}     # {ids : received_email_cnt}
    serious_user = []   # reported k times or more
    
    for ids in id_list:  # make a dictionary
        dic[ids] = []
        dic_reverse[ids] = 0
        dic_answer[ids] = 0
    
    for r in report:    # a-b pairs become key-value in dictionary
        a, b = r.split()
        dic[a].append(b)
    
    for ids in id_list:  # remove duplicates using set
        dic[ids] = list(set(dic[ids]))
    
    for ids, reported_user in dic.items():  
        for ru in reported_user:
            dic_reverse[ru] += 1    # reported count of users in dic_reverse
        
    for reported_user, cnt in dic_reverse.items():
        if cnt < k:
            pass
        else:
            serious_user.append(reported_user)
    
    for ids, reported_user in dic.items():
        for ru in reported_user:
            if ru in serious_user:
                dic_answer[ids] += 1    # email count of users in dic_answer
                    
    answer = list(dic_answer.values())  # from dict to list
    
    return answer
```

