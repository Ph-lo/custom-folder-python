# custom-folder
Create custom MacOS folder images.

## Table of Contents

-  [Installation](#installation)
-  [Usage](#usage)

## Installation

To install the required dependencies of the script, navigate to the root directory of the project and run the following command:
```bash
pip install -r requirements.txt
```

## Usage
Here is a list of script commands:
image_path: The path to the png image.<br />
`-o/--output`: Optional output path (default is image_path).<br />
`-f/--fill`: Optional color fill parameter. If false, the folder color will only be applied as "highlight".<br />
`-p/--padding`: Optional image padding parameter (default is 45).<br /><br />

#### You can run the python script with parameters like this:
```bash
python custom-folder.py [image_path] [-o output_path] [-f] [-p padding]
```
#### Example:
```bash
python custom-folder.py ~/myimage.png -o ~/custom_folders -f -p 50
```

