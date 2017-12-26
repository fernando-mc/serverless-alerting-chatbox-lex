
def run_alerting_playbook(level):
    print("Runing an alerting playbook like emailing, slacking and SMSing people")
    print("Running playbook for alert level of: " + level)

help_string = """
Help information: Please enter an AlertLevel such as Red, Orange, or Yellow. 
Red alerts are critical issues impacting production services, or that expose personally identifiable user data.
Orange alerts are isseues impacting production services that do not have significant negative consequences.
Yellow alerts are issues that you think need review by a manager.
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
        print(help_response)
        return help_response
    else:
        # Otherwise return the alert response and run alerting playbooks
        run_alerting_playbook(alert_type)
        print(alert_response)
        return alert_response
