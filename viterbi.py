# conding: utf-8


states = ('AT', 'BEZ', 'IN', 'NN', 'VB')

observations = ('bear', 'is', 'move', 'on', 'president', 'progress', 'the')

start_probability = {'AT': 0.2, 'BEZ':0.1, 'IN':0.1, 'NN':0.2, 'VB':0.3}

transition_probability = {'AT': {'AT': 2.05588e-5, 'BEZ': 2.05588e-5, 'IN': 2.05588e-5, 'NN': 0.999917765, 'VB': 2.05588e-5},
                          'BEZ': {'AT': 0.761868005, 'BEZ': 0.000385951, 'IN': 0.164801235, 'NN': 0.072558858, 'VB':0.000385951 },
                          'IN': {'AT': 0.699141465, 'BEZ': 1.61379e-5, 'IN': 0.021398832, 'NN': 0.279427428, 'VB':1.61379e-5},
                          'NN': {'AT': 0.017904743, 'BEZ': 0.062381599, 'IN': 0.712015289, 'NN': 0.197388053, 'VB': 0.010310315},
                          'VB': {'AT': 0.486540618, 'BEZ': 0.003444961, 'IN': 0.381269027, 'NN': 0.118330396, 'VB': 0.010414998}}

emission_probability = {'AT': {'bear': 1.44879e-05 , 'is': 1.44879e-05, 'move': 1.44879e-05, 'on':  1.44879e-05,'president': 1.44879e-05, 'progress': 1.44879e-05, 'the': 0.999913072},
                        'BEZ': {'bear': 9.95851e-5 , 'is': 0.999404289, 'move': 9.95851e-5, 'on':  9.95851e-5,'president': 9.95851e-5, 'progress': 9.95851e-5, 'the': 9.95851e-5},
                        'IN': {'bear': 0.000182116, 'is': 0.000182116, 'move': 0.000182116, 'on':  0.998907303,'president': 0.000182116, 'progress': 0.000182116, 'the': 0.000182116},
                        'NN': {'bear': 0.020257827 , 'is': 0.001841621, 'move': 0.068139963, 'on': 0.001841621,'president': 0.7053407, 'progress': 0.200736648, 'the': 0.001841621},
                        'VB': {'bear': 0.235294118 , 'is': 0.005347594, 'move': 0.71657754, 'on': 0.005347594,'president': 0.005347594, 'progress': 0.026737968, 'the': 0.005347594}}


def Viterbit(obs, sta, s_pro, t_pro, e_pro):
    path = { s:[] for s in states}
    curr_pro = {}
    for s in sta:
        curr_pro[s] = s_pro[s]*e_pro[s][obs[0]]
    # print(curr_pro)
    for i in xrange(1, len(obs)):
        last_pro = curr_pro
        curr_pro = {}
        for curr_sta in sta:
            max_pro, last_sta = max(((last_pro[l_state]*t_pro[l_state][curr_sta]*e_pro[curr_sta][obs[i]], l_state)
                                   for l_state in sta))
            curr_pro[curr_sta] = max_pro
            path[curr_sta].append(last_sta)
            # print (path)

    max_pro = 0
    max_path = None
    for s in states:
        path[s].append(s)
        if curr_pro[s] > max_pro:
            max_path = path[s]
            max_pro = curr_pro[s]
        print (str(path[s]) + ":" +  str(curr_pro[s]))
    return max_path

if __name__ == '__main__':
    sentence = "The bear is on the move."
    sentence = sentence.replace(".","")
    sentence = sentence.lower()
    sen_list = sentence.split()
    # for i in sen_list[len(sen_list)-1]:
    #     # print(i)
    #     if i.islower():
    #         pass
    #     else:
    #         a = i
    #         sen_list[len(sen_list)-1] = sen_list[len(sen_list)-1].replace(a,'')
    #         sen_list.append(a)

    max_path =  Viterbit(sen_list, states, start_probability, transition_probability, emission_probability)
    for i in range(len(max_path)):
        print(sen_list[i] + "/" + max_path[i]),