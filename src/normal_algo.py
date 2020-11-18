import argparse
import sys


def parse_args():
    """ Функция, которая принимает аргументы из командной строки(путь к файлу со схемой
    марковских подстановок, путь к файлу со словом, путь к файлу, в который нужно вывести слово,
    полученное в результате применения марковских подсатновок)"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--rules", type=argparse.FileType("r"), required=True)
    parser.add_argument("--input", type=argparse.FileType("r"), required=True)
    parser.add_argument("--output", type=argparse.FileType("w"), default=sys.stdout)
    return parser.parse_args()


class Rule:
    left = ""
    right = ""
    final = False


NON_FINAL_DELIMITER = "=>"
FINAL_DELIMITER = "=>."
EPSILON_SYMBOL = "ε"


def apply_rule(rule, input):
    """ Функция, которая применяет правило к входной строке """

    if rule.left == EPSILON_SYMBOL:
        return True, rule.right + input

    if rule.left in input:
        if rule.right == EPSILON_SYMBOL:
            return True, input.replace(rule.left, "", 1)
        return True, input.replace(rule.left, rule.right, 1)

    return False, input
