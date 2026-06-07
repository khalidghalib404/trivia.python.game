# load existing data or items 
# 1. creating a new item 
# 2. mark the item as complete
# 3. save item
# 4. delete item


import json
 
file_name = "todo_list.json"

def load_tasks():
    try:
     with open(file_name, "r") as file:
        return json.load(file)
    except Exception as e:
     print("Error:", e)
    return {"tasks": []}


def save_tasks(tasks):
    
 try:
     print("saving:", tasks)
     with open(file_name, "w") as file:
         json.dump(tasks, file, indent=4)
         print("Tasks saved successfully.")
         
 except Exception as e:
    print("Failed to save:", e)

def view_tasks():
    pass

def create_task(tasks):
    description = input("Enter task description: ").strip()
    if description:
          tasks["tasks"].append({"description": description, "completed": False})
          save_tasks(tasks)
          print(tasks)
          print("Task added successfully.")
    else:
        print("Task description cannot be empty.")
    

def mark_task_complete():
    pass

def main():
    tasks = load_tasks( )
    # save_tasks({"tasks": ["saved task"]})
    # tasks = load_tasks()
    # print(tasks)
    
    
    
    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("good bye")
            break
        else:
            print("Invalid choice. Please try again.")
            print("Invalid choice. Please try again.")
            print("Invalid choice. Please try again.")
            
     
main()