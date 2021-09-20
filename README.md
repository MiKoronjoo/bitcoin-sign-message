# bitcoin-sign-message
Easy way to sign and verify message with Python3, using python-bitcoinlib

## Usage
### Sign a message
- One line command:
```sh
$ python3 signmessage.py --key L2rtaZbPsM2NBa2ncD4w9CPQdksPE3Za2jDyhcPioKoNVhyueUZ8 --msg mymessage                                 
H9NuIPimV7io25fFrngXMCVE/SsbSJDjLst1LFQRpq+cRFH3b0j6jYgCUjZeflWP/7G7bKpi2WsfcceM5ecFgtg=
```
- CLI:
```sh
$ python3 signmessage.py                                                                           
Private Key: L2rtaZbPsM2NBa2ncD4w9CPQdksPE3Za2jDyhcPioKoNVhyueUZ8
Message to sign: 0x7bfa940866d4d46c806dad2a63ff6e14c0724e03
IHJGwD7Smp19c9UzCe2sdyB1Jpk99i55keinuuQavp4XWkX9RXtHkJD2lQpEp4owyN/+FFhAdSeTl2260lRnVY0=
```

### Verify a message
- One line command:
```sh
$ python3 verifymessage.py --adr 1GzUrMqUxCKNAM6YJ2wRCDnv9xaCHNPUH1 --msg mymessage --sig H9NuIPimV7io25fFrngXMCVE/SsbSJDjLst1LFQRpq+cRFH3b0j6jYgCUjZeflWP/7G7bKpi2WsfcceM5ecFgtg=
True
```
- CLI:
```sh
$ python3 verifymessage.py                                                                                                                                                        
Address: 1GzUrMqUxCKNAM6YJ2wRCDnv9xaCHNPUH1
Message: 0x7bfa940866d4d46c806dad2a63ff6e14c0724e03
Signature: IEfYrmX9s5ypLHcRI7nXOtTC7SUemyAu2ziPcDR6kUdpW03Nv27w2gerihYCqc/2l1lFUoabYMKfYeavr+7wCew=
True
```
