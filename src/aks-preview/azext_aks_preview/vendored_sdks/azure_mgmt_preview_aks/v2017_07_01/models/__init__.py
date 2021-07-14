# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ContainerService
    from ._models_py3 import ContainerServiceAgentPoolProfile
    from ._models_py3 import ContainerServiceCustomProfile
    from ._models_py3 import ContainerServiceDiagnosticsProfile
    from ._models_py3 import ContainerServiceLinuxProfile
    from ._models_py3 import ContainerServiceListResult
    from ._models_py3 import ContainerServiceMasterProfile
    from ._models_py3 import ContainerServiceOrchestratorProfile
    from ._models_py3 import ContainerServicePrincipalProfile
    from ._models_py3 import ContainerServiceSshConfiguration
    from ._models_py3 import ContainerServiceSshPublicKey
    from ._models_py3 import ContainerServiceVMDiagnostics
    from ._models_py3 import ContainerServiceWindowsProfile
    from ._models_py3 import KeyVaultSecretRef
    from ._models_py3 import OrchestratorProfile
    from ._models_py3 import OrchestratorVersionProfile
    from ._models_py3 import OrchestratorVersionProfileListResult
    from ._models_py3 import Resource
except (SyntaxError, ImportError):
    from ._models import ContainerService  # type: ignore
    from ._models import ContainerServiceAgentPoolProfile  # type: ignore
    from ._models import ContainerServiceCustomProfile  # type: ignore
    from ._models import ContainerServiceDiagnosticsProfile  # type: ignore
    from ._models import ContainerServiceLinuxProfile  # type: ignore
    from ._models import ContainerServiceListResult  # type: ignore
    from ._models import ContainerServiceMasterProfile  # type: ignore
    from ._models import ContainerServiceOrchestratorProfile  # type: ignore
    from ._models import ContainerServicePrincipalProfile  # type: ignore
    from ._models import ContainerServiceSshConfiguration  # type: ignore
    from ._models import ContainerServiceSshPublicKey  # type: ignore
    from ._models import ContainerServiceVMDiagnostics  # type: ignore
    from ._models import ContainerServiceWindowsProfile  # type: ignore
    from ._models import KeyVaultSecretRef  # type: ignore
    from ._models import OrchestratorProfile  # type: ignore
    from ._models import OrchestratorVersionProfile  # type: ignore
    from ._models import OrchestratorVersionProfileListResult  # type: ignore
    from ._models import Resource  # type: ignore

from ._container_service_client_enums import (
    ContainerServiceOrchestratorTypes,
    ContainerServiceStorageProfileTypes,
    ContainerServiceVMSizeTypes,
    Count,
    OSType,
)

__all__ = [
    'ContainerService',
    'ContainerServiceAgentPoolProfile',
    'ContainerServiceCustomProfile',
    'ContainerServiceDiagnosticsProfile',
    'ContainerServiceLinuxProfile',
    'ContainerServiceListResult',
    'ContainerServiceMasterProfile',
    'ContainerServiceOrchestratorProfile',
    'ContainerServicePrincipalProfile',
    'ContainerServiceSshConfiguration',
    'ContainerServiceSshPublicKey',
    'ContainerServiceVMDiagnostics',
    'ContainerServiceWindowsProfile',
    'KeyVaultSecretRef',
    'OrchestratorProfile',
    'OrchestratorVersionProfile',
    'OrchestratorVersionProfileListResult',
    'Resource',
    'ContainerServiceOrchestratorTypes',
    'ContainerServiceStorageProfileTypes',
    'ContainerServiceVMSizeTypes',
    'Count',
    'OSType',
]