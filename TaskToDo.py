import sys

def print_success():
  print("Task Added Successfully!!!")

def add_task(task):
  try:
    with open("Task_List.txt", "r") as f:
      tasks = f.readlines()

    added_tasks = set()
    for task_line in tasks:
      added_tasks.add(task_line.strip())

    if task in added_tasks:
      return "Task already exists!"

    with open("Task_List.txt", "a") as f:
      f.write(task + "\n")

    added_tasks.add(task)

    return "Successfully added task!"
  except Exception as e:
    return "Failed to add task: " + str(e)

def view_tasks():
  try:
        with open("Task_List.txt", "r") as f:
            tasks = f.readlines()

        if not tasks:
            print("Task list is empty!")
        else:
            print("To-do list:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task.strip()}")

  except Exception as e:
    print("Failed to view tasks: " + str(e))

def remove_task(index):
    try:
        with open("Task_List.txt", "r") as f:
            tasks = f.readlines()

        if not tasks:
            return "Task list is empty!"

        try:
            index = int(index)
        except ValueError:
            return "Invalid task number! Please enter a valid number."

        if index < 1 or index > len(tasks):
            return "Invalid task number!"

        removed_task = tasks.pop(index - 1)

        with open("Task_List.txt", "w") as f:
            f.writelines(tasks)

        return f"Task '{removed_task.strip()}' removed successfully!"
    except Exception as e:
        return "Failed to remove task: " + str(e)
    
    
def main():
  while True:
    print(" ")
    print("__Operations to Perform__")
    print("1. Add a task")
    print("2. View the to-do list")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice:: ")

    if choice == "1":
      print(" ")
      task = input("Enter the task to add: ")
      add_task_result = add_task(task)

      if add_task_result == "Successfully added task!":
        print(add_task_result)
      else:
        print(add_task_result)

    elif choice == "2":
      view_tasks()

    elif choice == "3":
      print(" ")
      index = input("Enter the task number to remove: ")
      remove_task_result = remove_task(index)
      print(remove_task_result)
      if remove_task_result == "Task removed successfully!":
        view_tasks()

    elif choice == "4":
      print("Thank you for using TaskToDo_List")
      break
    else:
      print("Invalid choice.")

if __name__ == "__main__":
  main()
