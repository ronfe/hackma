import utility
import src


setting = {
    "A": {
        "B": "3",
        "F": "IV",
        "C": "4",
        "D": "I",
        "E": "1"
    },
    "B": {
        "FC": "I",
        "AE": "1"
    },
    "C": {
        "A": "2",
        "FB": "III"
    },
    "D": {
        "A": "III"
    },
    "E": {
        "AB": "3"
    },
    "F": {
        "A": "II",
        "B": "III",
        "C": "I"
    }
}


def T12(setting, **kwargs):
    '''
        两直线平行，同位角相等
        1-to-many
        rtype: bool
    '''
    condition = kwargs['conditions'][0]
    claims = kwargs['claims'][0]
    k = src.judge_type([condition], [claims], 12)
    if k == False:
        return k
    
    k = utility.angle_tongwei(setting, 
        condition['elems'][0], 
        condition['elems'][1],
        claims['elems'][0],
        claims['elems'][1]
        )
    return k

def TD311(setting, **kwargs):
    '''
        角平分线的定义
        1-to-many
        rtype: bool
    '''
    condition = kwargs['conditions'][0]
    claims = kwargs['claims'][0]
    k = src.judge_type([condition], [claims], 99311)
    if k == False:
        return k
    #判断两个角是某个角的角平分角
    k = utility.angle_pingfenjiao(condition['elems'][0], 
        condition['elems'][1],
        claims['elems'][0],
        claims['elems'][1]
        )
    return k


def T13(setting, **kwargs):
    '''
        两直线平行，内错角相等
        1-to-many
        rtype: bool
    '''
    condition = kwargs['conditions'][0]
    claims = kwargs['claims'][0]
    k = src.judge_type([condition], [claims], 13)
    if k == False:
        return k
    
    t = utility.angle_neicuo(setting, condition['elems'][0], condition['elems'][1], claims['elems'][0], claims['elems'][1])
    return t


def T20 (setting, **kwargs):
    '''
        三角形外角等于不相邻的两个内角和
        1-to-many
        rtype: bool
    '''
    condition = kwargs['conditions'][0]
    claims = kwargs['claims'][0]
    k = src.judge_type([condition], [claims], 20)
    if k == False:
        return k
    #判断是两个不相邻内角和
    k = utility.judge_buxianglinneijiaohe(claims['elems'][1])
    return k

def Replace(setting, **kwargs):
    conditions = kwargs['conditions'] + kwargs['claims']
    flag = conditions[0]['type']
    for each in conditions[1:]:
        if flag != each['type']:
            return False

    return True
    

if __name__ == '__main__':
    c = {
        "type": "306",
        "elems": ["EAC", "TABC"],
        "label": "∠EAC是三角形ABC的外角"
    }
    r = {
        "type": "301",
        "elems": ["EAC", "ABCBCA"],
        "label": "∠EAC=∠ABC+∠BCA"
    }
    
    print(T20(setting, conditions=[c], claims=[r]))
