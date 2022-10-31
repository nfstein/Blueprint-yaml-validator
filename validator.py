import yamale
import uuid
import re
from yamale.validators import DefaultValidators, Validator, Regex

validators = DefaultValidators.copy()  # This is a dictionary
schema = yamale.make_schema('./schema.yaml', validators=validators)

data = yamale.make_data('./detection-rule.yaml')
# data = yamale.make_data('./test-rule1.yaml')
# data = yamale.make_data('./test-rule2.yaml')
# data = yamale.make_data('./test-rule3.yaml')


try:
    yamale.validate(schema, data)
    print('Blueprint Yaml Validation success! 👍')
except ValueError as e:
    print('Blueprint Yaml Validation failed!\n%s' % str(e))
    exit(1)
