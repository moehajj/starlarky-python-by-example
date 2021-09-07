import argparse
from pylarky.eval.evaluator import Evaluator, FailedEvaluation

parser = argparse.ArgumentParser(description='Run Starlarky Script.')
parser.add_argument('script', help='script filename')
parser.add_argument('input', help='input filename')

args = parser.parse_args()
script_filename = args.script
input_filename = args.input

with open(script_filename, "r") as script_fd, open(input_filename, "r") as input_fd:
    starlark_script = script_fd.read()
    script_input = input_fd.read()

    evaluator = Evaluator(starlark_script)
    eval_output = evaluator.evaluate(script_input)
    print(eval_output)

