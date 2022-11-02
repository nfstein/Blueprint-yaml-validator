from operator import truediv
import yamale
import uuid
import re
from yamale.validators import DefaultValidators, Validator, Regex

class TFVERSION(Validator):
    """ Custom TFVERSION validator """
    tag = 'settings'

    def __init__(self, *args, **kwargs):
        self._settings = str(kwargs.get('settings', ''))
        for k,v in self._settings:
            if k == "TF_VERSION":
                return True

        return False

validators = DefaultValidators.copy()  # This is a dictionary
validators[TFVERSION.tag] = TFVERSION
schema = yamale.make_schema('./schema.yaml', validators=validators)

#example data sets
data = yamale.make_data('./detection-rule.yaml')
# data = yamale.make_data('./test-sample/test-rule1.yaml')
# data = yamale.make_data('./test-sample/test-rule2.yaml')
# data = yamale.make_data('./test-sample/test-rule3.yaml')

try:
    yamale.validate(schema, data)
    print('Blueprint Yaml Validation success! 👍')
except ValueError as e:
    print('Blueprint Yaml Validation failed!\n%s' % str(e))
    exit(1)
