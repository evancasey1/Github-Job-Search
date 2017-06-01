# Github-Job-Search

## Summary
Job search on a keyword for jobs near the San Francisco area.

## Usage/Setup
1. Download/Clone repository into working directory.
2. Set up virtual environment
    1. `pip install virtualenv`
    2. `virtualenv <environment>`
    3. `source <environment>/bin/activate`
3. Install Django and necessary modules.
    1. `pip install django`
    2. `pip install requests`
4. Run python server
    1. Navigate to subdirectory containing manage.py
    2. `python manage.py runserver`
5. In a browser, go to <http://127.0.0.1:8000/app/>

## Technologies Used
* GitHub Jobs API
* Django 1.11.2
* Bootstrap
* Bower

## Languages Used
* Python
* HTML
* CSS

## Time Spent
|Phase         |Hours Spent|
|--------------|:----------|
|Planning      |1          |
|Study         |2          |
|Implementation|5          |
|Write-Up      |1          |
|**TOTAL**     |**9**      |

## Code Organization Summary
The code structure and organization is simple. At a high level, the code is separated into the parent `githubsearch` and the sub-application, `gitsearchapp`.
<br>
`githubsearch` contains the base URL patterns and the main Django settings and directs any URL with the pattern `baseurl/app` to `gitsearchapp`.
<br>
`gitsearchapp` is the "main" application. It queries the GitHub API on jobs that match a user-input keyword and are near San Francisco, CA. `gitsearchapp` is a barebones prototype Django application that revolves mainly around `urls.py`, `views.py` and the templates associated with each view. `models.py`, `tests.py`, and `admin.py` were not utilized for this application. There are two views, one for the top level index, and another that the user is taken to on click for the detailed information on a job.

## Next Steps
The immediate next steps to take in order to take this application from a first phase prototype to a fully-fledged application would be to make the UI more user friendly, expand feature list (allowing users to increase the scope of their search past San Francisco, CA would be trivial, simply involving an extra search box and passing the search term into an API request. This would make it so that the `keyword` search box and/or the `location` search box needs to be used, instead of only the `keyword` box).
<br>
#### UI Changes would include <br>
* Fixing logo image size and providing a default image to companies who do not have a logo
* Displaying the top level index view as a 2 column view
* Removing the large amount of white/unused space
* Instead of having the detail view be in a separate URL, use JavaScript/CSS to create a drop-down box of sorts with the necessary information inside. This way only one view is needed for both the top-level index and the detail view.
* Make detail view more aesthetically pleasing/allow for rich text to be used in the job description instead of plaintext.


