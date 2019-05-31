from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import SimpleResponse, Confirmation, OutputContexts, Suggestions
import json
DATA_FILE = "data/GetApplicationDeadline.json"
with open(DATA_FILE, 'r') as infile:
    data = json.load(infile)

def process(req):
    params = req.get_paramters()
    if params["graduate-programme"] not in data:
        return DialogflowResponse("We currently do not have information for {0}. Please try again later".format(params["graduate-programme"])).get_final_response()
    return DialogflowResponse(data[params["graduate-programme"]]).get_final_response()
    
