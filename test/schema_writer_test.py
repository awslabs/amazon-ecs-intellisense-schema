import unittest

from src.schema_writer import *


class TestSchemaMethods(unittest.TestCase):

    def setUp(self):
        self.test_api_model = {
            "shapes": {
                "HTTP": {
                    "type": "list",
                    "members": {
                        "power": {
                            "shape": "CPU"
                        }
                    }
                },
                "OneMember": {
                    "type": "structure",
                    "members": {
                        "family": {
                            "shape": "Password"
                        }
                    }

                },
                "GetAPetRequest": {
                    "type": "structure",
                    "required": [
                        "rabbits"
                    ],
                    "members": {
                        "rabbits": {
                            "shape": "Rabbits"
                        }
                    }
                },
                "RegisterTaskDefinitionRequest": {
                    "type": "structure",
                    "required": [
                        "family"
                    ],
                    "members": {
                        "family": {"shape": "String"},
                        "taskRoleArn": {"shape": "String"}
                    }
                },
                "CPU": {
                    "type": "integer",
                    "enum": [5, 10, 15]
                },
                "Password": {
                    "type": "string",
                    "min": 0,
                    "max": 15,
                    "pattern": "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
                },
                "Rabbit": {
                    "type": "string",
                    "enum": [
                        "Bugs Bunny",
                        "Anyone"
                    ]
                },
                "Rabbits": {
                    "type": "list",
                    "member": {"shape": "Rabbit"}
                },
                "String": {"type": "string"}
            }

        }

    def test_recursive_rabbit(self):
        dummy_reference = {'rabbits': 'Rabbits'}
        dummy_required = ['rabbits']
        dummy_description = {'rabbits': 'HELLO'}

        self.assertEqual(get_schema(dummy_reference, dummy_description, dummy_required, self.test_api_model), {
             "$schema": "http://json-schema.org/draft-07/schema#",
             "type": "object",
             "additionalProperties": False,
             "properties": {
                 "rabbits": {
                     "additionalProperties": False,
                     "type": "array",
                     "items": {
                         "type": "string",
                         "enum": [
                             "Bugs Bunny",
                             "Anyone"
                         ]
                     },
                     "description": "HELLO"
                 }
             },
             "required": ['rabbits']
         })

    def test_http_description_with_enum_values(self):
        dummy_reference = {'power': 'CPU'}
        dummy_description = {'power': 'The launch type on which to run your task. For more information, see '
                                      'https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html '
                                      'Amazon ECS Launch Types in the '
                                      'Amazon Elastic Container Service Developer Guide.'}
        dummy_required = []

        self.assertEqual(get_schema(dummy_reference, dummy_description, dummy_required, self.test_api_model), {
             "$schema": "http://json-schema.org/draft-07/schema#",
             "type": "object",
             "additionalProperties": False,
             "properties": {
                 "power": {
                     "type": "integer",
                     "enum": [5, 10, 15],
                     "description": "The launch type on which to run your task. For more information, see "
                                    "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html "
                                    "Amazon ECS Launch Types in the Amazon Elastic Container Service Developer Guide."
                 }
             },
             "required": []
         })

    def test_family_required(self):
        dummy_reference = {'family': 'String', 'taskRoleArn': 'String'}
        dummy_description = {'family': 'The family name', 'taskRoleArn': 'No description currently available'}
        dummy_required = ['family']

        self.assertEqual(get_schema(dummy_reference, dummy_description, dummy_required, self.test_api_model), {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "family": {
                    "description": "The family name",
                    "type": "string"
                },
                "taskRoleArn": {
                    "description": "No description currently available",
                    "type": "string"
                }
            },
            "required": ['family']
        })
        self.assertNotEqual(get_schema(dummy_reference, dummy_description, dummy_required, self.test_api_model), {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "family": {
                    "description": "The family name",
                    "type": "string"
                },
                "taskRoleArn": {
                    "description": "No description currently available",
                    "type": "string"
                }
            },
            "required": ['family', 'taskRoleArn']
        })

    def test_one_member_with_min_max_pattern(self):
        dummy_reference = {'family': 'Password'}
        dummy_description = {'family': 'No description currently available'}
        dummy_required = []

        self.assertEqual(get_schema(dummy_reference, dummy_description, dummy_required, self.test_api_model), {
             "$schema": "http://json-schema.org/draft-07/schema#",
             "type": "object",
             "additionalProperties": False,
             "properties": {
                 "family": {
                     "description": "No description currently available",
                     "type": "string",
                     "minLength": 0,
                     "maxLength": 15,
                     "pattern": "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
                 },
             },
             "required": []
         })
        self.assertNotEqual(get_schema(dummy_reference, dummy_description, dummy_required, self.test_api_model), {
             "$schema": "http://json-schema.org/draft-07/schema#",
             "type": "object",
             "additionalProperties": False,
             "properties": {
                 "family": {
                     "description": "No description currently available",
                     "type": "string",
                     "minLength": 0,
                 },
             },
             "required": []
         })


if __name__ == '__main__':
    unittest.main()
