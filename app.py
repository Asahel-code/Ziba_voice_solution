from flask import Flask, request, Response
from send_sms import SMSClient

app = Flask(__name__)


@app.route('/initiate_call', methods=['GET', 'POST'])
def initate_call():
    session_id = request.form.get('sessionId')
    is_active = request.form.get('isActive')

    if is_active == '1':
        response = '<?xml version="1.0" encoding="UTF-8"?>'
        response += '<Response>'
        response += '<GetDigits timeout="30" finishOnKey="#" callbackUrl="https://9826-41-139-168-163.ngrok-free.app/processed_to_next">'
        response += '<Say>Welcome to Ziba. We offer personal training for tech courses for free and welcome voluteers to train newbees. Press 1 if you need access to tech free tech resource. pressed 2 to guide you if you are someone to guide you in your tech journey or press 3 to become a voluteer. After the number follow it with a hash sign</Say>'
        response += '</GetDigits>'
        response += '</Response>'

        return Response(response, content_type='application/xml')


@app.route('/processed_to_next', methods=['GET', 'POST'])
def connect_to_expert():
    session_id = request.form.get('sessionId')
    dtmfDigits = request.form.get('dtmfDigits')
    is_active = request.form.get('isActive')

    if is_active == '1':
        if dtmfDigits == '1':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<GetDigits timeout="30" finishOnKey="#" callbackUrl="https://9826-41-139-168-163.ngrok-free.app/access_to_material">'
            response += '<Say>We offer reading tech material for frontend developers, backend developer, machine learning and cloud. Press 1 if you need access to tech materail in frontend, press 2 if you need access to tech materail in backend, press 3 if you need access to tech materail in machine learning and press 3 if you need access to tech materail in cloud. After the number follow it with a hash sign</Say>'
            response += '</GetDigits>'
            response += '</Response>'
        elif dtmfDigits == '2':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<Dial phoneNumbers="+254711959117" />'
            response += '</Response>'
        elif dtmfDigits == '3':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<Dial phoneNumbers="+254769339499" />'
            response += '</Response>'

@app.route('/access_to_material', methods=['GET', 'POST'])
def access_to_material():
    session_id = request.form.get('sessionId')
    dtmfDigits = request.form.get('dtmfDigits')
    is_active = request.form.get('isActive')
    callerNumber = request.form.get('callerNumber')

    if is_active == '1':
        if dtmfDigits == '1*1':
            link = ""
            message =f"We have sent you the link to our resource on frontend. Click the link attach {link}"
            sms_client = SMSClient(callerNumber, message)
            sms_client.send_sms()

        elif dtmfDigits == '1*2':
            link = ""
            message =f"We have sent you the link to our resource on backend. Click the link attach {link}"
            sms_client = SMSClient(callerNumber, message)
            sms_client.send_sms()
        elif dtmfDigits == '1*3':
            link = ""
            message =f"We have sent you the link to our resource on machine learning. Click the link attach {link}"
            sms_client = SMSClient(callerNumber, message)
            sms_client.send_sms()
        elif dtmfDigits == '1*4':
            link = ""
            message =f"We have sent you the link to our resource on cloud. Click the link attach {link}"
            sms_client = SMSClient(callerNumber, message)
            sms_client.send_sms()

        return Response(response, content_type='application/xml')


# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)
