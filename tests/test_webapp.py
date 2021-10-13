#from app.co

from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm

import unittest

def home_page():
    return render_template('home.html')

if __name__ == "__main__":
    unittest.main()