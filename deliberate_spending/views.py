import os
from flask import render_template

from deliberate_spending import app

# Fill in your Plaid API keys - https://dashboard.plaid.com/account/keys
PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')
PLAID_PUBLIC_KEY = os.getenv('PLAID_PUBLIC_KEY')
# Use 'sandbox' to test with Plaid's Sandbox environment (username: user_good,
# password: pass_good)
# Use `development` to test with live users and credentials and `production`
# to go live
PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')
# PLAID_PRODUCTS is a comma-separated list of products to use when initializing
# Link. Note that this list must contain 'assets' in order for the app to be
# able to create and retrieve asset reports.
PLAID_PRODUCTS = os.getenv('PLAID_PRODUCTS', 'transactions')

# PLAID_COUNTRY_CODES is a comma-separated list of countries for which users
# will be able to select institutions from.
PLAID_COUNTRY_CODES = os.getenv('PLAID_COUNTRY_CODES', 'US,CA,GB,FR,ES')

# Parameters used for the OAuth redirect Link flow.
#
# Set PLAID_OAUTH_REDIRECT_URI to 'http://localhost:5000/oauth-response.html'
# The OAuth redirect flow requires an endpoint on the developer's website
# that the bank website should redirect to. You will need to whitelist
# this redirect URI for your client ID through the Plaid developer dashboard
# at https://dashboard.plaid.com/team/api.
PLAID_OAUTH_REDIRECT_URI = os.getenv('PLAID_OAUTH_REDIRECT_URI', '');
# Set PLAID_OAUTH_NONCE to a unique identifier such as a UUID for each Link
# session. The nonce will be used to re-open Link upon completion of the OAuth
# redirect. The nonce must be at least 16 characters long.
PLAID_OAUTH_NONCE = os.getenv('PLAID_OAUTH_NONCE', '');

@app.route('/')
def index():
  return render_template(
    'index.ejs',
    plaid_public_key=PLAID_PUBLIC_KEY,
    plaid_environment=PLAID_ENV,
    plaid_products=PLAID_PRODUCTS,
    plaid_country_codes=PLAID_COUNTRY_CODES,
    plaid_oauth_redirect_uri=PLAID_OAUTH_REDIRECT_URI,
    plaid_oauth_nonce=PLAID_OAUTH_NONCE,
  )
