import unittest
from src.intellisense import IntellisenseSchema


class TestSchemaMethods(unittest.TestCase):

    def setUp(self):
        self.test_schema_version = 'v1.0.0'
        self.test_sdk_go_version = 'v1.12.1'

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
                        "Furry"
                    ],
                    "members": {
                        "Furry": {
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
                        "proxyConfiguration": {"shape": "String"}
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
        self.test_doc_model = {
            "shapes": {
                "String": {
                    "refs": {
                        "RegisterTaskDefinitionRequest$family": "The family name",
                        "RegisterTaskDefinitionRequest$proxyConfiguration": None
                    }
                },
                "CPU": {
                    "refs": {
                        "HTTP$power": "The launch type on which to run your task. For more information, see "
                                      "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html "
                                      "Amazon ECS Launch Types in the Amazon Elastic Container Service Developer Guide."
                    }
                },
                "Password": {
                    "refs": {
                        "OneMember$family": None
                    }
                },
                "Rabbits": {
                    "refs": {
                        "GetAPetRequest$Furry": "Want a carrot?"
                    }
                }
            }
        }

        self.intellisense = IntellisenseSchema(self.test_api_model, self.test_doc_model,
                                               self.test_schema_version, self.test_sdk_go_version)

    def test_family_required(self):

        members = {'family': 'String', 'proxyConfiguration': 'String'}
        required = ['family']
        operation = 'RegisterTaskDefinitionRequest'

        expected = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "description": "Intellisense for Amazon ECS Task Definition schema version {}, "
                           "based on AWS SDK for Go version {}."
                           .format(self.test_schema_version, self.test_sdk_go_version),
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "family": {
                    "description": "The family name",
                    "type": "string"
                },
                "proxyConfiguration": {
                    "description": "No description available",
                    "type": "string"
                }
            },
            "required": ['family']
        }

        self.assertEqual(self.intellisense.build(members, required, operation), expected)

    def test_recursive_rabbit(self):
        members = {'Furry': 'Rabbits'}
        required = ['Furry']
        operation = 'GetAPetRequest'

        self.maxDiff = None

        expected = {
             "$schema": "http://json-schema.org/draft-07/schema#",
             "type": "object",
             "additionalProperties": False,
             "description": "Intellisense for Amazon ECS Task Definition schema version {}, "
                            "based on AWS SDK for Go version {}."
                            .format(self.test_schema_version, self.test_sdk_go_version),
             "properties": {
                 "Furry": {
                     "additionalProperties": False,
                     "type": "array",
                     "items": {
                         "type": "string",
                         "enum": [
                             "Bugs Bunny",
                             "Anyone"
                         ]
                     },
                     "description": "Want a carrot?"
                 }
             },
             "required": ['Furry']
         }

        self.assertEqual(self.intellisense.build(members, required, operation), expected)

    def test_http_description_with_enum_values(self):
        members = {'power': 'CPU'}
        required = []
        operation = 'HTTP'

        expected = {
             "$schema": "http://json-schema.org/draft-07/schema#",
             "type": "object",
             "additionalProperties": False,
             "description": "Intellisense for Amazon ECS Task Definition schema version {}, "
                            "based on AWS SDK for Go version {}."
                            .format(self.test_schema_version, self.test_sdk_go_version),
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
         }

        self.assertEqual(self.intellisense.build(members, required, operation), expected)


    def test_one_member_with_min_max_pattern(self):
        members = {'family': 'Password'}
        required = []
        operation = "OneMember"

        expected = {
             "$schema": "http://json-schema.org/draft-07/schema#",
             "type": "object",
             "additionalProperties": False,
             "description": "Intellisense for Amazon ECS Task Definition schema version {}, "
                            "based on AWS SDK for Go version {}."
                            .format(self.test_schema_version, self.test_sdk_go_version),
             "properties": {
                 "family": {
                     "description": "No description available",
                     "type": "string",
                     "minLength": 0,
                     "maxLength": 15,
                     "pattern": "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
                 },
             },
             "required": []
         }

        self.assertEqual(self.intellisense.build(members, required, operation), expected)


if __name__ == '__main__':
    unittest.main()
