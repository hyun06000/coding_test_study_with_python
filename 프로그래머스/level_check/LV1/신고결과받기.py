def solution(id_list, report, k):
    mail_id = dict()
    mail_count = dict()
    for _id in id_list:
        mail_id.update({_id:set()})
        mail_count.update({_id:0})
    
    for rep in report:
        sub, obj = rep.split(" ")
        mail_id[obj].add(sub)
    
    for _id in id_list:
        if len(mail_id[_id]) >= k:
            for send_back in mail_id[_id]:
                mail_count[send_back] += 1
    answer = []
    for _id in id_list:
        answer.append(mail_count[_id])
    
    print(mail_id)
    print(mail_count)
    print(answer)
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
solution(id_list, report, k)