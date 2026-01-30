import importlib
import inspect
import os
import pkgutil
from functools import wraps
from types import FunctionType

import ratp_route_calc.api.default as apis
from mcp.server.fastmcp import FastMCP
from ratp_route_calc.client import AuthenticatedClient

mcp = FastMCP("ratp")

client = AuthenticatedClient(
    base_url="https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia",
    token=os.environ["NAVITIA_TOKEN"],
    auth_header_name="apikey",
    prefix="",
)

for submodule in pkgutil.iter_modules(apis.__path__):
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

        return wrapper

    wrapped = create_wrapper(fn)

    mcp.add_tool(
        wrapped,
        name=submodule.name,
        title=submodule.name,
        description=wrapped.__doc__,
        structured_output=False,
    )
