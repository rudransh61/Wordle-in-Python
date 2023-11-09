# print('hw')


def matchings_positions(str,answer):
    correct = []
    diffpos = []
    for i in range(len(str)):
        try:
            if str[i]==answer[i]:
                correct.append(str[i])
            elif str[i] in answer :
                diffpos.append(str[i])
        except:
            pass

    return correct,diffpos