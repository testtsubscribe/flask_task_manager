from app import app, db
from models import User

def update_users():
    with app.app_context():
        # Remove admin status
        user = User.query.filter_by(username='ramill').first()
        if user:
            user.is_admin = False
            db.session.commit()
            print(f"Removed admin status from {user.username}")

        # Delete user
        user_to_delete = User.query.filter_by(username='ramilla').first()
        if user_to_delete:
            db.session.delete(user_to_delete)
            db.session.commit()
            print(f"Deleted user: {user_to_delete.username}")

if __name__ == '__main__':
    update_users()
