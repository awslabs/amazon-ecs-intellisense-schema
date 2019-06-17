# from src.api_2_reader import get_task_def
from src import api_2_reader as a

def func(s, action):
    return a.get_task_def(s, action)


def test_reg_task_def():
    assert func('shapes', 'RegisterTaskDefinitionRequest') == {
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
    }

def test_create_service_req():
    assert func('shapes', 'CreateServiceRequest') == {
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
        "propagateTags": "PropagateTags"
      }

