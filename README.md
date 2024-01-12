# Amazon ECS IntelliSense Schema

This package is to provide an intelligent code completion (IntelliSense) experience for users when writing an Amazon ECS task definition in their Visual Studio Code or JetBrains IDEs. It does so by parsing the Amazon ECS model files from the AWS SDK for Go. With these files, the package generates a JSON schema file that provides code completion, documentation lookup, and error checking. Instructions to [build](#how-to-run-this-tool) and [enable IntelliSense](#how-do-i-set-it-up) are down below.

## What does an integration look like?
Here is a VSCode setup integration example:  
![intellisense](https://user-images.githubusercontent.com/879348/66334750-80117900-e8ee-11e9-9000-435c7b0a6604.gif)

## How do I set it up?
### VS Code
1. Configure your IDE settings by going to `Code` → `Preferences` → `Settings`
2. In the search bar, type in settings.json
3. Click on _Edit in settings.json_
4. Check to see if `json.schemas` is already added
   1. If you see `json.schemas`, then just append this code to the `json.schemas` array
      ```json
      {
        "fileMatch": [
          "*ecs-task-def.json"
        ],
        "url": "https://ecs-intellisense.s3-us-west-2.amazonaws.com/task-definition/schema.json"
      }
      ```
    2. Otherwise, create it:
        ```json
        "json.schemas": [{
          "fileMatch": [
            "*ecs-task-def.json"
          ],
          "url": "https://ecs-intellisense.s3-us-west-2.amazonaws.com/task-definition/schema.json"
        }]
        ```

#### Example
![vscode](https://user-images.githubusercontent.com/879348/66334789-90295880-e8ee-11e9-8462-566dfdd61617.png)

### JetBrains
1. Go to `File` → `Preferences` → `Languages & Frameworks` → `Schemas and DTDs` → `JSON Schema Mappings`
2. Select the `+` sign at the top to add new mapping
3. Enter this URL inside `Schema file or URL`: https://ecs-intellisense.s3-us-west-2.amazonaws.com/task-definition/schema.json
4. Select `JSON schema version 7` for `Schema version`  
![jetbrains-1](https://user-images.githubusercontent.com/879348/66334825-9ddede00-e8ee-11e9-9bd3-2e1aaa73cd63.png)
5. Add file matching by selecting the `+` button at the bottom  
![jetbrains-2](https://user-images.githubusercontent.com/879348/66334849-adf6bd80-e8ee-11e9-9ec8-f1376b00179e.png)
6. Select `Add File Path Pattern`
7. For file path pattern type in `*ecs-task-def.json`  
![jetbrains-3](https://user-images.githubusercontent.com/879348/66334877-ba7b1600-e8ee-11e9-8c74-7a77171b8fa4.png)

## How to run this tool?
1. Install dependencies with `pip install -r requirements.txt`
2. To update `api.json` and `docs.json` for a specific Go SDK version Run `./update.sh SCHEMA_VERSION GO_SDK_VERSION`
3. Update the `schema_version` and `sdk_go_version` values in `src/version.py` file accordingly.
4. Run `python3 src/main.py`  
   NOTE: If you run into `ModuleNotFoundError: No module named 'src'`. Then, run `export PYTHONPATH="${PYTHONPATH}:/path/to/src/"`
5. The schema should be generated under `./src/model/schema/`

## License

This library is licensed under the Apache 2.0 License. 
