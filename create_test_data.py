from app import app, db
from models import User, Task
from datetime import datetime

def create_test_data():
    with app.app_context():
        # Get ramill user
        ramill = User.query.filter_by(username='ramill').first()
        
        # Create test tasks
        tasks = [
            Task(
                title='Implement Login System',
                description='Create authentication system with Flask-Login',
                created_at=datetime.utcnow()
            ),
            Task(
                title='Design Database Schema',
                description='Create SQLite database models and relationships',
                created_at=datetime.utcnow()
            ),
            Task(
                title='Add CSRF Protection',
                description='Implement CSRF tokens for forms security',
                created_at=datetime.utcnow()
            ),
            Task(
                title='Create Admin Interface',
                description='Build admin dashboard for task management',
                created_at=datetime.utcnow()
            )
        ]
        
        # Add tasks to database and assign to ramill
        for task in tasks:
            task.assigned_users.append(ramill)
            db.session.add(task)
        
        db.session.commit()
        print("Test tasks created and assigned to ramill successfully!")

if __name__ == '__main__':
    create_test_data()
