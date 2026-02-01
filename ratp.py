import importlib
import inspect
import os
import pkgutil
from functools import wraps
from types import FunctionType
from typing import Optional

from mcp.server.fastmcp import FastMCP
from mcp.types import AnyFunction
from pydantic.errors import PydanticSchemaGenerationError

import ratp_route_calc.api.default as apis
from ratp_route_calc.client import AuthenticatedClient

mcp = FastMCP("ratp")

client = AuthenticatedClient(
    base_url="https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia",
    token=os.environ["NAVITIA_TOKEN"],
    auth_header_name="apikey",
    prefix="",
)


def add_tool_to_mcp(
    fn: AnyFunction,
    name: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    structured_output: Optional[bool] = None,
):
    mcp.add_tool(
        fn,
        name=name,
        title=title,
        description=description,
        structured_output=structured_output,
    )


submodules = pkgutil.iter_modules(apis.__path__)
OLD_PREFIX = submodules.__next__().name
NEW_PREFIX = "transports"

for submodule in submodules:
    imported = importlib.import_module(apis.__name__ + "." + submodule.name)
    fn: FunctionType = imported.__dict__["sync"]

    def create_wrapper(original_fn):
        @wraps(original_fn)
        def wrapper(*args, **kwargs):
            return original_fn(client=client, *args, **kwargs)

        sig = inspect.signature(original_fn)
        params = list(sig.parameters.values())[1:]  # Skip first parameter (client)
        new_sig = sig.replace(parameters=params)
        wrapper.__signature__ = new_sig  # pyright: ignore[reportAttributeAccessIssue]
        wrapper.__name__ = NEW_PREFIX + submodule.name.removeprefix(OLD_PREFIX)

        return wrapper

    wrapped = create_wrapper(fn)

    add_tool = lambda structured_output: add_tool_to_mcp(  # noqa: E731
        wrapped,
        title=wrapped.__name__,
        description=wrapped.__doc__ or "",
        structured_output=structured_output,
    )

    print(f"Added {wrapped.__name__} tool", end=" ")
    try:
        add_tool(True)
        print("with typed output")
    except PydanticSchemaGenerationError:
        add_tool(False)
        print("without typed output")
