import parser
import code

filepath = 'add/Add.asm'
savepath = filepath.replace('.asm','.hack')
p = parser.Parser(filepath)
c = code.Code()


def int2bin(num):
    return '0'*(16-len(bin(num)[2:])) + bin(num)[2:]


with open(savepath,'w') as fw:
    while p.hasMoreCommands():

        p.advance()
        if p.commandType() == p.A_COMMAND:
            print('current:',p.current_command)
            print('symbol:',p.symbol())
            print(f'binary:{int2bin(int(p.symbol()))}')
            print()
            fw.write(int2bin(int(p.symbol()))+'\n')
        elif p.commandType() == p.C_COMMAND:
            print(f'current:{p.current_command}')
            print(f'comp:{p.comp()}')
            print(f'dest:{p.dest()}')
            print(f'jump:{p.jump()}')
            line = '111'+c.comp(p.comp()) + c.dest(p.dest()) + c.jump(p.jump())
            print(f'binary:{line}')
            print()

            fw.write(line+'\n')

        elif p.commandType() == p.L_COMMAND:
            print(p.current_command)

            line = '111'+c.comp(p.comp()) + c.dest(p.dest()) + c.jump(p.jump())
            print(line)
            fw.write(line+'\n')



