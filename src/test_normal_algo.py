import io
import unittest

from .normal_algo import Rule, read_rules, apply_rules, parse_rule, EPSILON_SYMBOL


class NormalAlgoTestCase(unittest.TestCase):
    def test_rule_parse(self):
        """ Тестирует вызов функции parse_rule(). """

        rule = parse_rule("a => b")
        self.assertFalse(rule.final)
        self.assertEqual(rule.left, "a")
        self.assertEqual(rule.right, "b")

        rule = parse_rule("a =>. b")
        self.assertTrue(rule.final)
        self.assertEqual(rule.left, "a")
        self.assertEqual(rule.right, "b")

        rule = parse_rule("ε => b")
        self.assertFalse(rule.final)
        self.assertEqual(rule.left, EPSILON_SYMBOL)
        self.assertEqual(rule.right, "b")

        rule = parse_rule("a => ε")
        self.assertFalse(rule.final)
        self.assertEqual(rule.left, "a")
        self.assertEqual(rule.right, EPSILON_SYMBOL)

    def test_read_rules(self):
        """ Тестирует вызов функции read_rules(). """
        rules = read_rules(io.StringIO(
            "a => b\n" +
            "b => c\n" +
            "ε =>. d"
        ))
        self.assertEqual(len(rules), 3)
        self.assertFalse(rules[0].final)
        self.assertFalse(rules[1].final)
        self.assertTrue(rules[2].final)

    def test_apply_rules(self):
        """ Тестирует вызов функции apply_rules(). """
        rule1 = Rule()
        rule1.final = False
        rule1.left = "a"
        rule1.right = "b"

        rule2 = Rule()
        rule2.final = True
        rule2.left = "c"
        rule2.right = "d"

        self.assertEqual(
            apply_rules([rule1, rule2], "abc"),
            "bbd"
        )


if __name__ == '__main__':
    unittest.main()