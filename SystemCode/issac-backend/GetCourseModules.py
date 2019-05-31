from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import SimpleResponse, Confirmation, OutputContexts, Suggestions
import json
DATA_FILE = "data/GetCourseModules.json"
with open(DATA_FILE, 'r') as infile:
    data = json.load(infile)

def process(req):
    params = req.get_paramters()
    if params["graduate-programme"] not in data:
        return DialogflowResponse("We currently do not have information for {0}. Please try again later".format(params["graduate-programme"])).get_final_response()

    result = data[params["graduate-programme"]]
    responseText = "\n".join(["{0}. {1}".format(num, ans) for num, ans in zip(result, range(1, len(result)+1))])

    return DialogflowResponse(responseText).get_final_response()
    
