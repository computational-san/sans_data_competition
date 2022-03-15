![alt text](https://github.com/computational-san/sans_data_competition/blob/main/images/logo/CSAN_Logo_Square_transparent.png)


# CompSAN 2022 SANS Data Competition

This [jupyter-book](https://jupyterbook.org/) was developed for the CompSAN Data Competition for the 2022 [Social and Affective Neuroscience](https://socialaffectiveneuro.org/) annual meeting. 


# Getting Started

This project is hosted on [github](https://github.com/computational-san/sans_data_competition). If you have any questions, comments, or suggestions, please open an issue.

If you notice any mistakes or have idea for new content, please either open an issue or submit a pull request for us to review.

The website is built using [jupyter book](https://jupyter.org/), which creates a sphinx website from markdown and jupyter notebooks. Please read their materials to learn more about this neat resource.

# Updating Book

To update the book, you will need to build it locally using [jupyter-book build](https://jupyterbook.org/start/build.html) and then push it to github. We are syncing the code to master and the deployed website to the gh-pages branch. I recommend using [ghp-import](https://github.com/c-w/ghp-import) to make this easier. We are using the new version of jupyter-book, so make sure this package is up to date. You will also need to install `ghp-import`. I think we can probably set this up to autobuild on travis or circelci at some point if anyone wants to help with that.

1. **Install packages**

`pip install jupyter-book ghp-import`

2. **Build website locally**. The new version of jupyter-book will run the notebooks to generate the figures by default. I find it helpful to keep 1-2 subjects in `~/Github/dartbrains/data/localizer`, which is in .gitignore so it will not get pushed to github.

`jupyter-book build sans_data_competition`

3. **Push updated book to github**. This will sync the updated book to gh-pages branch of our github repository. Don't forget to submit a pull request or push the code to the master repository as well.

`ghp-import -n -p -f _build/html`


# License for this book

All content in this book is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0) license.

# Acknowledgments

This jupyterbook was created by Luke Chang, Mark Thornton, and James Thompson and supported by an NSF CAREER Award 1848370 and the Dartmouth Center for Interacting Minds.
