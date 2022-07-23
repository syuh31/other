## overview

output csv file from json with js command.

json file
```
❯ cat jsonfile.json
{
    "Parameters": [
        {
            "Name": "AppDebug",
            "Type": "String",
            "Value": "true",
            "Version": 1,
            "LastModifiedDate": "2020-11-24T07:29:14.417000+00:00",
            "ARN": "arn:aws:ssm:ap-northeast-1:144675461972:parameter/AppDebug",
            "DataType": "text"
        },
        {
            "Name": "BatchAvailable",
            "Type": "String",
            "Value": "true",
            "Version": 1,
            "LastModifiedDate": "2022-05-27T17:58:38.452000+00:00",
            "ARN": "arn:aws:ssm:ap-northeast-1:144675461972:parameter/BatchAvailable",
            "DataType": "text"
        }
    ]
}
```

execute following command
```
cat jsonfile.json | jq -r '.[][] | [.Name, .Value] | @csv'
```
output
```
"AppDebug","true"
"BatchAvailable","true"
```

## memo
```
cat jsonfile.json | jq -r '.[][] | [.Name, .Value] | @csv'


cat jsonfile.json | jq -r '.[]'
cat jsonfile.json | jq -r '.[][].Name'
cat jsonfile.json | jq -r '.[][] | [.Name, .Value]'
cat jsonfile.json | jq -r '.[][] | [.Name, .Value] | @csv'
cat jsonfile.json | jq -r '["name","value"], (.[][] | [.Name, .Value]) | @csv'
cat jsonfile.json | jq -r '(.[][0])'
cat jsonfile.json | jq -r '(.[][0]|to_entries|map(.key))'
```