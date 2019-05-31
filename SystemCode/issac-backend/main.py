import requests
from flask import Flask, request, make_response, jsonify
from pydialogflow_fulfillment import DialogflowRequest
from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import SimpleResponse, Confirmation, OutputContexts, Suggestions
import GetCourseDescription
import GetGraduateProgrammeFee
import GetCourseLearningOutcome
import GetCourseDuration
import GetApplicationDeadline
import GetCourseAdmissionRequirements
import GetCourseApplicationProcess
import GetCourseCareerProspects
import GetCourseModules


app = Flask(__name__)

def getjson(url):
    resp = requests.get(url)
    print(url)
    return resp.json()

# *****************************
# WEBHOOK MAIN ENDPOINT : START
# *****************************
PROJECT_ID = 'issac-b2751'

@app.route('/', methods=['POST'])
def webhook():
    req = DialogflowRequest(request.data)
    intent_name = req.get_intent_displayName()
    print(intent_name)
    if intent_name == "GetCourseDescription":
        return make_response(GetCourseDescription.process(req))
    if intent_name == "GetCourseLearningOutcome":
        return make_response(GetCourseLearningOutcome.process(req))
    if intent_name == "GetCourseDuration":
        return make_response(GetCourseDuration.process(req))
    if intent_name == "GetApplicationDeadline":
        return make_response(GetApplicationDeadline.process(req))
    if intent_name == "GetCourseAdmissionRequirements":
        return make_response(GetCourseAdmissionRequirements.process(req))
    if intent_name == "GetCourseApplicationProcess":
        return make_response(GetCourseApplicationProcess.process(req)) 
    if intent_name == "GetCourseCareerProspects":
        return make_response(GetCourseCareerProspects.process(req))
    if intent_name == "GetCourseModules":
        return make_response(GetCourseModules.process(req))
    if intent_name=="GetGraduateProgrammeFee" or intent_name =="GetGraduateProgrammeFee-ReplyProgramme" or intent_name == "GetGraduateProgrammeFee-ReplyApplicationGroup":
        return make_response(GetGraduateProgrammeFee.process(req))
    if intent_name=="GetGraduateProgrammeFee2":
        print(str(req.get_session()))
        print(str(req.get_response_id()))
        res = DialogflowResponse("This is a new response")
        print(res.get_final_response())
        #__init__(self,project_id,session_id,context_name,context_life_span, context_parameters):
        return make_response(res.get_final_response())       
    # TODO: STEP 2
    # Write your code here..
    # write some if/else to check for the correct intent name.
    # Write code to call the getWeatherIntentHandler function with appropriate input

    if intent_name == "Weather Intent":
        respose_text = "weather"

    else:
        respose_text = "No intent matched from fullfilment code."
    # Branching ends here

    # Finally sending this response to Dialogflow.
    return make_response(jsonify({"fulfillmentText": respose_text}))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
