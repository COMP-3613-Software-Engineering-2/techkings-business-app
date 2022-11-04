from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity


from App.controllers import (
    create_group, 
    get_all_groups,
    get_all_groups_json,
)

group_views = Blueprint('group_views', __name__, template_folder='../templates')


@group_views.route('/groups', methods=['GET'])
def get_group_page():
    groups = get_all_groups()
    return render_template('group.html', groups=groups)

@group_views.route('/api/groups', methods=['GET'])
def get_group_action():
    groups = get_all_groups_json()
    return jsonify(groups)

@group_views.route('/api/groups', methods=['POST'])
def create_group_action():
    data = request.json
    create_group(data['groupname'], data['password'])
    return jsonify({'message': f"group {data['groupname']} created"})


@group_views.route('/identify', methods=['GET'])
@jwt_required()
def identify_group_action():
    return jsonify({'message': f"groupname: {current_identity.groupname}, id : {current_identity.id}"})

@group_views.route('/static/groups', methods=['GET'])
def static_group_page():
  return send_from_directory('static', 'static-group.html')