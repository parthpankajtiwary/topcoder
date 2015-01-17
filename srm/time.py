
def convert(program):
    convertedProgram = [x for x in program.split("->")]
    return ".".join(convertedProgram)

program = "Test* t = new Test();","t->a = 1;","t->b = 2;","t->go(); // a=1, b=2 --> a=2, b=3"

print convert(program)
