from flask import render_template, redirect, url_for, request, abort
from flask_login import login_required, current_user
from models import Task, User
from database import db

@login_required
def task_list():
    # Check if user is admin
    # is_admin = 'admin' in [role.name for role in current_user.roles]
    is_admin = current_user.is_admin

    # Base query - admins see all tasks, others see only assigned tasks
    if is_admin:
        tasks = Task.query.all()
    else:
        tasks = Task.query.filter(Task.assigned_users.contains(current_user))

    # Get filter parameters
    filter_param = request.args.get('filter', 'pending')  # Default to pending
    title_filter = request.args.get('title', '')

    # Filter tasks based on status
    if filter_param == 'completed':
        tasks = [task for task in tasks if task.status]
    elif filter_param == 'pending':
        tasks = [task for task in tasks if not task.status]

    # Filter tasks based on title if provided
    if title_filter:
        tasks = [task for task in tasks if title_filter.lower() in task.title.lower()]

    return render_template('tasks/task_list.html',
                         tasks=tasks,
                         filter=filter_param,
                         title_filter=title_filter,
                         is_admin=is_admin)

@login_required
def mark_done(task_id):
    task = Task.query.get_or_404(task_id)
    
    # Check permissions
    if current_user.is_admin or current_user in task.assigned_users:
        task.status = True
        task.completed_at = db.func.now()
        task.completed_by = current_user
        db.session.commit()
        
    return redirect(url_for('task_list'))
