import alerts

help_string = """
Help information: Please enter an AlertLevel such as Red, Orange, or Yellow. 
Detailed level information can be found here - https://www.cisecurity.org/cybersecurity-threats/alert-level/

Red indicates a severe risk of hacking, virus, or other malicious activity 
resulting in widespread outages and/or significantly destructive compromises 
to systems with no known remedy or debilitates one or more critical 
infrastructure sectors. 

Orange indicates a high risk of increased hacking, virus, or other malicious 
cyber activity that targets or compromises core infrastructure, causes 
multiple service outages, causes multiple system compromises, or compromises 
critical infrastructure.

Yellow indicates a significant risk due to increased hacking, virus, or other 
malicious activity that compromises systems or diminishes service.
"""

help_response = {
    "dialogAction": {
        "type": "ElicitSlot",
        "message": {
            "contentType": "PlainText",
            "content": help_string
        },
        "intentName": "AlertTeam",
        "slots": {
            "AlertLevel": None
        },
        "slotToElicit" : "AlertLevel"
    }
}


def handler(event, context):
    alert_type = event['currentIntent']['slots']['AlertLevel']
    print(alert_type)

    alert_response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": "Thanks, I have started the configured alerting procedures for a {0} Alert.".format(alert_type)
            }
        }
    }
    
    if alert_type.lower() == 'help':
        # If help AlertLevel - Then return help message and request a new slot
        return help_response
    else:
        # Otherwise - Run alerting playbooks and return the alert response
        alerts.send_alerts(alert_type)
        return alert_response
