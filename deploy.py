#Following tutuorial from FreecodeCamp.org with Patrick Collins 
from solcx import compile_standard

with open("./PraxisToken.sol", "r") as file:
    token_file = file.read()

#compile solidity file using py-solc-x

compiled_sol = compile_standard(
    "language" : "Solidity",
    "sources" : {"PraxisToken.sol": {"content":token_file}},
    "setting" : {
        
    }
)