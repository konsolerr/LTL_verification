#!/usr/bin/python3
import argparse
from ltlFormula.formulas import *
from buchiAutomata.buchiAutomata import LabeledGeneralisedBuchiAutomaton, BuchiAutomaton
from automaton import Automaton
from automatonToBuchi import automaton_to_buchi
from utils import verification
from pprint import pprint
import os.path


def extant_file(x):
    if not os.path.exists(x):
        raise argparse.ArgumentTypeError("{0} does not exist".format(x))
    return x

parser = argparse.ArgumentParser()
parser.add_argument("path_to_automaton",
                    help="Path to xml file with automaton description",
                    type=extant_file)
parser.add_argument("path_to_ltl",
                    help="Path to file with LTL formulas to be validated one formula for each line",
                    type=extant_file)


def main():
    args = parser.parse_args()
    automaton = Automaton.from_file(args.path_to_automaton)
    automaton = automaton_to_buchi(automaton)

    formulas = get_formulas_from_file(args.path_to_ltl)
    for formula in formulas:
        neg = formula.normal_form(negation=True)
        closure = neg.get_closure()

        if any(map(lambda x: isinstance(x, UntilFormula), closure)):
            ltl_automaton = LabeledGeneralisedBuchiAutomaton.from_formula(neg, aps=automaton.aps)
            ltl_automaton = BuchiAutomaton.from_labeled(ltl_automaton)
            results = verification(automaton, ltl_automaton)

            if not results[0]:
                print("Formula \"{}\" is valid\n---".format(formula.get_text()))
            else:
                print("Formula \"{}\" is invalid, here goes the counter example :\nStart:\n{};\nCycle:\n{};\n---".format(
                    formula.get_text(),
                    "\n".join(map(lambda x: "\t" + " ".join(sorted(map(lambda y: y.name, x))), results[1])),
                    "\n".join(map(lambda x: "\t" + " ".join(sorted(map(lambda y: y.name, x))), results[2]))
                ))
        else:
            print("Formula \"{}\" has not temporal operator from (U, F, G, R). \n"
                  "So nothing to verify really\n---".format(formula.get_text()))
        # pprint(results)

if __name__ == "__main__":
    main()
