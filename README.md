# eth_vanity_wallet_generator
generate a vanity ethereum wallet address

To set up just run pip install web3 in your terminal and run eth_vanity_wallet_generator.py

Program uses multiprocessing so it will stress your cpu while running
Users can input any string they want as long as the characters are all in hexadecimal (a-fA-F, 0-9).
My 5900x hitting 11 threads at ~4ghz found 6 wallets with a prefix of length 6 in 7 hours, so that can give you some info on how long it may take to find you a wallet.
The first key in the wallet files is the public key, the 2nd one is the private key so keep it safe.
