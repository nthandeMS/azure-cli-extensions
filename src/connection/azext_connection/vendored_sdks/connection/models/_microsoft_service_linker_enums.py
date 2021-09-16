# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ActionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs.
    """

    INTERNAL = "Internal"

class AuthType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type.
    """

    SYSTEM_ASSIGNED_IDENTITY = "systemAssignedIdentity"
    USER_ASSIGNED_IDENTITY = "userAssignedIdentity"
    SERVICE_PRINCIPAL_SECRET = "servicePrincipalSecret"
    SERVICE_PRINCIPAL_CERTIFICATE = "servicePrincipalCertificate"
    SECRET = "secret"

class ClientType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    DOTNET = "dotnet"
    DOTNET_CORE = "dotnetCore"
    PYTHON = "python"
    DJANGO = "django"
    PHP = "php"
    NODEJS = "Nodejs"
    JAVA = "java"
    GO = "go"
    SPRING_CLOUD_BINDING = "springCloudBinding"

class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class LinkerStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies if the linker is healthy.
    """

    HEALTHY = "Healthy"
    NOT_HEALTHY = "Not healthy"

class Origin(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system"
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"

class Type(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of setting. One of appSettings, connectionStrings, serviceBindings
    """

    APP_SETTINGS = "appSettings"
    CONNECTION_STRINGS = "connectionStrings"
    SERVICE_BINDINGS = "serviceBindings"