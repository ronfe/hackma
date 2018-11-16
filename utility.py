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
    ### 1 同位角顶点需分别在线上
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


#判断两个角是某角的两个平分角 angle_a是大角
def angle_pingfenjiao(line_a, angle_a, angle_b, angle_c):
    if angle_a[1] == angle_b[1] == angle_c[1]:
        if angle_a[0] == angle_b[0]:
            if angle_b[2] == line_a[1]:
                if angle_c[0] == line_a[1]:
                    return True
                else: return False
            else: return False
        elif angle_a[0] == angle_c[0]:
                if angle_b[0] == line_a[1]:
                    if angle_c[2] == line_a[1]:
                        return True
                    else: return False
                else: return False
        else: return False
    else: return False
