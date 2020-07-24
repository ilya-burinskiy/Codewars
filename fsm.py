class FSM(object):


    def __init__(self, instructions):
        self.create_transit_table(instructions)

    def run_fsm(self, start, sequence):
        q0 = start
        path = []
        path.append(q0)

        for input_symbol in sequence:
            q = self.delta(q0, input_symbol)
            q0 = q
            path.append(q0)
        
        fin_state_val = self.transition_table[q0][2]
        return q0, fin_state_val, path

    def create_transit_table(self, instructions):
        self.transition_table = {}

        instructions = instructions.replace(' ', '')
        instructions = instructions.split('\n')
        for i in range(len(instructions)):
            instructions[i] = instructions[i].split(';')
            instructions[i][1] = instructions[i][1].split(',')
            self.transition_table[instructions[i][0]] = (*(instructions[i][1]),
                instructions[i][2])


    def delta(self, curr_state, input_symbol):
        new_state = self.transition_table[curr_state][input_symbol]
        return new_state


instructions = \
'''S1; S1, S2; 9
S2; S1, S3; 10
S3; S4, S3; 8
S4; S4, S1; 0'''

fsm = FSM(instructions)

sequence = [0, 1, 1, 0, 1]
fin_state, fin_state_val, path = fsm.run_fsm('S1', sequence)
print(fin_state, fin_state_val, path)