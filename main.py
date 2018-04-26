from tools import *
from quine_mccluskey import *
import sys
import string


def simplify():
    if(len(sys.argv)!=2):
        print("Please provide 1 logic expresion")
    else:
        expr = sys.argv[1]
        args = [char for char in expr if char!=' ']
        if(is_logic(expr)):
            rpn_expr = convert_to_rpn(args)
            vars = list(filter(lambda c: c not in operators and c not in ('1', '0'), rpn_expr))

            true_evs = all_true_evaluations(rpn_expr,vars)
            q_m = qm(true_evs,[],len(vars))
            simplified_expression = get_result(q_m,vars)
            print(''.join(simplified_expression))
        else: print("This is not a proper logic expression")

def main():
    simplify()
    

if __name__ == '__main__':
    main()