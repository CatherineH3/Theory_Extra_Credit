# Catherine Healy
# Theory of Computing Extra Credit
# CFG --> Chomsky Normal Form
# All grammars go either to a single letter or two other variables
# 108 Textbook
# Algorithm on Page 110-
# Input a CFG and generate something in Chomsky Normal Form

import csv
# This is a list of new characters that we will use to make new rules. This isn't a super long list right now, but more could be added if we want to expand teh capabilities of the program
new_rules_nonterminals = ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

file_name = 'test_chealy5.csv'

def main():
    # Create a dicitonary to hold all of the rules of the CFG. Assume the input is formatted and matches the input case
    # Step 1: Read in all the information into a dictionary!
    cfg = {}
    with open(file_name, mode = 'r')as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            key = row[0].strip()
            values = [value.strip() for value in row[1:]]
            cfg[key] = values

    with open('trace_output_chealy5.txt', mode='w') as file:
        file.write("Initial Input\n")
        file.write("-------------------------------------------------------------------------")
     # Print the formatted output (print S0)
        for key, value in cfg.items():
            if key == 'S0':
                file.write(f'{key} --> {" | ".join(value)}')

        # Print the formatted output
        for key, value in cfg.items():
            if key != 'S0':
                file.write("\n")
                file.write(f'{key} --> {" | ".join(value)}')
        file.write("\n")
        file.write("-------------------------------------------------------------------------")
        file.write("\n")

    # Step 2: Add production rule S0-->S
    cfg['S0'] = ['S']


    with open('trace_output_chealy5.txt', mode='a') as file:
        file.write("\n")
        file.write("Step 1: Add the starting produciton rule (ex: S0-->S)\n")
     # Print the formatted output (print S0)
        for key, value in cfg.items():
            if key == 'S0':
                file.write(f'{key} --> {" | ".join(value)}')

        # Print the formatted output
        for key, value in cfg.items():
            if key != 'S0':
                file.write("\n")
                file.write(f'{key} --> {" | ".join(value)}')

        file.write("\n")


    # Step 3: Remove all epsilon productions X --> e (note that e stands for epsilon)
    # Loop through the list of values for each. For each epsilon found (1) remove it... Go through all other values of that
    # key add add a version without the key. it anything has just that key, then add an epsilon

    for key, values in cfg.items():
        for val in values:
            if val == 'e': # epsilon found
                #remove the e from the list
                values.remove('e')
                # keep track of the key that had the value
                special_key = key
                # Iterate through the other rules (nested loop). If the special key occurs, add a rule without it
                for key, values in cfg.items():
                    for val in values:
                        if special_key in val:
                            if special_key != val:
                                new_val = val.replace(special_key, '')
                                cfg[key].append(new_val)
                            else:
                                cfg[key].append('e') # Add an epsilon if special key occurs alone

    with open('trace_output_chealy5.txt', mode='a') as file:
        file.write("\n")
        file.write("Step 2: Remove all epsilon productions (ex: A-->e)\n")
     # Print the formatted output (print S0)
        for key, value in cfg.items():
            if key == 'S0':
                file.write(f'{key} --> {" | ".join(value)}')

        # Print the formatted output
        for key, value in cfg.items():
            if key != 'S0':
                file.write("\n")
                file.write(f'{key} --> {" | ".join(value)}')

        file.write("\n")


       # Step 4: Remove all unit productions
       # Steps: Search for a unit production. If any individual captial letters, then append the whole list of rules to it
    for key, values in cfg.items():
       for val in values:
        if len(val) ==1 and val.isupper(): # Captial letter of length 1 and not start
            unit_rule = val
            # Remove the letter form the list
            values.remove(val)
            if (key != val):
            # Append the unit rule of that letter to the list
                cfg[key] = cfg[key] + cfg[unit_rule]


    with open('trace_output_chealy5.txt', mode='a') as file:
        file.write("\n")
        file.write("Step 3: Replace all unit productions (ex: B-->A \n")
     # Print the formatted output (print S0)
        for key, value in cfg.items():
            if key == 'S0':
                file.write(f'{key} --> {" | ".join(value)}')

        # Print the formatted output
        for key, value in cfg.items():
            if key != 'S0':
                file.write("\n")
                file.write(f'{key} --> {" | ".join(value)}')

        file.write("\n")



    #  Step 5: Look for terminal and nonterminal mixes: A--> aAS
    for key, values in cfg.copy().items():
        for val in values:
            lowercase = 0
            uppercase = 0
            found = False
            for char in val:

                if char.islower():
                    lowercase += 1
                    lowercase_char = char
                elif char.isupper():
                    uppercase += 1
                if lowercase > 0 and uppercase > 0:    # Identify cases with mixed terminals and nonterminals

                    for second_key, second_val in cfg.copy().items():
                        if cfg[second_key]==[lowercase_char]:
                            found = True
                            break;

                    if found:
                        mixed_nonterm_term_val = val.replace(lowercase_char, second_key)
                        cfg[key].remove(val)
                        cfg[key].append(mixed_nonterm_term_val)
                        break;

                    else:
                        # remove a value from the list of new_rules_nonterminals
                        new_rule = new_rules_nonterminals.pop()
                        cfg[new_rule] = [lowercase_char]
                        # # Now go back and replace lowercase with symbol
                        mixed_nonterm_term_val = val.replace(lowercase_char, new_rule)
                        cfg[key].remove(val)
                        cfg[key].append(mixed_nonterm_term_val)
                        break



    with open('trace_output_chealy5.txt', mode='a') as file:
        file.write("\n")
        file.write("Step 4: Replace productions with mixed nonterminals and terminals (ex: aAS\n")
     # Print the formatted output (print S0)
        for key, value in cfg.items():
            if key == 'S0':
                file.write(f'{key} --> {" | ".join(value)}')

        # Print the formatted output
        for key, value in cfg.items():
            if key != 'S0':
                file.write("\n")
                file.write(f'{key} --> {" | ".join(value)}')

        file.write("\n")


    # Step 6: Look for production rules with more than 2 terminals: B--> bb
    for key, values in cfg.copy().items():
        for val in values:
            lowercase = 0
            for char in val:
                if char.islower():
                    lowercase += 1
                    lowercase_char = char
                if lowercase > 1:
                    new_rule = new_rules_nonterminals.pop()
                    cfg[new_rule] = [lowercase_char]
                    double_nonterm = val.replace(char, new_rule)
                    cfg[key].remove(val)
                    cfg[key].append(double_nonterm)
                    break;




    with open('trace_output_chealy5.txt', mode='a') as file:
        file.write("\n")
        file.write("Step 5: Replace productions with more than 2 terminals (B-->bb)\n")
     # Print the formatted output (print S0)
        for key, value in cfg.items():
            if key == 'S0':
                file.write(f'{key} --> {" | ".join(value)}')

        # Print the formatted output
        for key, value in cfg.items():
            if key != 'S0':
                file.write("\n")
                file.write(f'{key} --> {" | ".join(value)}')

        file.write("\n")


    # Step 7: Look for more than 2 nonterminals.
    for key, values in cfg.copy().items():
        for val in values:
            nonterminals = 0
            nonterminal_list = []
            for char in val:
                charlist = []
                if char.isupper():
                    nonterminals += 1
                    if len(nonterminal_list) == 0:
                        nonterminal_list.append(val)
                if nonterminals > 2:
                    new_rule = new_rules_nonterminals.pop()
                    result = ''.join(nonterminal_list[0][:2])
                    cfg[new_rule] = [result]
                    new_val = val.replace(result, new_rule)
                    cfg[key].remove(val)
                    cfg[key].append(new_val)

                    break


    with open('trace_output_chealy5.txt', mode='a') as file:
        file.write("\n")
        file.write("Step 6: Replace rules with more than 2 nonterminals (ex: S-->ASB)\n")
        # Print the formatted output (print S0)
        for key, value in cfg.items():
            if key == 'S0':
                file.write(f'{key} --> {" | ".join(value)}')

        # Print the formatted output
        for key, value in cfg.items():
            if key != 'S0':
                file.write("\n")
                file.write(f'{key} --> {" | ".join(value)}')

        file.write("\n")



    # Print the formatted output (print S0)
    for key, value in cfg.items():
        if key == 'S0':
            print(f'{key} --> {" | ".join(value)}')

    # Print the formatted output
    for key, value in cfg.items():
        if key != 'S0':
            print(f'{key} --> {" | ".join(value)}')

        # Print the formatted output
        # for key, value in cfg.items():
        #     print(f'{key} --> {" | ".join(value)}')

    with open('trace_output_chealy5.txt', mode='a') as file:
        file.write("\n")
        file.write("Final Results\n")
        file.write("-------------------------------------------------------------------------")
        file.write("Final results:\n")
        # Print the formatted output (print S0)
        for key, value in cfg.items():
            if key == 'S0':
                file.write(f'{key} --> {" | ".join(value)}')

        # Print the formatted output
        for key, value in cfg.items():
            if key != 'S0':
                file.write("\n")
                file.write(f'{key} --> {" | ".join(value)}')


if __name__ == '__main__':
    main()


############# Description of cases that I will consider
# Add production rule S0 --> S
# Remove all epsilon productions X --> e
# Remove all unit productions (these are any single capital letters on the right side)
# Look for terminals mixed with nonterminals
    #If there is not a rule for a terminal going to a signle nonterminal (ex: X--> a), add them. Then, go and replace the nonterminal with that rule so S-->AaS is S-->AXS
# look for two terminals in a row. Replace them with some nonterminals. (Can use repeats) A--> bb goes to A-->VV is V --> b
# Look for more than 2 Nonterminals. A-->XAS Take the first two and make a new rule that points to the first one. Z --> XA Then replace the first two with that rule and you can keep the first the same A--> ZS
