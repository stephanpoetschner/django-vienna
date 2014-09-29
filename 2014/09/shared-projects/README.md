# Fun with Django shared projects 

    * *speaker:* Roland Angerer
* Django Developer, yelster GmbH 
* *slides*: 


## Notes

    They had to maintain a Django project from a company from Spain. The project was sort of a project where you could generate Django websites from. (Like for a web agency that builds a lot of websites for various customers)

That meta Django project consisted of three main Django Projects. The CMS project, a project named the kernel that included shared code and one project for custom stuff. 

Roland explained how the handled the code and added internationalisation. They had multiple full Django projects and Git submodules. The conclusio they found in the last months is, that they will have to refactor the code base so it is one big Django projects consisting of multiple Django apps.

