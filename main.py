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
            print(args)  # Process arguments
        except:
            print(
                "\nError in arguments.\n\nSpecify which problems you want to solve.\nExamples:\n\tmain.py 1 2 3 (solve problems 1, 2 and 3)\n\tmain.py all (solve all problems)\n"
            )


if __name__ == "__main__":
    main()
