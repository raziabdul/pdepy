import os
directory = os.path.dirname(os.path.abspath(__file__))
os.system('python3 {}/diff_op_expression/main.py'.format(directory))
os.system('python3 {}/diff_operators/main.py'.format(directory))
os.system('python3 {}/domain_conditions/dirichlet/main.py'.format(directory))
os.system('python3 {}/domain_conditions/domain/main.py'.format(directory))
os.system('python3 {}/fdm/fdm_solver/main.py'.format(directory))