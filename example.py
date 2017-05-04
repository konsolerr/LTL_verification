from LTL_formula.formulas import *
from buchi_translation import  holy_fucking_translation
from pprint import pprint

simple_tests_path = "tests/ltl_formulas/simple"
bulk_file = "tests/ltl_formulas/bulk.ltl"

formula_set = FormulaSet.from_filename(bulk_file)

print(len(formula_set))
for formula in formula_set:
    print("###")
    print(formula)
    neg = formula.normal_form()
    print(neg)
    print({neg} == {neg})
    pprint(holy_fucking_translation(neg))
    # print(formula.get_text())
    # print(formula.negative_propagation())
    # print(formula.normal_form())