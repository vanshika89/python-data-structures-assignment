import os

tasks = [
    "Task1_DiscountRules.py",
    "Task2_MultipleOrders.py",
    "Task3_UserMenu.py",
    "Task5_LoopControl.py"
]

print("="*40)
print("RUNNING ASSIGNMENT 2: CONTROL FLOW")
print("="*40)

for task in tasks:
    print(f"\n--- Executing {task} ---")
    os.system(f"python {task}")
    print(f"\n--- {task} Completed ---")

print("\n" + "="*40)
print("ALL ASSIGNMENT TASKS PROCESSED")
print("="*40)