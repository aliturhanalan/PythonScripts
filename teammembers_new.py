import requests
import json
import argparse

file = open("config.json", "r")
data = json.load(file)
file.close()

USER_ID = data['USER_ID']
API_TOKEN = data['API_TOKEN']
API_ROOT = data['API_ROOT']
AUTH = (USER_ID, API_TOKEN)

def teammembers_new():

    endpoint_url = API_ROOT % "teammembers/new"
    parser = argparse.ArgumentParser(description='Creates a new member.')
    parser.add_argument('-ag', '-autogp', type=str, choices = ['true', 'false'], help='Gets or sets a value indicating whether the Password will be generate automatically by system. If password is created as automatic you havent to enter the Password and ConfirmPassword')
    parser.add_argument('-pw', '-password', type=str, help='Gets or sets the password')
    parser.add_argument('-sn', '-sendnotification', type=str, choices = ['true', 'false'], default='true', help='Gets or sets a value indicating whether the notification will send after user is created')
    parser.add_argument('-pn', '-pnumber', type=str, help='Gets or sets the phone number')
    parser.add_argument('-ap', '-accper', type=str, choices=['AccountAdministrator', 'ManageWebsites'], help='Gets or sets the accounts permissions as comma separated. You can use following permissions : AccountAdministrator, ManageWebsites')
    parser.add_argument('-tid', '-timezoneid', type=str, help='Gets or sets the users time zone. You can check out following endpoint to see all of time zones. Api endpoint : /api/1.0/teams/gettimezones. Default : GMT Standard Time')
    parser.add_argument('-wg', '-wgroups', type=str, help='Gets or sets the groups as comma separated.While creating a member, if he got administrator permissions no need to enter a website group otherwise its required')
    parser.add_argument('-sp', '-scanper', type=str, help='Gets or sets the scans permissions as comma separated.You can use following permissions : StartScans, ViewScanReports, ManageIssues, ManageIssuesAsRestricted')
    parser.add_argument('-dtf', '-dtformat', type=str, choices=['dd/MM/yyyy', 'MM/dd/yyyy'], help='Gets or sets user date format that defines the culturally appropriate format of displaying dates and times. You can use these values ; dd/MM/yyyy and MM/dd/yyyy. Default : dd/MM/yyyy')
    parser.add_argument('-e', '-email', type=str, help='Gets or sets the email')
    parser.add_argument('-n', '-name', type=str, help='Gets or sets the display name of the user')
    parser.add_argument('-cp', '-confirmp', type=str, help='Gets or sets the confirmation password')
    parser.add_argument('-ae', '-apiaccess', type=str, choices = ['true', 'false'], default='true', help='Gets or sets a value indicating whether api access is enabled for user')

    args = parser.parse_args()

    json_object = {
        "AutoGeneratePassword": args.ag,
        "Password": args.pw,
        "SendNotification": args.sn,
        "PhoneNumber": args.pn,
        "AccountPermissions": args.ap,
        "TimezoneId": args.tid,
        "WebsiteGroups": args.wg,
        "ScanPermissions": args.sp,
        "DateTimeFormat": args.dtf,
        "Email": args.e,
        "Name": args.n,
        "ConfirmPassword": args.cp,
        "IsApiAccessEnabled": args.ae
        }
    
    response = requests.post(endpoint_url, json=json_object, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))
    
    if response.status_code != 201:
        print(response.text)

    else:
        print("Team member has been created.")

def main():

    teammembers_new()

if __name__ == '__main__':
    main()