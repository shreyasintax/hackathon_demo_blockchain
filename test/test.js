import Web3 from 'web3';
const web3 = new Web3('http://127.0.0.1:8545');

// Example of getting the balance of the first account
web3.eth.getAccounts()
    .then(accounts => {
        const firstAccount = accounts[0];
        return web3.eth.getBalance(firstAccount);
    })
    .then(balance => {
        console.log(`Balance of account: ${web3.utils.fromWei(balance, 'ether')} ETH`);
    })
    .catch(error => {
        console.error('Error:', error);
    });
