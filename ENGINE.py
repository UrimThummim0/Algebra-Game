CONST_ = []
OP_ = []
VAR_ = []
EQ_SIGN_ = []

MAP = []
MAP_ = []



def recognition():
    IN_ = input("Enter an equation: ")
    for i, char in enumerate(IN_):
        if char in {'x', 'y', 'z'} | {'x'.upper(), 'y'.upper(), 'z'.upper()}:
            VAR_.append(char)
            MAP.append({"type": "variable", "value": char, "position": i})
            MAP_.append(MAP[i]["value"])

        elif char in {'+', '-', '*', '/'}:
            OP_.append(char)
            MAP.append({"type": "operator", "value": char, "position": i})
            MAP_.append(MAP[i]["value"])

        elif char == '=':
            EQ_SIGN_.append(char)
            MAP.append({"type": "equal_sign", "value": char, "position": i})
            MAP_.append(MAP[i]["value"])

        elif char.isdigit():
            CONST_.append(char)
            MAP.append({"type": "constant", "value": char, "position": i})
            MAP_.append(MAP[i]["value"])

        else:
            raise SyntaxError(f"Syntax Error")                

    

recognition()


TEXT = ''.join(MAP_)
print(f"Constants={CONST_}, Variables={VAR_}, Operators={OP_}, Equals={EQ_SIGN_}")

