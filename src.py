c = [{
        "type": "101",
        "elems": ["AD", "BC"],
        "label": "AD∥BC"
    }]
r = [{
    "type": "301",
    "elems": ["EAD", "EBC"],
    "label": "∠EAD=∠EBC"
}]




def judge_type(_input, _output, index):

    theorem_type = {
    12: {
        "input": ["101"],
        "output": ["301"]
    }
}
    i, o = theorem_type[index]['input'], theorem_type[index]['output']
    flag_i = False
    flag_o = False
    
    for each in _input:
        if each['type'] in i:
            flag_i = True
            break

    for each in _output:
        if each['type'] in o:
            flag_o = True
            break
    
    return flag_i and flag_o



# judge_type(c, r, 12)