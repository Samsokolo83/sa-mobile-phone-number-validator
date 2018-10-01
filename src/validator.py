import re


class Validator(object):

    def __init__(self):
        self.isValid = False
        self.pattern = r"(^0[876][0123456789]((\d{7})|( |-)((\d{3}))( |-)(\d{4})|( |-)(\d{7})))"

    def validate(self, number):
        try:
            if number is None:
                return self.isValid
            if isinstance(number, str) and number.find(' ') >= 0:
                number = number.replace(' ', '')
            self.isValid = number.isdigit() and len(number) == 10
            if self.isValid:
                self.isValid = re.match(
                    self.pattern, number, flags=0) is not None
            return self.isValid
        except Exception:
            self.isValid = False
            return self.isValid
