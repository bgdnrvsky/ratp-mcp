import importlib
import inspect
import os
import pkgutil
from functools import wraps
from types import FunctionType

import ratp_route_calc.api.default as apis
from mcp.server.fastmcp import FastMCP
from ratp_route_calc.client import AuthenticatedClient

mcp = FastMCP("ratp", json_response=True)

client = AuthenticatedClient(
    base_url="https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia",
    token=os.environ["NAVITIA_TOKEN"],
    auth_header_name="apikey",
    prefix="",
)


submodules = pkgutil.iter_modules(apis.__path__)
OLD_PREFIX = submodules.__next__().name
NEW_PREFIX = "ratp"

for submodule in submodules:
    imported = importlib.import_module(apis.__name__ + "." + submodule.name)
    fn: FunctionType = imported.__dict__["sync"]

    def create_wrapper(original_fn):
        @wraps(original_fn)
        def wrapper(*args, **kwargs):
            return original_fn(client=client, *args, **kwargs).to_dict()

        sig = inspect.signature(original_fn)
        params = list(sig.parameters.values())[1:]  # Skip first parameter (client)
        new_sig = sig.replace(parameters=params)
        wrapper.__signature__ = new_sig  # pyright: ignore[reportAttributeAccessIssue]
        wrapper.__name__ = NEW_PREFIX + submodule.name.removeprefix(OLD_PREFIX)

        return wrapper

    wrapped = create_wrapper(fn)

    mcp.add_tool(
        fn,
        title=wrapped.__name__,
        description=wrapped.__doc__ or "",
        structured_output=False,
    )
