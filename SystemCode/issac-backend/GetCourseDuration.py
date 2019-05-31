from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import SimpleResponse, Confirmation, OutputContexts, Suggestions
import json
DATA_FILE = "data/GetCourseDuration.json"
with open(DATA_FILE, 'r') as infile:
    data = json.load(infile)

def process(req):
    params = req.get_paramters()
    print(params)
    #if has_params("graduate-programme", params):
    #    return askProgramme(req)
    
    graduate_programme_ptft = "" if "graduate-programme-ptft" not in params else params["graduate-programme-ptft"] 
    graduate_programme = "" if "graduate-programme" not in params else params["graduate-programme"]

    result = [item["answer"] for item in data 
                    if item["graduate-programme"] == graduate_programme 
                        and item["graduate-programme-ptft"] == graduate_programme_ptft]

    if len(result) == 0:
        return DialogflowResponse("There is no information for {0}".format(graduate_programme)).get_final_response()
    return DialogflowResponse("The course duration is {0}".format(result[0])).get_final_response()
    
