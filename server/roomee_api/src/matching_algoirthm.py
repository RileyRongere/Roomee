#Matching Algorithm

#mock user list
user_list=[]


def sleep(user1, user2, score):
    if user1["sleep"]=user2["sleep"]:
        score=score+3
    if user1["sleep"]+1=user2["sleep"]:
        score=score+2
    if user1["sleep"]-1=user2["sleep"]:
        score=score+2
    if user1["sleep"]+2=user2["sleep"]:
        score=score+1
    if user1["sleep"]-2=user2["sleep"]:
        score=score+1
    retun score

def wake_up(user1,user2,score):
    if user1["wake"]=user2["wake"]:
        score=score+3
    if user1["wake"]+1=user2["wake"]:
        score=score+2
    if user1["wake"]-1=user2["wake"]:
        score=score+2
    if user1["wake"]+2=user2["wake"]:
        score=score+1
    if user1["wake"]-2=user2["wake"]:
        score=score+1
    return score
    
def pet(user1,user2,user_list):
    if user1["want_pets"]=0 and user2["have_pets"]=1:
        user_list.remove(user2)
    if user1["have_pets"]=1 and user2["want_pets"]=0:
        user_list.remove(user2)

def friends_over(user1,user2,score):
    if user1["friends"]=user2["friends"]:
        score=score+3
    if user1["friends"]+1=user2["friends"]:
        score=score+2
    if user1["friends"]-1=user2["friends"]:
        score=score+2
    if user1["friends"]+2=user2["friends"]:
        score=score+1
    if user1["friends"]-2=user2["friends"]:
        score=score+1
    return score

def smoking(user1,user2,user_list):
    if user1["smokes"]=1 and user2["allows_smoking"]=0:
        user_list.remove(user2)
    if user1["allows_smoking"]=0 and user2["smokes"]=1:
        user_list.remove(user2)

def intro_extro(user1,user2,user_list):
    if user1['type_e_i']=user2['type_e_i']:
        score=score+2

def main:
    high=[]
    med=[]
    low=[]
    for users in users_list:
        score=0
        smoking(user1,user,user_list)
        if user in user_list:
            pet(user1,user,user_list)
        if user in user_list:
            score1=intro_extro(user1,user,score)
            score2=friends_over(user1,user,score1)
            score3=wake_up(user1,user,score2)
            final_score=sleep(user1,user,score3)
            if final_score < 5:
                low.append(user)
            elif final_score > 0:
                high.append(user)
            else:
                med.append(user)



    