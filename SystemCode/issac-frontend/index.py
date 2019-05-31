from flask import Flask, request, jsonify, render_template
import os
import dialogflow
import requests
import json

app = Flask(__name__)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ISSAC-702e5c96171c.json'
os.environ['DIALOGFLOW_PROJECT_ID'] = 'issac-b2751'




@app.route('/')
def index():
    print('here is main')
    return render_template('index.html')

def detect_intent_texts(project_id, session_id, text,knowledge_base_id, language_code):
    import dialogflow_v2beta1 as dialogflow
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        
        query_input = dialogflow.types.QueryInput(text=text_input)
        
        knowledge_base_path = dialogflow.knowledge_bases_client.KnowledgeBasesClient.knowledge_base_path(project_id, knowledge_base_id)
        
        query_params = dialogflow.types.QueryParameters(knowledge_base_names=[knowledge_base_path])
        
        response = session_client.detect_intent(
            session=session, query_input=query_input,
            query_params=query_params)

        return response.query_result.fulfillment_text


@app.route('/send_message', methods=['POST'])
def send_message():
    print('here is send_message')
        
    message = request.form['message']
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    fulfillment_text = detect_intent_texts(project_id, "unique", message,"MzExMTU5MTUxODMyNzAxMzM3Ng", 'en')
    response_text = { "message":  fulfillment_text }
                        
    return jsonify(response_text)

# run Flask app
if __name__ == "__main__":
    app.run()