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


def parse_rule(line):
    """ Функция, которая разделяет правило по разделителю"""
    rule = Rule()

    if FINAL_DELIMITER in line:
        parts = line.split(FINAL_DELIMITER, 2)
        rule.final = True
        rule.left = parts[0].strip()
        if len(parts) > 1:
            rule.right = parts[1].strip()
        else:
            rule.right = ""
    elif NON_FINAL_DELIMITER in line:
        parts = line.split(NON_FINAL_DELIMITER, 2)
        rule.final = False
        rule.left = parts[0].strip()
        if len(parts) > 1:
            rule.right = parts[1].strip()
        else:
            rule.right = ""
    else:
        raise Exception("delimiter not found in rule "+line)

    return rule


def read_rules(source):
    """ Функция, которая читает правила из файла"""
    rules = []
    for line in source:
        rules.append(parse_rule(line))

    if not rules:
        raise Exception("no rules found in rules file")

    return rules



