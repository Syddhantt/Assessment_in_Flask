from flask import jsonify, render_template, request, Response, g, Markup
import json
import MySQLdb
from flask.ext.login import current_user, login_user

from functions import app
from models import User

@app.before_request
def db_connect():
  g.conn = MySQLdb.connect(host='localhost',
                              user='root',
                              passwd='',
                              db='ohm_assessment')
  g.cursor = g.conn.cursor()

@app.after_request
def db_disconnect(response):
  g.cursor.close()
  g.conn.close()
  return response

def query_db(query, args=(), one=False):
  g.cursor.execute(query, args)
  rv = [dict((g.cursor.description[idx][0], value)
  for idx, value in enumerate(row)) for row in g.cursor.fetchall()]
  return (rv[0] if rv else None) if one else rv

@app.route('/community', methods=['GET'])
def community():

    login_user(User.query.get(1))

    result = query_db("SELECT u.user_id, u.display_name, u.tier, u.point_balance, COALESCE(GROUP_CONCAT(r.attribute), '-') as phone_number, COALESCE(r2.attribute, 'Location Unknown') as location FROM ohm_assessment.user u LEFT JOIN ohm_assessment.rel_user_multi r ON (u.user_id = r.user_id AND r.rel_lookup='PHONE') LEFT JOIN ohm_assessment.rel_user r2 ON (u.user_id = r2.user_id AND r2.rel_lookup='LOCATION') GROUP BY u.user_id ORDER BY signup_date DESC LIMIT 5")
    data = json.dumps(result)


    args = {
            'gift_card_eligible': True,
            'cashout_ok': True,
            'user_below_silver': current_user.is_below_tier('Silver'),
            'resp': Markup(data)
    }

    return render_template("community.html", **args)
