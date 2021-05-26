def stringify(obj):
    if isinstance(obj, str):
        return "{}".format(obj)
    if isinstance(obj, list):
        result_list = []
        for val in obj:
            result_list.append(stringify(val))
        return result_list

    result_dict = {}
    for key, val in obj.items():
        result_dict[key] = stringify(val)
    return result_dict


k = {
    "key1" : "val1",
    "key2" : "val2",
    "key3" : ['l1', 'l2'],
    "key4" : {
        "KEY" : "VAL"
    }
}

ctr = {
  '2c79b47a-bc95-11eb-96a2-991e50b9d156': {
    'priceRef': ['2c79b6fa-bc95-11eb-96a2-991e50b9d156', '29c5c14c-bc95-11eb-96a2-991e50b9d156'], 
    'taxRef': ['2c79b902-bc95-11eb-96a2-991e50b9d156'], 
    'legacyId': '27', 
    'attributes': {
      'MopIDs': 'MOP_001', 'Status': 'Ticketed', 'Number': '088183535', 'StartValidityDate': '2021-04-29T00:00:00Z', 'ExternalID': '0000000000', 'EndValidityDate': '2021-04-29T23:59:59Z', 'TkoIDs': 'TKO_001', 'IssueDate': '2021-04-29', 'NumberOfPassengers': '1'
    }, 
    'deliveryMethod': {'attributes': {'DistribType': '004'}}, 
    'refundable': {
      'resultingAmountRef': '2c79c0be-bc95-11eb-96a2-991e50b9d156', 'refundableFee': {'feeAmountRef': '2c79c528-bc95-11eb-96a2-991e50b9d156'}, 'refundablePenalty': {'penaltyAmountRef': '2c79c294-bc95-11eb-96a2-991e50b9d156'}
      }, 
    'refids': ['2c78e9c8-bc95-11eb-96a2-991e50b9d156', '2c78fde6-bc95-11eb-96a2-991e50b9d156', '2c7984d2-bc95-11eb-96a2-991e50b9d156', '29c57be2-bc95-11eb-96a2-991e50b9d156', '29c59c30-bc95-11eb-96a2-991e50b9d156', '29c59726-bc95-11eb-96a2-991e50b9d156'], 
    'uid': '2c79b47a-bc95-11eb-96a2-991e50b9d156', 
    'attributesExtra': {'URLlink': 'https://recette.monbillet.sncf/e-billet?KEY=NAlQoDmKQ2755o0iMYzTEhE9HPpK2IW9MRzs1YAvLcO4nfHncJ8174HOAkKsd6vjDNW0ppAKGac-LANG=EN-TYPE=CONF', 'Type': '006'}
  }
}
print(stringify(ctr))
