#!/usr/bin/env python3

import requests
import json
import toml


config = toml.load("proposals.toml")


def sendTelegramMessage(message):
    url = f"https://api.telegram.org/bot{config['telegram']['token']}/sendMessage?chat_id={config['telegram']['chat_id']}&text={message}"
    headers = { 'Accept': 'application/json' }
    data = requests.get(url, headers=headers).text

def debugPrint(output):
    if config['loglevel'].upper() == "DEBUG":
        print(output)

for status in config['status']:
    debugPrint(f"Proposals with status {status}")
    for network in config['networks']:
        debugPrint(f" For netowrk {network}")
        url = f"{config['networks'][network]['lcd']}/cosmos/gov/v1beta1/proposals?proposal_status={config['status'][status]}"
        headers = { 'Accept': 'application/json' }
        data = requests.get(url, headers=headers).text
        proposals=json.loads(data)
        for proposal in proposals['proposals']:
            url = f"{config['networks'][network]['lcd']}/gov/proposals/{proposal['proposal_id']}/votes/{config['networks'][network]['voter']}"
            data = requests.get(url, headers=headers).text
            vote_data = json.loads(data)
            try:
                vote = vote_data['result']['options'][0]['option']
            except:
                vote = "DID_NOT_VOTE"
                message=f"There is a proposal for {network.upper()} network on which you DID NOT vote\n\nProposal ID: {proposal['proposal_id']} -> {config['networks'][network]['proposal_link']}/{proposal['proposal_id']}"
                sendTelegramMessage(message)
            debugPrint(f"  Porposal {proposal['proposal_id']} -> {vote}")
    debugPrint("\n")
