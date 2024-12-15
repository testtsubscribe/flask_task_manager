from flask import Flask
from database import db
from models import User, Task
import random



def assign_all_tasks_to_users():
    """Assign all tasks to each user"""
    with app.app_context():
        users = User.query.all()
        tasks = Task.query.all()
        
        for task in tasks:
            # Clear existing assignments
            task.assigned_users = []
            
            # Assign all users to this task
            task.assigned_users.extend(users)
            db.session.add(task)
            print(f"Task '{task.title}' assigned to: {[user.username for user in users]}")
        
        db.session.commit()
        print("All tasks have been assigned to all users successfully!")


"""
def assign_random_tasks():
    #Randomly assign tasks to users
    with app.app_context():
        users = User.query.all()
        tasks = Task.query.all()
        
        for task in tasks:
            # Randomly select 1-3 users for each task
            num_assignees = random.randint(1, 3)
            selected_users = random.sample(users, min(num_assignees, len(users)))
            
            # Clear existing assignments
            task.assigned_users = []
            
            # Assign new random users
            for user in selected_users:
                task.assigned_users.append(user)
            
            db.session.add(task)
            print(f"Task '{task.title}' assigned to: {[user.username for user in selected_users]}")
        
        db.session.commit()
        print("Task assignment completed successfully!")
"""

if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    db.init_app(app)
    #assign_random_tasks()
    assign_all_tasks_to_users()

