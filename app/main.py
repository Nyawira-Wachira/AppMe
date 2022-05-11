import email
import os
import secrets
from PIL import Image
from email.policy import default
from flask import Flask, render_template, flash,redirect, url_for, flash, redirect, request, abort
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Mail,Message

# app = Flask(__name__)

mail=Mail(app)

