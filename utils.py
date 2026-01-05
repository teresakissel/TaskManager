import json
import os

FILE_NAME = "tasks.json"

def create_task(tasks):
  task_id = len(tasks) + 1
  title = input("Enter task title")
  desc = input("Enter task description")
  priority = input("Enter task priority (Low/Medium/High/Urgent)")
  due_date = input("Enter task due date")

task = {
  "id" = task_id
      
  
