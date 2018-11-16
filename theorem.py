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
    
    
    


if __name__ == '__main__':
    c = {
        "type": "101",
        "elems": ["AD", "BC"],
        "label": "AD∥BC"
    }
    r = {
        "type": "301",
        "elems": ["DAC", "ACB"],
        "label": "∠EAD=∠EBC"
    }
    print(T12(setting, conditions=[c], claims=[r]))