import logging
import random
from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])

def getAnswer():
    info = request.get_data(as_text=True)
    possible = info['possible_values']
    num = info['num_slots']
    guess = random.sample(possible, num)
    return guess
