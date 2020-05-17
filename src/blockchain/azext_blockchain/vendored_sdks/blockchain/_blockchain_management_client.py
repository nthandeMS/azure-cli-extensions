# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

from ._configuration import BlockchainManagementClientConfiguration
from .operations import BlockchainMemberOperations
from .operations import BlockchainMemberOperationResultOperations
from .operations import LocationOperations
from .operations import OperationOperations
from .operations import SkuOperations
from .operations import TransactionNodeOperations
from . import models


class BlockchainManagementClient(object):
    """REST API for Azure Blockchain Service.

    :ivar blockchain_member: BlockchainMemberOperations operations
    :vartype blockchain_member: azure.mgmt.blockchain.operations.BlockchainMemberOperations
    :ivar blockchain_member_operation_result: BlockchainMemberOperationResultOperations operations
    :vartype blockchain_member_operation_result: azure.mgmt.blockchain.operations.BlockchainMemberOperationResultOperations
    :ivar location: LocationOperations operations
    :vartype location: azure.mgmt.blockchain.operations.LocationOperations
    :ivar operation: OperationOperations operations
    :vartype operation: azure.mgmt.blockchain.operations.OperationOperations
    :ivar sku: SkuOperations operations
    :vartype sku: azure.mgmt.blockchain.operations.SkuOperations
    :ivar transaction_node: TransactionNodeOperations operations
    :vartype transaction_node: azure.mgmt.blockchain.operations.TransactionNodeOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = BlockchainManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.blockchain_member = BlockchainMemberOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.blockchain_member_operation_result = BlockchainMemberOperationResultOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.location = LocationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sku = SkuOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.transaction_node = TransactionNodeOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> BlockchainManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)