import theorem

setting = theorem.setting

practice_log = [
    {
        "dueto": [{"type": "309", "elems": ['EAC', '△ABC'], 'label': '∠EAC是△ABC的外角'}],
        "therefore": [{"type": "301", "elems": ['EAC', 'ABC', 'BCA'], 'label': '∠EAC=∠ABC+∠BCA'}]
    },
    {
        "dueto": [{"type": "101", "elems": ["AD", "BC"], "label": "AD∥BC"}],
        "therefore": [{"type": "301", "elems": ["EAD", "ABC"], "label": "∠EAD=∠ABC"}]
    }
]

all_theorem = [
    theorem.T12, theorem.TD311, theorem.T13, theorem.T20, theorem.Replace
]


def judge_step_correct(step, setting):
    for func in all_theorem:
        x = func(setting, conditions=step['dueto'], claims=step['therefore'])
        if x == True:
            return True
    return False


def rater(practice_log, setting):
    # some code
    step_correctness = list()
    error_claims = list()
    for step in practice_log:
        x = [t in error_claims for t in step['dueto']]
        if sum(x) > 0:
            step_correctness.append(False)
            error_claims += step['therefore']
            continue
        k = judge_step_correct(step, setting)
        if k == False:
            error_claims += step['therefore']
        step_correctness.append(k)
    return {
        "score": sum(step_correctness),
        "correct": step_correctness
    }

if __name__ == '__main__':
    print(rater(practice_log, setting))