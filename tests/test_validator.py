#!/usr/bin/env python
# coding=utf-8

import unittest
import json
import os
from src.validator import Validator


class ValidatorTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_validatorStr(self):
        validator = Validator()
        valid = validator.validate('')
        self.assertFalse(valid)
        valid = validator.validate(' ')
        self.assertFalse(valid)
        valid = validator.validate('auqywsdsad')
        self.assertFalse(valid)

    def test_validatorNone(self):
        validator = Validator()
        valid = validator.validate(None)
        self.assertFalse(valid)

    def test_validatorClass(self):
        validator = Validator()
        valid = validator.validate(validator)
        self.assertFalse(valid)

    def test_validator(self):
        validator = Validator()
        valid = validator.validate('0898474635')
        self.assertTrue(valid)
        valid = validator.validate('0752781937')
        self.assertTrue(valid)
        validator = Validator()
        valid = validator.validate('0619871528')
        self.assertTrue(valid)
        valid = validator.validate('0549371528')
        self.assertFalse(valid)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(exit=False)
