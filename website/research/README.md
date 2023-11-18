# Research Projects
This module contains all of the content for the research projects pages.

## Research Module Structure
```
├── research                            # Module directory
│   ├── templates                       # Templates for content and pages
│   │   ├── abstracts                   # Components for abstracts
│   │   │   └── <abstract-name.j2>
│   │   ├── markdown                    # Create/update project content here
│   │   │   ├── TEMPLATE.md             # Template file for research projects
│   │   │   ├── <abstract-name.md>
│   │   │   └── <project-name.md>
│   │   ├── projects                    # Components for projects
│   │   │   └── <project-name.j2>
│   │   ├── <top-level-research-pages>  # Pages can include components
│   │   └── md_to_j2.py                 # Converts markdown to jinja2
│   ├── __init__.py                      
│   ├── README.md                       # Module documentation
│   └── research.py                     # Module blueprint
```

## Current Pages
To view the current pages, start the development server from the root directory of the project.
```bash
# From the root directory of the project
pwd
# file-path-to/jessicadesilva.github.io
python app.py
```
Then follow the links below to view the pages.
* Current Undergraduate Projects - [research/undergrad/current.html](localhost:5000/research/undergrad/current.html)
  * Current Undergraduate Abstracts - [research/undergrad/current/abstracts.html](localhost:5000/research/undergrad/current/abstracts.html)
* Former Undergraduate Projects - [research/undergrad/former.html](localhost:5000/research/undergrad/former.html)
* Electric Vehicle Charging Poster - [research/projects/ev_charging_poster.html](localhost:5000/research/projects/ev_charging_poster.html)
* Walking Time Poster - [research/projects/walking_time_poster.html](localhost:5000/research/projects/walking_time_poster.html)
* Other Projects - [research/other.html](localhost:5000/research/other.html)

## Adding a New Project or Abstract
1. Copy the `TEMPLATE.md` file in the `research/templates/markdown` directory.
    ```bash
    # From the research directory
    cp templates/markdown/TEMPLATE.md templates/markdown/<project_name>.md
    ```
    Alternatively, open the `TEMPLATE.md` file in the `templates/markdown` directory and copy the contents and past them into a new file in the `templates/markdown` directory.
    * Be sure to rename the file to the name of the project.
       (i.e. file -> save as -> `<project_name>.md`)
    * To create an abstract, prefix the project name with `abstract_`.
       (i.e. file -> save as -> `abstract_<project_name>.md`)

2. Fill in the template with the project information.
   * `Image`
   * `Title`
   * `Advisor` - optional
   * `Student`
   * `Major` - optional
   * `Description`
   * `Button` - optional

3. Convert the markdown file to a jinja2 file.
    > **Note**: see [current pages](#current-pages) for instructions on how to check the current directory.
    * If you are currently in the `research` directory, navigate to the project root.
    ```bash
    # From the research directory
    cd ../..
    ```
    * Run the `md_to_j2.sh` script.
    ```bash
    # From the project root directory
    ./md_to_j2.sh
    ```
    
    This will convert all markdown files in the `research/templates/markdown` directory to jinja2 files. Files prefixed with `abstract_` will be in the in the `research/templates/abstracts` directory, otherwise they will be in the `research/templates/projects` directory.

4. Add the project to the `research.py` file.
    > **Note**: the `projects` directory is used for both current and former projects. Be sure to add the project to the correct list.
    ### Current Undergraduate Projects  
    ```python
    # From the research.py file

    # Add current undergraduate projects here
    # NOTE: the project must be located in the `projects` directory
    # NOTE: the project name must match the name of the jinja2 file
    #       and should exclude the file extension
    #       (i.e. <project_name>.j2)
    # NOTE: projects are displayed in the order they they are listed
    current_ugrad_project_names = [
        "<project_name>",
        ...
    ]
    ```
    ### Former Undergraduate Project
    ```python
    # From the research.py file

    # Add former undergraduate projects here
    # NOTE: the project must be located in the `projects` directory
    # NOTE: the project name must match the name of the jinja2 file
    #       and should exclude the file extension
    #       (i.e. <project_name>.j2)
    # NOTE: projects are displayed in the order they they are listed
    fromer_ugrad_project_names = [
        "<project_name>",
        ...
    ]
    ```
    ### Current Undergraduate Project Abstracts
    ```python
    # From the research.py file

    # Add current undergraduate abstracts here
    # NOTE: the project must be located in the `abstracts` directory
    # NOTE: the project name must match the name of the jinja2 file
    #       and should exclude the file extension
    #       (i.e. abstract_<project_name>.j2)
    # NOTE: projects are displayed in the order they they are listed
    current_ugrad_abstract_names = [
        "abstract_<project_name>",
        ...
    ]
    ```
    ### Other Projects
    This section is not currently supported.

5. Visit the relevant page to view your changes!
   > **Note**: See [current pages](#current-pages) for instructions on how to check the current pages.
