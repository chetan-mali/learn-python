import subprocess
import pandas

def main():
    file = "user_sheet.csv"

    # Connect to PowerBI
    cmd = "Connect-PowerBIServiceAccount"
    response = subprocess.run(["powershell","-Command",cmd])
    
    if response.returncode != 0:
        print("An error occred: %s",response.stderr)
    else:
        print("Connected")
        try:
            user_data_full = pandas.read_csv(filepath=file)
            user_data = user_data_full[user_data_full['Action_performed' == False]]
        except Exception as e:
            print(f"Unable to read csv [error :{e}]")
            return
        
        for user in user_data.iterrows():
            action = user[1].action
            if action.lower() == "remove":
                scope = user[1].Scope
                workspace_id = user[1].Workspace_ID
                email = user[1].Email

                base_cmd = f"Remove-PowerBIWorkspaceUser -Scope {scope} -Id {workspace_id} -UserEmailAddress {email}"
                response = subprocess.run(["powershell","-Command",base_cmd])
                if response.returncode != 0:
                    print("An error occred: %s",response.stderr)
                else:
                    print("Action performed")
                    user_data_full.loc[user[0],"Action_performed"] == "TRUE"
            else:
                scope = user[1].Scope
                workspace_id = user[1].Workspace_ID
                email = user[1].Email
                accessright = user[1].AccessRight

                base_cmd = f"Add-PowerBIWorkspaceUser -Scope {scope} -Id {workspace_id} -UserEmailAddress {email} -AccessRight {accessright}"
                response = subprocess.run(["powershell","-Command",base_cmd])
                if response.returncode != 0:
                    print("An error occred: %s",response.stderr)
                else:
                    print("Action performed")
                    user_data_full.loc[user[0],"Action_performed"] == "TRUE"
        user_data_full.to_csv(file,index=False)
    return
        
if __name__ == "__main__":
    response = main()