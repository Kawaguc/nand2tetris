class Parser:

    def __init__(self, filepath):
        self.fd = open(filepath)
        self.current_command = None
        self.line_total = len(self.fd.readlines())
        self.fd.seek(0)
        self.line_count = 0
        self.A_COMMAND = 0
        self.C_COMMAND = 1
        self.L_COMMAND = 2

    def hasMoreCommands(self):
        return self.line_count < self.line_total

    def advance(self):
        self.current_command = self.fd.readline()
        # preprocess
        comment_idx = self.current_command.find('//')
        if comment_idx != -1:
            self.current_command = self.current_command[:comment_idx]
        self.current_command = self.current_command.strip()

        self.line_count += 1

    def commandType(self):

        if self.current_command == '':
            return ''

        if self.current_command[0] == '@':
            return self.A_COMMAND
        if ('=' or ';') in self.current_command: # ()で括らないと非空文字列がTrueと判定される
            return self.C_COMMAND
        if self.current_command[0] == '(':
            return self.L_COMMAND

    def symbol(self):
        return self.current_command.strip('()@')

    def dest(self):
        if not '=' in self.current_command:
            return ''
        return self.current_command.split('=')[0]

    def comp(self):
        tmp = self.current_command.split('=')[1]
        return tmp.split(';')[0]

    def jump(self):
        if not ';' in self.current_command:
            return ''
        return self.current_command.split(';')[1]
