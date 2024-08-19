# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "networkcloud kubernetescluster agentpool wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.networkcloud/kubernetesclusters/{}/agentpools/{}", "2024-06-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.agent_pool_name = AAZStrArg(
            options=["-n", "--name", "--agent-pool-name"],
            help="The name of the Kubernetes cluster agent pool.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^([a-zA-Z0-9][a-zA-Z0-9-_]{0,28}[a-zA-Z0-9])$",
            ),
        )
        _args_schema.kubernetes_cluster_name = AAZStrArg(
            options=["--kubernetes-cluster-name"],
            help="The name of the Kubernetes cluster.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^([a-zA-Z0-9][a-zA-Z0-9-_]{0,28}[a-zA-Z0-9])$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AgentPoolsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class AgentPoolsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/kubernetesClusters/{kubernetesClusterName}/agentPools/{agentPoolName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "agentPoolName", self.ctx.args.agent_pool_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "kubernetesClusterName", self.ctx.args.kubernetes_cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-06-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
            )
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            extended_location = cls._schema_on_200.extended_location
            extended_location.name = AAZStrType(
                flags={"required": True},
            )
            extended_location.type = AAZStrType(
                flags={"required": True},
            )

            properties = cls._schema_on_200.properties
            properties.administrator_configuration = AAZObjectType(
                serialized_name="administratorConfiguration",
            )
            properties.agent_options = AAZObjectType(
                serialized_name="agentOptions",
            )
            properties.attached_network_configuration = AAZObjectType(
                serialized_name="attachedNetworkConfiguration",
            )
            properties.availability_zones = AAZListType(
                serialized_name="availabilityZones",
            )
            properties.count = AAZIntType(
                flags={"required": True},
            )
            properties.detailed_status = AAZStrType(
                serialized_name="detailedStatus",
                flags={"read_only": True},
            )
            properties.detailed_status_message = AAZStrType(
                serialized_name="detailedStatusMessage",
                flags={"read_only": True},
            )
            properties.kubernetes_version = AAZStrType(
                serialized_name="kubernetesVersion",
                flags={"read_only": True},
            )
            properties.labels = AAZListType()
            properties.mode = AAZStrType(
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.taints = AAZListType()
            properties.upgrade_settings = AAZObjectType(
                serialized_name="upgradeSettings",
            )
            properties.vm_sku_name = AAZStrType(
                serialized_name="vmSkuName",
                flags={"required": True},
            )

            administrator_configuration = cls._schema_on_200.properties.administrator_configuration
            administrator_configuration.admin_username = AAZStrType(
                serialized_name="adminUsername",
            )
            administrator_configuration.ssh_public_keys = AAZListType(
                serialized_name="sshPublicKeys",
            )

            ssh_public_keys = cls._schema_on_200.properties.administrator_configuration.ssh_public_keys
            ssh_public_keys.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.administrator_configuration.ssh_public_keys.Element
            _element.key_data = AAZStrType(
                serialized_name="keyData",
                flags={"required": True},
            )

            agent_options = cls._schema_on_200.properties.agent_options
            agent_options.hugepages_count = AAZIntType(
                serialized_name="hugepagesCount",
                flags={"required": True},
            )
            agent_options.hugepages_size = AAZStrType(
                serialized_name="hugepagesSize",
            )

            attached_network_configuration = cls._schema_on_200.properties.attached_network_configuration
            attached_network_configuration.l2_networks = AAZListType(
                serialized_name="l2Networks",
            )
            attached_network_configuration.l3_networks = AAZListType(
                serialized_name="l3Networks",
            )
            attached_network_configuration.trunked_networks = AAZListType(
                serialized_name="trunkedNetworks",
            )

            l2_networks = cls._schema_on_200.properties.attached_network_configuration.l2_networks
            l2_networks.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.attached_network_configuration.l2_networks.Element
            _element.network_id = AAZStrType(
                serialized_name="networkId",
                flags={"required": True},
            )
            _element.plugin_type = AAZStrType(
                serialized_name="pluginType",
            )

            l3_networks = cls._schema_on_200.properties.attached_network_configuration.l3_networks
            l3_networks.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.attached_network_configuration.l3_networks.Element
            _element.ipam_enabled = AAZStrType(
                serialized_name="ipamEnabled",
            )
            _element.network_id = AAZStrType(
                serialized_name="networkId",
                flags={"required": True},
            )
            _element.plugin_type = AAZStrType(
                serialized_name="pluginType",
            )

            trunked_networks = cls._schema_on_200.properties.attached_network_configuration.trunked_networks
            trunked_networks.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.attached_network_configuration.trunked_networks.Element
            _element.network_id = AAZStrType(
                serialized_name="networkId",
                flags={"required": True},
            )
            _element.plugin_type = AAZStrType(
                serialized_name="pluginType",
            )

            availability_zones = cls._schema_on_200.properties.availability_zones
            availability_zones.Element = AAZStrType()

            labels = cls._schema_on_200.properties.labels
            labels.Element = AAZObjectType()
            _WaitHelper._build_schema_kubernetes_label_read(labels.Element)

            taints = cls._schema_on_200.properties.taints
            taints.Element = AAZObjectType()
            _WaitHelper._build_schema_kubernetes_label_read(taints.Element)

            upgrade_settings = cls._schema_on_200.properties.upgrade_settings
            upgrade_settings.drain_timeout = AAZIntType(
                serialized_name="drainTimeout",
            )
            upgrade_settings.max_surge = AAZStrType(
                serialized_name="maxSurge",
            )
            upgrade_settings.max_unavailable = AAZStrType(
                serialized_name="maxUnavailable",
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""

    _schema_kubernetes_label_read = None

    @classmethod
    def _build_schema_kubernetes_label_read(cls, _schema):
        if cls._schema_kubernetes_label_read is not None:
            _schema.key = cls._schema_kubernetes_label_read.key
            _schema.value = cls._schema_kubernetes_label_read.value
            return

        cls._schema_kubernetes_label_read = _schema_kubernetes_label_read = AAZObjectType()

        kubernetes_label_read = _schema_kubernetes_label_read
        kubernetes_label_read.key = AAZStrType(
            flags={"required": True},
        )
        kubernetes_label_read.value = AAZStrType(
            flags={"required": True},
        )

        _schema.key = cls._schema_kubernetes_label_read.key
        _schema.value = cls._schema_kubernetes_label_read.value


__all__ = ["Wait"]
