import problems
import sys


def main():
    args = sys.argv[1:]
    nb_args = len(args)
    if nb_args == 0:
        print(
            "\nError in arguments.\n\nSpecify which problems you want to solve.\nExamples:\n\tmain.py 1 2 3 (solve problems 1, 2 and 3)\n\tmain.py all (solve all problems)\n"
        )
    elif args[0] == "all" and nb_args == 1:
        for name, value in vars(problems).items():
            value()

    else:
        try:
            for arg in args:
                int(arg)
            # print(args)  # Process arguments
            found = []
            not_found = []
            for arg in args:
                for name, value in vars(problems).items():
                    if name == "solve" + arg:
                        value()
                        found.append(arg)
            for arg in args:
                if not (arg in found):
                    not_found.append(arg)
            if len(not_found) == 0:
                pass
            elif len(not_found) == 1:
                print("Be careful: problem " + arg + " is not solved yet !")
            else:
                print("Be careful: these problems do not have a written solution yet : ", end='')
                for arg in not_found:
                    if (arg == not_found[-1]):
                        print(arg + ".")
                    else:
                        print(arg + ', ', end='')

        except:
            print(
                "\nError in arguments.\n\nSpecify which problems you want to solve.\nExamples:\n\tmain.py 1 2 3 (solve problems 1, 2 and 3)\n\tmain.py all (solve all problems)\n"
            )


if __name__ == "__main__":
    main()
