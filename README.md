# ToGo-s
A simple WebApp I made to help with the ToGo shift at work in the Deli at PCC Fremont
Built with Python and Pyramid (pip installable)

## Updating
To update the site with new black bottom combos, you will need a copy of the Chef Tech HTML page you get when you filter only "to go" options

modify scrape.py to target the HTML file, and it will format the information in a way for the site to read

Careful, there are a lot of mismatches in the database because they haven't hired me onto IT to fix it yet (nerds) so you will need to fix them manually.

These mismatches include: 

Cauliflower Tahini/ Tahini Cauliflower

The Works Mashed Potato/ The Works Mashed Potatoes/ The Works Potatoes

Sesame Edamame Quinoa/ Sesame Edamame Quinoa Salad

Kelp Noodles/ Kelp Noodle Salad

...things like that. Try to double check before publishing

## Running 
simply run togo.py and go to http://0.0.0.0:8000/
