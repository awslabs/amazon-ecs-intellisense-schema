import unittest
from src.api_reader import *


class TestReferenceMethods(unittest.TestCase):

    def setUp(self):
        self.test_api_model = {
            "shapes": {
                "RegisterTaskDefinitionRequest": {
                    "type": "structure",
                    "required": [
                        "family",
                        "containerDefinitions"
                    ],
                    "members": {
                        "family": {"shape": "String"},
                        "taskRoleArn": {"shape": "String"},
                        "executionRoleArn": {"shape": "String"},
                        "networkMode": {"shape": "NetworkMode"},
                        "containerDefinitions": {"shape": "ContainerDefinitions"},
                        "volumes": {"shape": "VolumeList"},
                        "placementConstraints": {"shape": "TaskDefinitionPlacementConstraints"},
                        "requiresCompatibilities": {"shape": "CompatibilityList"},
                        "cpu": {"shape": "String"},
                        "memory": {"shape": "String"},
                        "tags": {"shape": "Tags"},
                        "pidMode": {"shape": "PidMode"},
                        "ipcMode": {"shape": "IpcMode"},
                        "proxyConfiguration": {"shape": "ProxyConfiguration"}
                    }
                },
                "CreateServiceRequest": {
                    "type": "structure",
                    "required": ["serviceName"],
                    "members": {
                        "cluster": {"shape": "String"},
                        "serviceName": {"shape": "String"},
                        "taskDefinition": {"shape": "String"},
                        "loadBalancers": {"shape": "LoadBalancers"},
                        "serviceRegistries": {"shape": "ServiceRegistries"},
                        "desiredCount": {"shape": "BoxedInteger"},
                        "clientToken": {"shape": "String"},
                        "launchType": {"shape": "LaunchType"},
                        "platformVersion": {"shape": "String"},
                        "role": {"shape": "String"},
                        "deploymentConfiguration": {"shape": "DeploymentConfiguration"},
                        "placementConstraints": {"shape": "PlacementConstraints"},
                        "placementStrategy": {"shape": "PlacementStrategies"},
                        "networkConfiguration": {"shape": "NetworkConfiguration"},
                        "healthCheckGracePeriodSeconds": {"shape": "BoxedInteger"},
                        "schedulingStrategy": {"shape": "SchedulingStrategy"},
                        "deploymentController": {"shape": "DeploymentController"},
                        "tags": {"shape": "Tags"},
                        "enableECSManagedTags": {"shape": "Boolean"},
                        "propagateTags": {"shape": "PropagateTags"}
                    }
                }
            }
        }

    def test_register_task_def(self):
        self.assertEqual(get_references(self.test_api_model, 'RegisterTaskDefinitionRequest'), ({
            "containerDefinitions": "ContainerDefinitions",
            "cpu": "String",
            "executionRoleArn": "String",
            "family": "String",
            "ipcMode": "IpcMode",
            "memory": "String",
            "networkMode": "NetworkMode",
            "pidMode": "PidMode",
            "placementConstraints": "TaskDefinitionPlacementConstraints",
            "proxyConfiguration": "ProxyConfiguration",
            "tags": "Tags",
            "requiresCompatibilities": "CompatibilityList",
            "taskRoleArn": "String",
            "volumes": "VolumeList"
        }, ['family', 'containerDefinitions']))

    def test_register_task_def_networkmode_type_fail(self):
        self.assertNotEqual(get_references(self.test_api_model, 'RegisterTaskDefinitionRequest'), ({
            "containerDefinitions": "ContainerDefinitions",
            "cpu": "String",
            "executionRoleArn": "String",
            "family": "String",
            "ipcMode": "IpcMode",
            "memory": "String",
            "networkMode": "String",
            "pidMode": "PidMode",
            "placementConstraints": "TaskDefinitionPlacementConstraints",
            "proxyConfiguration": "ProxyConfiguration",
            "requiresCompatibilities": "CompatibilityList",
            "tags": "Tags",
            "taskRoleArn": "String",
            "volumes": "VolumeList"
        }, ['family', 'containerDefinitions']))

    def test_register_task_def_family_required_fail(self):
        self.assertNotEqual(get_references(self.test_api_model, 'RegisterTaskDefinitionRequest'), ({
            "containerDefinitions": "ContainerDefinitions",
            "cpu": "String",
            "executionRoleArn": "String",
            "family": "String",
            "ipcMode": "IpcMode",
            "memory": "String",
            "networkMode": "NetworkMode",
            "pidMode": "PidMode",
            "placementConstraints": "TaskDefinitionPlacementConstraints",
            "proxyConfiguration": "ProxyConfiguration",
            "requiresCompatibilities": "CompatibilityList",
            "tags": "Tags",
            "taskRoleArn": "String",
            "volumes": "VolumeList"
        }, ['containerDefinitions']))

    def test_create_service_req(self):
        self.assertEqual(get_references(self.test_api_model, 'CreateServiceRequest'), ({
            "cluster": "String",
            "serviceName": "String",
            "taskDefinition": "String",
            "loadBalancers": "LoadBalancers",
            "serviceRegistries": "ServiceRegistries",
            "desiredCount": "BoxedInteger",
            "clientToken": "String",
            "launchType": "LaunchType",
            "platformVersion": "String",
            "role": "String",
            "deploymentConfiguration": "DeploymentConfiguration",
            "placementConstraints": "PlacementConstraints",
            "placementStrategy": "PlacementStrategies",
            "networkConfiguration": "NetworkConfiguration",
            "healthCheckGracePeriodSeconds": "BoxedInteger",
            "schedulingStrategy": "SchedulingStrategy",
            "deploymentController": "DeploymentController",
            "tags": "Tags",
            "enableECSManagedTags": "Boolean",
            "propagateTags": "PropagateTags",
          }, ["serviceName"]))

    def test_create_service_req_extra_parameter_fail(self):
        self.assertNotEqual(get_references(self.test_api_model, 'CreateServiceRequest'), ({
            "cluster": "String",
            "serviceName": "String",
            "taskDefinition": "String",
            "loadBalancers": "LoadBalancers",
            "serviceRegistries": "ServiceRegistries",
            "desiredCount": "BoxedInteger",
            "clientToken": "String",
            "launchType": "LaunchType",
            "platformVersion": "String",
            "deploymentConfiguration": "DeploymentConfiguration",
            "placementConstraints": "PlacementConstraints",
            "placementStrategy": "PlacementStrategies",
            "networkConfiguration": "NetworkConfiguration",
            "healthCheckGracePeriodSeconds": "BoxedInteger",
            "schedulingStrategy": "SchedulingStrategy",
            "deploymentController": "DeploymentController",
            "tags": "Tags",
            "enableECSManagedTags": "Boolean",
            "propagateTags": "PropagateTags",
            "volumes": "VolumeList"
        }, ["serviceName"]))


if __name__ == '__main__':
    unittest.main()
