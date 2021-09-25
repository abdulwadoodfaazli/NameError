import logging
import random
import json
from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])

def getAnswer():
    result = {}
    info = request.get_json()
    possible = info.get('possible_values')
    num = info.get('num_slots')
    guess = random.sample(possible, num)
    result['answer'] = guess
    return result
