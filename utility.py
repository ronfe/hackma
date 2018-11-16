import itertools 

def find_coline_point(setting, point_a, point_b):
    for each in setting[point_a]:
        if point_b in each:
            return point_a+each
    return ""

def judge_coline(setting, point_a, point_b):
    if point_a == point_b:
        return True
    
    k = ''
    for each in setting[point_a]:
        k += each
    return point_b in k


def find_alternative_segments(setting, point_a, point_b):
    k = None
    for elem in setting[point_a]:
        if point_b in elem:
            k = elem
            break
    j = itertools.permutations(k, 2)
    return list(j)


def addup_keyword(setting, goal, position):
    t = setting[position]
    for key in t:
        if goal in key:
            return key
    return None


def angle_tongwei(setting, parallel_a, parallel_b, angle_a, angle_b):
    ### 1 同位角顶点在一条线上
    top_a, top_b = angle_a[1], angle_b[1]
    seg_a, seg_b = find_coline_point(setting, parallel_a[0], parallel_a[1]), find_coline_point(setting, parallel_b[0], parallel_b[1])

    if top_a not in seg_a or top_b not in seg_b:
        return False
    
    ### 2. 构成同位关系
    #### 2.1 第1点共线
    first_a, first_b = angle_a[0], angle_b[0]
    if not judge_coline(setting, first_a, first_b):
        return False
    
    #### 2.2 第2-3点构成线段平行
    alt_a, alt_b = find_alternative_segments(setting, parallel_a[0], parallel_a[1]), find_alternative_segments(setting, parallel_b[0], parallel_b[1])
    if angle_a[1:] in alt_a and angle_b[1:] in alt_b:
        return True

    angle_a_23 = angle_a[1:]
    angle_b_23 = angle_b[1:]
    a,b = addup_keyword(setting, angle_a_23[1], angle_a_23[0]),addup_keyword(setting, angle_b_23[1], angle_b_23[0])
    direction_a = setting[angle_a_23[0]][a]
    direction_b = setting[angle_b_23[0]][b]

    if direction_a == direction_b:
        return True

    return False



##3.构成内错关系
def angle_neicuo(setting, parallel_a, parallel_b, angle_a, angle_b): #线AD 线BC 角DAC 角ACB
    ### 1 内错角顶点在一条线上
    top_a, top_b = angle_a[1], angle_b[1]  #顶点
    seg_a, seg_b = find_coline_point(setting, parallel_a[0], parallel_a[1]), find_coline_point(setting, parallel_b[0], parallel_b[1])
    
    ### 2. 构成内错关系
    #### 2.1  角23位 = 角12位    
    con_point_23, con_point_12 = angle_a[1:], angle_b[0:2]
    if not judge_presence(setting, con_point_23, con_point_12):
        return False
    
    #### 2.2 角12位 （同方向）平行 角23位
    alt_a, alt_b = find_alternative_segments(setting, parallel_a[0], parallel_a[1]), find_alternative_segments(setting, parallel_b[0], parallel_b[1])
    if angle_a[1:] in alt_a and angle_b[1:] in alt_b:
        return True

    angle_a_23 = angle_a[0:2]
    angle_b_23 = angle_b[1:]
    a,b = addup_keyword(setting, angle_a_23[1], angle_a_23[0]),addup_keyword(setting, angle_b_23[1], angle_b_23[0])
    direction_a = setting[angle_a_23[0]][a]
    direction_b = setting[angle_b_23[0]][b]

    if direction_a == direction_b:
        return True

    return False


def judge_presence(setting, point_a,point_b): #判断
    if point_a == point_b:
        return True
#判断两个角是某角的两个平分角 angle_a是大角
def angle_pingfenjiao(line_a, angle_a, angle_b, angle_c):
    if angle_a[1] == angle_b[1] == angle_c[1]:
        if angle_a[0] == angle_b[0]:
            if angle_b[2] == line_a[1]:
                    return True
            else: 
                return False
            # else: 
            #     return False
        elif angle_a[0] == angle_c[0]:
                if angle_b[0] == line_a[1]:
                    if angle_c[2] == line_a[1]:
                        return True
                    else: return False
                else: return False
        else: return False
    else: return False


def judge_buxianglinneijiaohe(angle_a):
    if angle_a[0] != "A":
        if angle_a[3] != "A":
            return False
        elif angle_a[4] == "B" and angle_a[5] == "C" and angle_a[0] == "B" and angle_a[1] =="C" and angle_a[2] == "A":
            return True
        else: 
            return False
    elif angle_a[1] == "B" and angle_a[2] =="C" and angle_a[3] == "B" and angle_a[4] == "C" and angle_a[5] == "A":
            return True
    else:
        return False
