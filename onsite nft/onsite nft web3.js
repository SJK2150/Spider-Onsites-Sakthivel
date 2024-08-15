const Web3 = require('web3');

const web3 = new Web3('https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID');

const contractABI = [
    
];

const contractAddress = '0xYourContractAddress';

const nftContract = new web3.eth.Contract(contractABI, contractAddress);

const account = '0xYourAccountAddress';

async function getTotalSupply() {
    const totalSupply = await nftContract.methods.totalSupply().call();
    console.log("Total Supply of NFTs:", totalSupply);
}

async function mintNFT(tokenURI) {
    const tx = nftContract.methods.mint(account, tokenURI);
    const gas = await tx.estimateGas({ from: account });
    const gasPrice = await web3.eth.getGasPrice();
    const data = tx.encodeABI();

    const txData = {
        from: account,
        to: contractAddress,
        data: data,
        gas,
        gasPrice
    };

    const signedTx = await web3.eth.accounts.signTransaction(txData, 'YOUR_PRIVATE_KEY');

    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log('Transaction receipt:', receipt);
}

async function getTokenURI(tokenId) {
    const tokenURI = await nftContract.methods.tokenURI(tokenId).call();
    console.log("Token URI:", tokenURI);
}

(async () => {
    await getTotalSupply();
    await mintNFT("ipfs://your-nft-metadata-link");
    await getTokenURI(1);
})();
