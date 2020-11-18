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


