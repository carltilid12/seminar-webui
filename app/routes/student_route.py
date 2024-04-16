from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

student_bp = Blueprint('student_bp',__name__)

@student_bp.route('/')
def home():
    return render_template("home.html")

@student_bp.route('/students', methods=['GET'])
def get_students():
    return render_template("home.html")