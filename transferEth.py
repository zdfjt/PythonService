def main():
    logMsg(rpc)
    logMsg(key)
    w3 = Web3(Web3.HTTPProvider(rpc))
    acc = w3.eth.account.from_key(key)
    sendValue= w3.to_wei(0,'ether')
    toAddr = w3.to_checksum_address("0x05bA432637a63078DaDC1869d64d66084f0B12d0")
    chain_id = w3.eth.chain_id
    # _data = '0x'+ w3.keccak(text='exactInputSingle((address,address,uint24,address,uint256,uint256,uint256,uint160,bool))').hex()[2:10]
    logMsg(acc.address)
    maxFeePerGas = w3.to_wei(5, 'gwei')
    maxPriorityFeePerGas = w3.to_wei(0.2, 'gwei')
    send_data ='0x1231234'
    print(send_data)
    current_nonce = w3.eth.get_transaction_count(acc.address)
    trx_dict = dict(
        nonce=current_nonce,
        gasPrice= maxFeePerGas,
        gas=295529 ,
        to=toAddr,
        value=sendValue,
        data=send_data,
        chainId= chain_id)
    signed = acc.sign_transaction(trx_dict)
    trxHash = w3.eth.send_raw_transaction(signed.rawTransaction).hex()
    trxStatus = wait_until_over(w3,hash)

    return trxStatus,trxHash
trxStatus,trxHash  =  main()
