from http.client import HTTPException
from flask import Blueprint, request, jsonify
from services.summarization_service import summarize_text
from models.summariz_request import SummarizeRequest
from models.summarize_response import SummarizeResponse
from services.auth import validate_token

summarization_controller = Blueprint('summarization_controller', __name__)

@summarization_controller.route('/summarize', methods=['POST'])
def summarize():
    """
    Endpoint to summarize a given code.
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input, request body is required'}), 400

    try:
        # Validate the API token from the request headers
        api_key = request.headers.get('x-api-key')
        if not api_key or not validate_token(api_key):
            return jsonify({'error': 'Unauthorized'}), 401

        # Validate and parse the request data using SummarizeRequest
        req = SummarizeRequest(**data)

        # Perform summarization
        summary = summarize_text(req.code, req.type_, req.name)
        response = SummarizeResponse(content=summary)

        return jsonify(response.model_dump())
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500