from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, current_app
import requests

API_BASE_URL = 'http://127.0.0.1:5000/'

course_bp = Blueprint('course_bp',__name__)

@course_bp.route('/courses', methods=['GET', 'POST', 'DELETE'])
def get_courses():
    if request.method == 'POST':
        course_name = request.form['course_name']
        response = requests.post(API_BASE_URL + '/course', json={'course': course_name})
        if response.status_code == 200:
            print('Course added successfully', 'success')
        else:
            print('An error occurred while adding the course', 'danger')
        return redirect(url_for('course_bp.get_courses'))
    
    response = requests.get(API_BASE_URL + '/courses')
    courses = response.json()['data'][0][0]
    course_names = [{'course_id': course['course_id'], 'course_name': course['course_name']} for course in courses]

    return render_template("course.html", courses=course_names)

@course_bp.route('/course/<course_id>', methods=['POST'])
def edit_course(course_id):
    course_name = request.form['course_name']
    response = requests.put(API_BASE_URL + '/course/' + course_id, json={'course': course_name})
    if response.status_code == 200:
        print('Course updated successfully', 'success')
    else:
        print('An error occurred while updating the course', 'danger')
    return redirect(url_for('course_bp.get_courses'))

@course_bp.route('/course/<course_id>', methods=['DELETE'])
def delete_course(course_id):
    response = requests.delete(API_BASE_URL + '/course/' + course_id)
    if response.status_code == 200:
        print('Course deleted successfully', 'success')
    else:
        print('An error occurred while deleting the course', 'danger')
    return redirect(url_for('course_bp.get_courses'))   