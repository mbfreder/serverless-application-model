from __future__ import annotations

from typing import Dict, Optional, Union


from samtranslator.schema.common import BaseModel, LenientBaseModel
from samtranslator.schema import (
    aws_serverless_simpletable,
    aws_serverless_application,
    aws_serverless_connector,
    aws_serverless_function,
    aws_serverless_statemachine,
    aws_serverless_layerversion,
    aws_serverless_api,
    aws_serverless_httpapi,
    any_cfn_resource,
)


class Globals(BaseModel):
    Function: Optional[aws_serverless_function.Globals]
    Api: Optional[aws_serverless_api.Globals]
    HttpApi: Optional[aws_serverless_httpapi.Globals]
    SimpleTable: Optional[aws_serverless_simpletable.Globals]


class Model(LenientBaseModel):
    Globals: Optional[Globals]
    Resources: Dict[
        str,
        Union[
            aws_serverless_connector.Resource,
            aws_serverless_function.Resource,
            aws_serverless_simpletable.Resource,
            aws_serverless_statemachine.Resource,
            aws_serverless_layerversion.Resource,
            aws_serverless_api.Resource,
            aws_serverless_httpapi.Resource,
            aws_serverless_application.Resource,
            any_cfn_resource.Resource,
        ],
    ]


if __name__ == "__main__":
    print(Model.schema_json(indent=2))