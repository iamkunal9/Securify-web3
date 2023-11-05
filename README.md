# Securify Web3
## _Ml based threat intelligence_
_Build for the MNIT 24HACK Hackathon_

Securify is a ml based tool which can be used for threat monitoring and fraud prevention

Process:-
- Clone the repo
- run `python3 main.py`
- Head to `http://localhost:5000` in your web browser
- Now just put the token address you want to check
- ✨Magic ✨

## Features

- Model can be retrained by providing the custom bytecodes of diffrent scam contracts and running the `python3 train.py`
- If the token is not scam the code will then move forward to simulate a buy and sell of the specific token using hardhat forked mainnet
- Using the result of the simulation the bytecode is added/updated in the dataset and dataset will be retrained.
-  Web based access using python flask!!!
- Easy and quick

## Future scopes

- Using more roboust algo for the model traning 
- Using more accurate dataset
- Making the ui more attractive
- The mempool can be monitored using alchemy websocket and checking the pending txns we can push the contract bytecode to the module and check for the scam or not
- PEACE


## License

MIT

**Free Software, Hell Yeah!**

