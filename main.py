from utils import create_task, display_tasks, update_task, mark_complete, delete_task
def main():
  tasks = display_tasks()
  while True:
    print("n=== Personal Task Manager ===")
    print("1. Create Task")
    print("2. Display Tasks")
    print("3. Update Task")
    print("4. Mark Task Complete")
    print("5. Delete Task")

    choice = input("Enter Selection: ")
    if choice == "1":
      create_task(tasks)
    elif choice == "2":
      display_tasks(tasks)
    elif choice == "3":
      update_task(tasks)
    elif choice == "4":
      mark_complete(tasks)
    elif choice == "5":
      delete_task(tasks)
    else:
      print("Invalid selection. Try again")

if __name__ == "__main__":
  main()

