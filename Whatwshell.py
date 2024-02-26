

def esoteric_interpreter(code: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    idx = 0
    output = []
    in_brackets = False
    for char in code:
        if char == '{':
            in_brackets = True
            continue
        elif char == '}':
            in_brackets = False
            continue

        if in_brackets:
            output.append(char)
            continue

        if char in (' ', '(', ')', '“', '”'):
            output.append(char.replace('“', '"').replace('”', '"'))
        elif char == '?':
            idx = (idx + 1) % 26
        elif char == '~':
            idx = (idx - 1) % 26
        elif char == '`':
            idx = (idx + 4) % 26
        elif char == '@':
            idx = (idx - 4) % 26
        elif char == '_':
            idx = 13
        elif char == 'é':
            idx = 0
        elif char == '$':
            output.append(alphabet[idx])

    # translated_code = ''.join(output)
    # print(f"Translated Code: {translated_code}")  # Debug line to print the translated code
    # return translated_code
    return ''.join(output)


def custom_print(s):
    # Convert the special characters “” to standard quotes
    cleaned_string = s.replace("“", '"').replace("”", '"')
    exec(f"print({cleaned_string})")

def custom_for(args_str):
    # Assuming the structure is for variable_name in range(int): command
    # Example: "i in range(5): print(\"what\")"
    
    var_name, rest = args_str.split(' in ')
    _, loop_range, command = rest.split(' ', 2)

    # Removing "range(" and ")" to get the actual range value
    loop_count = int(loop_range[len("range("):-1])

    # Removing colon to get the actual command
    command = command.strip(':').strip()

    # Iterate and execute the command
    for _ in range(loop_count):
        # Extracting the function name and its arguments
        func_name = command.split('(')[0]
        command_args = command[command.index('(')+1:-1] 
        
        # Execute the command
        COMMANDS[func_name](command_args)

# Define a mapping of commands to functions
COMMANDS = {
    'print': custom_print,
    'for': custom_for,
    # 'in': custom_print,
    # 'range': custom_print,

}

def main():
    while True:
        try:
            esoteric_code = input('>>> ')
            if not esoteric_code:
                continue

            command_str = esoteric_interpreter(esoteric_code)

            # Check if it's a recognized command with arguments
            if '(' in command_str and ')' in command_str:
                func_name = command_str.split('(')[0]
                args_str = command_str[command_str.index('(')+1:-1]  # Extracting everything between ( and )

                # Check if the command is in the mapping
                if func_name in COMMANDS:
                    COMMANDS[func_name](args_str)


            else:
                # Handle cases without arguments, if needed
                print(f"Unrecognized command: {command_str}")

        except KeyboardInterrupt:
            print("\nExiting the Esoteric shell.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()

#_??$_`$_@~$_$_`??$(“é`???$é`$_~~$_~~$_?$ _``?$_?$_`$_~~$é???$”) print("hello world") -> hello world

#a = é$
#b = é?$
#c = é??$
#d = é`~$
#e = é`$
#f = é`?$
#g = é`??$
#h = é``~$
#i = _@~$
#j =_@$ 
#k =_@?$
#l =_~~$
#m =_~$
#n = _$
#o = _?$
#p = _??$
#q = _`~$
#r = _`$
#s = _`?$
#t = _`??$
#u = _``~$
#v = _``$
#w = _``?$
#x = _``??$
#y = _```~$
#z = _````$

#patrick = _??$é$_`??$_`$_@~$é??$_@?$

# é`?$_?$_`$ _@~$ _@~$_$ _`$é$_$é`??$é`$(5):
#     _??$_`$_@~$_$_`??$(“_``?$é``~$é$_`??$“)

#     this should be equivalent to 

# for i in range(5):
#     print("what")

#     and I want it to run this whit results in this printint to console in the shell:

#     what
#     what
#     what
#     what
#     what



