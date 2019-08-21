import models

import os
import sys
import secrets
from PIL import Image

from flask import Blueprint, request, jsonify, url_for, send_file
# Blueprint -- they record operations to execute (their controllers)

from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from playhouse.shortcuts import model_to_dict


user = Blueprint('user', 'user', url_prefix='/user')

# ================ REGISTER ================ #
@user.route('/register', methods=['POST'])
def register():
	# form info
	payload = request.get_json()
	print(payload, '<--- payload in user register route')

	payload['email'].lower()

	try:
		models.User.get(models.User.email == payload['email'])

		return jsonify(data={}, status={'code': 401, 'message': 'A user with that username and/or email already exists'})

	except models.DoesNotExist:

		payload['password'] = generate_password_hash(payload['password'])

		user = models.User.create(**payload)
		print(user, '<--- registered user')

		login_user(user)

		user_dict = model_to_dict(user)
		print(user_dict, '<--- user_dict in register route')

		del user_dict['password']

		return jsonify(data=user_dict, status={'code': 200, 'message': 'Register successful'})

# ================ LOGOUT ================ #
@user.route('/logout', methods=['POST'])
def logout():
	logout_user()
	return redirect('http://localhost:8000/')





