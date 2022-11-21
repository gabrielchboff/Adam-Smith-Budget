from flask import Flask

app = Flask(__name__)

app.route('/', methods=['GET'])
def home():
    return 'infos'

app.route('/transaction/add', methods=['POST'])
def add_transaction():
    return ''

app.route('/transaction/<int:transaction_id>/delete', methods=['POST'])
def delete_transaction(transaction_id):
    return ''

app.route('/transaction/<int:transaction_id>/edit', methods=['POST'])
def edit_transaction(transaction_id):
    return ''

app.route('/transaction/list', methods=['GET'])
def transactions():
    return ''

