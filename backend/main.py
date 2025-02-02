from flask import request, jsonify,send_from_directory
from config import app, db
from models import Contact
import os

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

    '''The jsonify() function is useful in Flask apps because it
     automatically sets the correct response headers
      and content type for JSON responses,'''

@app.route("/create_contact", methods = ["POST","OPTIONS"])
def create_contact():

    if request.method == "OPTIONS":
        return jsonify({"message": "CORS Preflight OK"}), 200
    
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    

    if not first_name or not last_name or not email:
        return(
            jsonify({"message": "You must include a first name, last name and email"}),
            400,
        )

    new_contact = Contact(first_name = first_name, last_name = last_name, email = email)

    try:
        db.session.add(new_contact)
        db.session.commit()
        
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Contact created successfully"}), 201

@app.route("/update_contact/<int:user_id>" , methods  = ["PATCH","PUT"])
def update_contact(user_id):
     contact = Contact.query.get(user_id)

     if not contact:
        return jsonify({"message": "User not found"}),404

     data = request.json
     contact.first_name = data.get("firstName",contact.first_name)
     contact.last_name = data.get("lastName",contact.last_name)
     contact.email = data.get("email",contact.email)

     db.session.commit()

     return jsonify({"message":"user updated"}), 200

@app.route("/delete_contact/<int:user_id>",methods = ["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}),404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message":"user deleted"}), 200



if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    port = int(os.environ.get('PORT', 5000)) 

    app.run(host='0.0.0.0', port=port, debug=True)