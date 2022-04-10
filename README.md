# ![WebApp](images/webapp1.jpeg)
# Amaze Job Search Web App
<table>
<tr>
<td>
    Amaze Job Search Web App is tailored for graduating IT students. The web app uses REST based APIs for smart job search. A smart recommender system is implemented which picks up required details from resumes like skills, personal info, hobbies and in return recommends the most suitable jobs according to current job openings. A sleek web interface has been implemented to ease the laborious process of job hunting.  
</td>
</tr>
</table>


## Demo
Here is a working live demo :  [link to youtube video]


## Site
Few snapshots of individual pages with their descriptions.

### Landing Page
![](images/webapp1.jpeg)

### Job Display 
![](images/webapp2.jpeg)

### Login Pages
![](images/webapp3.jpeg)
![](images/webapp4.jpeg)
![](images/webapp5.jpeg)

## Setup and Launch
The application uses a mono-repo with multiple packages. To install and initialize all the packages on a local development environment, including running a docker image for the DB and seeding the DB, execute the following commands in the project root folder:


```jsx
make env-setup
make local # To run on local
make cloud # TO run on cloud
```

## Architecture
![System Architecture](images/Architecture.png)

## Mobile support
The Web App is compatible with devices of all sizes and all OSs, and consistent improvements will be made.



### Development
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 

### Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/vishalsmak/amazeballs-job-search/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/vishalsmak/amazeballs-job-search/issues). Please include sample queries and their corresponding results.


## Built with 
-  Python, Flask, Docker, HTML, CSS



## To-do
- Integrate learning 


## Team

[Namrata](https://github.com/NamrataKankaria) | [Vishal](https://github.com/vishalsmak)
---|---
[Kriti](https://github.com/KritiJaggi) | [Maanav](https://github.com/maanavb)

## [License](link)

MIT © 

