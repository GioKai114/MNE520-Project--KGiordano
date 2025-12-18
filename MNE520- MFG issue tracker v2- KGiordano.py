# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 18:14:35 2025

@author: giord
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 15:22:17 2025

@author: giord
"""

import json
import os

# ------------------------------
# File paths
# ------------------------------
COUNTER_FILE = "counters.json"
ISSUE_FILE = "issues.json"

# ------------------------------
# Load counters
# ------------------------------
if os.path.exists(COUNTER_FILE):
    with open(COUNTER_FILE, "r") as file:
        counters = json.load(file)
else:
    counters = {"AQE": 100,
                "BIQ": 100,
                "CPI": 100,
                "DEV": 100 }

# ------------------------------
# Load issues
# ------------------------------
if os.path.exists(ISSUE_FILE):
    with open(ISSUE_FILE, "r") as file:
        issues = json.load(file)
else:
    issues = {"AQE": {},
              "BIQ": {},
              "CPI": {},
              "DEV": {} }

# ------------------------------
# Action functions
# ------------------------------

# ------------------------------
# SAVING ISSUE FILE
# ------------------------------
def save_all():
     #Save counters and issue dictionaries to JSON files.
    with open(COUNTER_FILE, "w") as file:
        json.dump(counters, file, indent=4)

    with open(ISSUE_FILE, "w") as file:
        json.dump(issues, file, indent=4)

# ------------------------------
# CREATING NEW ISSUE
# ------------------------------
def create_issue(issue_type):
    #Create a new issue of a given type.
    counters[issue_type] += 1
    issue_id = f"{issue_type}{counters[issue_type]}"

    desc= input("Enter your issue description: \n\n-------> ")
    issue_status= ("OPEN")

    issues[issue_type][issue_id] = {"Description" : desc,
                                         "Status" : issue_status}

    save_all()  # Save after creating issue
    print(f"\n------------------------------\nIssue created: {issue_id}\n"
          "------------------------------\n")
    
# ------------------------------
# EDITING EXISTING ISSUE
# ------------------------------
def edit_issue(issue_type):
    if issue_type not in issues:
        print(f"Error: Issue type '{issue_type}' not found.")
        return

    print(f"Which {issue_type} issue do you want to edit?\n")
    current_issues = issues[issue_type]

    # Prints list of issue ID (key) and issue descriptions/status (value)
    for key, value in current_issues.items():
        print(f"ID: {key}, \n    Details: {value}")

    editing_id = input("\n\n----\n Enter Issue ID to edit (i.e. AQE100): \n ---> \n").strip().upper()

    # -------------------------
    # Check if the entered ID exists in the current issue type dictionary
    # -------------------------
    if editing_id in current_issues:
        print(f"\n\n-----\nCurrently editing issue ID: {editing_id}\n")
        print(f"Current details: {current_issues[editing_id]}\n-----\n")

        # ------------------------------
        # UPDATE DIRECTORY VALUE(S)
        # ------------------------------
        new_description = input("\nEnter new description (or press Enter to keep current): ").strip()
        new_status = input("\nEnter new status (e.g., 'OPEN', 'CLOSED', 'RESOLVED'; or press Enter): ").strip().upper()

        if new_status not in ['OPEN','CLOSED', 'RESOLVED']:
            print("Invalid input")
            return

        if new_description != "":
            # Direct assignment updates the dictionary
            issues[issue_type][editing_id]['Description'] = new_description
            save_all() 
        if new_status != "":
            # Direct assignment updates the dictionary
            issues[issue_type][editing_id]['Status'] = new_status
            save_all() 

            
            
        print(f"\n\n-----\nUpdated details for {editing_id}:\n-----\n {issues[issue_type][editing_id]}")
        
    else:
        print(f"\nError: Issue ID '{editing_id}' not found for issue type '{issue_type}'.")
        

# ------------------------------
# DELETING A SINGLE ISSUE RECORD
# ------------------------------


def delete_issue(issue_type):
    print(f"Which {issue_type} issue do you want to delete?\n")
    current_issues = issues[issue_type]

    # ----------------------
    # Prints list of issue ID and issue details
    # ----------------------
    if not current_issues:
        print("No issues recorded for this type.")
        return

    for key, value in current_issues.items():
        print(f"ID: {key}, \n    Details: {value}")

    deleting_id = input("\n\n----\n Enter Issue ID to delete (i.e. AQE100): \n ---> ").strip().upper()

    # ----------------------
    # Check if the entered ID exists
    # ----------------------
    if deleting_id in current_issues:
        print(f"\nCurrent details: {current_issues[deleting_id]}\n-----\n")
        confirmation = input("\nARE YOU SURE YOU WANT TO DELETE THIS ISSUE?"
                             "\n 1-NO"
                             "\n 2-YES"
                             "\n-------> ").strip().upper()
        if confirmation in ["2", "YES"]:
            current_issues.pop(deleting_id)
            save_all()
            print(f"\nIssue {deleting_id} has been deleted successfully.")
        else:
            print("\nDeletion cancelled.")
    else:
        print(f"\nError: Issue ID '{deleting_id}' not found for issue type '{issue_type}'.\n")
                

# ------------------------------
# Main Program
# ------------------------------

print("The following program will initiate and track issues within the manufacturing facility.\n----")

def run_program():
    action = input("\nSelect an option number:\n"
                   "1 - NEW ISSUE\n"
                   "2 - VIEW ISSUES\n"
                   "3 - EDIT ISSUES\n"
                   "4 - EXIT\n"
                   "\n5 - DELETE A SINGLE ISSUE RECORD\n"
                   "\n6 - DELETE ALL DATA\n"
                   "-------> " ).upper().strip()

    # --------------------------
    # Create new issue
    # --------------------------
    if action == "1":
        print("\n------------------------------\nCreating new issue...\n"
              "------------------------------\n")
        issue_type = input("Select type:\n"
                           "1 - AQE\n"
                           "2 - BIQ\n"
                           "3 - CPI\n"
                           "4 - DEVIATION\n"
                           "-------> ").upper().strip()

        type_map = { "1": "AQE", "AQE": "AQE",
                     "2": "BIQ", "BIQ": "BIQ",
                     "3": "CPI", "CPI": "CPI",
                     "4": "DEV", "DEVIATION": "DEV", }

        if issue_type in type_map:
            create_issue(type_map[issue_type])
        else:
            print("Invalid issue type.\n")
            return

    # --------------------------
    # View issues
    # --------------------------
    elif action == "2":
        print("\n------------------------------\nVIEWING ISSUES...\n"
              "------------------------------\n")
        view_type = input("Select issue type to view:\n"
                           "1 - AQE\n"
                           "2 - BIQ\n"
                           "3 - CPI\n"
                           "4 - DEVIATION\n"
                           "-------> ").upper().strip()
        # --------------------------
        # ALLOWS INPUT OF "1" or "AQE" to result to "AQE"
        # --------------------------
        type_map = { "1": "AQE", "AQE": "AQE",
                     "2": "BIQ", "BIQ": "BIQ",
                     "3": "CPI", "CPI": "CPI",
                     "4": "DEV", "DEVIATION": "DEV", }


        if view_type in type_map:
            view = type_map[view_type]
            print(f"\n---- {view} ISSUES ----")
            
            # --------------------------
            # CHECKS IF VIEWING LIST IS EMPTY OR DOESN'T EXIST
            # --------------------------
            if len(issues[view]) == 0:
                print("No issues recorded.")
            else:
                # --------------------------
                # VIEW CODE
                # --------------------------
                print(json.dumps(issues[view], indent=2))                
            return
        else:
            print("Invalid selection.\n")
            return
            
    # --------------------------
    # Edit Issue
    # --------------------------
    elif action == "3":
        print("\n------------------------------\nEditing issue...\n"
              "------------------------------\n")
        issue_type = input("Select type:\n"
                           "1 - AQE\n"
                           "2 - BIQ\n"
                           "3 - CPI\n"
                           "4 - DEVIATION\n"
                           "-------> ").upper().strip()

        type_map = { "1": "AQE", "AQE": "AQE",
                     "2": "BIQ", "BIQ": "BIQ",
                     "3": "CPI", "CPI": "CPI",
                     "4": "DEV", "DEVIATION": "DEV", }
        editing = type_map[issue_type]
        
        # --------------------------
        # CHECKS IF EDITING LIST IS EMPTY OR DOESN'T EXIST
        # --------------------------
        if not issues.get(editing):
            print(f"\nNo issues found for type:  {editing}. Cannot edit.\n")
            return
        else: 
            # --------------------------
            # RUN THE EDITING CODE
            # --------------------------
            
            edit_issue(type_map[issue_type])
            return
       
    
    # --------------------------
    # Exit
    # --------------------------
    elif action == "4":
        print("Exiting program...")
        save_all()
        return
 
    
 
    
    # --------------------------
    # DELETE A SINGLE ISSUE RECORD
    # --------------------------
    elif action == "5":
        print("\n------------------------------\nDELETING A SINGLE ISSUE FROM RECORDS...\n"
              "------------------------------\n")
        issue_type = input("Select issue type to delete:\n"
                           "1 - AQE\n"
                           "2 - BIQ\n"
                           "3 - CPI\n"
                           "4 - DEVIATION\n"
                           "-------> ").upper().strip()
        # --------------------------
        # ALLOWS INPUT OF "1" or "AQE" to result to "AQE"
        # --------------------------
        delete_map = { "1": "AQE", "AQE": "AQE",
                     "2": "BIQ", "BIQ": "BIQ",
                     "3": "CPI", "CPI": "CPI",
                     "4": "DEV", "DEVIATION": "DEV", }
        
        if issue_type in delete_map:
            delete = delete_map[issue_type]
            
            # --------------------------
            # CHECKS IF DELETE TYPE LIST IS EMPTY OR DOESN'T EXIST
            # --------------------------
            if len(issues[delete]) == 0:
                print("No issues recorded to delete.")
                return
            else:
                # --------------------------
                # DELETE SINGLE ENTRY CODE
                # --------------------------
                delete_issue(delete_map[issue_type])
                return
        else:
            print("Invalid selection.\n")
            return


    # --------------------------
    # CLEAR ALL DATA
    # --------------------------
    elif action == "6":
        confirmation = int(input("\n ARE YOU SURE YOU WANT TO DELETE ALL EXISTING ISSUE DATA SAVED? "
                             "\n **(THIS INCLUDES AQE, BIQ, CPI, AND DEVIATION ISSUE HISTORY)\n"
                             "\n 1-NO"
                             "\n 2-YES"
                             "\n-------> "))
        # --------------------------
        # CONFIRMATION TO DELETE DATA
        # --------------------------
        if confirmation == "2" or "YES":
            os.remove("issues.json")
            os.remove("counters.json")
            print("Data Deleted")
            return
    else:
        print("Invalid selection.\n")
        return




if __name__ == "__main__":
    run_program()
    input("Press Enter to exit program ")