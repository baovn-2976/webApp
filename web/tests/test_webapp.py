#from app.co

from market import app
#from flask import render_template, redirect, url_for, flash, request
#rom market.models import Item, User
#from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm


import unittest

def test_home_page_hello():
   # return render_template('home.html')
   reponse = app.test_client().get('/')

   assert reponse.status_code == 200

   assert reponse.data == b'Hello, World!'

if __name__ == "__main__":
    unittest.main()