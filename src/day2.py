from src.utils import get_input_data


def run_program(program):
    i = 0
    seq = program[i:i + 4]
    while seq[0] != 99:
        program = run_step(program, seq)
        i += 4
        seq = program[i:i + 4]
    return program


def run_step(program, seq):
    t, in1, in2, out = seq
    if t == 1:
        program[out] = program[in1] + program[in2]
    elif t == 2:
        program[out] = program[in1] * program[in2]
    else:
        raise ValueError(f"Unknown instruction type: {t}")
    return program


def run_noun_verb(noun, verb, program):
    program[1] = noun
    program[2] = verb
    return run_program(program)


def check_noun_verb(program, val):
    for n in range(0, 100):
        for v in range(0, 100):
            d = program.copy()
            answer = run_noun_verb(n, v, d)[0]
            if answer == val:
                return (100 * n) + v
    raise ValueError(f"Did not find value {val}")


if __name__ == "__main__":
    input_data = get_input_data("input2.txt")
    data = [int(i) for i in input_data[0]]
    answer1 = run_noun_verb(12, 2, data.copy())[0]
    answer2 = check_noun_verb(data, 19690720)

    print(answer1)
    print(answer2)
