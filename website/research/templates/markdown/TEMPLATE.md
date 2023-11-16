<!--
    HOW TO USE THIS TEMPLATE
     
    1. Make a copy of this file in the `markdown` directory.
    
        Or copy the text below and paste it into a new file in the `markdown` directory.
    
    2. Rename the copied file to the name of the project.
        NOTE: This can be a shortened name.
        (i.e. Mathematical Measures of Fairness in Legislative Districting -> `mathematical_fairness_districting.md`)
    
    3. Fill in the information below.
        NOTE: to exclude a section simply delete the section (including the header)
        Or keep the header and leave the content blank.
        (i.e. if there is no advisor, delete the entire "Advisor" section)

        * IMAGE
            * Add the image to the `website/static/images` directory.
            * Replace the `...` in the `src` attribute with the name of the image.
            * Replace the `...` in the `alt` attribute with a description of the image.
        
        * TITLE
            * Replace the `...` with the full name of the project.
        
        * ADVISOR
            * Replace the `...` with the name of the advisor(s).
            * To create a link to the advisor's website, wrap the name in square brackets [] and follow it with the URL in parentheses (). 
            * [alt text](url)
            * i.e. [Dr. David Offner](https://davidoffner.wordpress.com/)
        
        * STUDENT
            * Replace the `...` with the name of the student(s).
            * To create a link to the student's website, follow the same instructions as the advisor.

        * MAJOR
            * Replace the `...` with the major(s) of the student(s).

        * DESCRIPTION
            * Replace the `...` with the description/abstract of the project.
            * See the advisor section for an example of how to create a link.

        * BUTTON
            * Replace the `...` in the `href` attribute with the URL of the page you want to link to.
            * Replace the `...` in the text between the opening and closing `<a>` tags with the text you want to display on the button.
            * i.e. <a href="https://www.csustan.edu" class="button">Stan State</a>
            * i.e. <a href="{{ url_for('research.current_undergrad_projects') }}" class="button">Current Undergrad Projects</a> 

Everything above this line will be ignored when converted to a jinja2 file. -->
## Image

<!-- The image should be added to the `website/static/images` directory.
    Replace the `...` in the `src` attribute with the name of the image.
    Replace the `...` in the `alt` attribute with a description of the image.
-->
<img src="{{ url_for('static', filename='images/...') }}" alt="...">

## Title

<!-- Add the full project name here -->
...

## Advisor

<!-- Add project advisor(s) here 
    NOTE: markdown syntax to create a link is [alt text](url)
-->
...

## Student

<!-- Add student(s) here 
    NOTE: markdown syntax to create a link is [alt text](url)
-->
...

## Major

<!-- Add student(s) major(s) here -->
...

## Description

<!-- Add project description/abstract here 
    NOTE: markdown syntax to create a link is [alt text](url)
-->
...

## Button

<!-- Add a button here
    NOTE: url_for('...') is used to link to internal pages.
        See research.py for a list of internal pages.
        A valid route is any function following the `@research_blueprint.route` decorator.
        To access the route, use the name of the module (i.e. research) followed by a period (.) and the name of the function (i.e. current_undergrad_projects).
    
    * external site: <a href="https://www.csustan.edu" class="button">Stan State</a>
    * internal site: <a href="{{ url_for('research.current_undergrad_projects') }}" class="button">Current Undergrad Projects</a>
-->

<a href="..." class="button">...</a>