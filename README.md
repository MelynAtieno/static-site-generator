## Static Site Generator

This is a static site generator that uses markdown files to produce a static site.

It was built using:
<ul>
<li>HTML</li>
<li>CSS</li>
<li>Python</li>
</ul>

## Getting Started

clone this repository on your local machine, using the command line interface:

`git@github.com:MelynAtieno/static-site-generator.git`

Navigate to the project directory:

`cd static-site-generator`

To open the project on Visual Studio, run:

`code .`

To view the static site, run:

`explorer.exe index.html`

You are now able to view the static site on the browser.

## How to use the static-site generator.

Ensure python is installed on your local machine.

Create a `.venv` folder by running:

`python -m venv .venv`

Activate the virtual environment by running:

`source .venv/bin/activate`

Create a new markdown file containing the content of your website. On the terminal you can use the command:

`touch <filename>.md`

To render the content in the markdown file you created, add the name of the markdown file in the template file. In this case, the template file is; `layout.html`.
The filename should be added in the following format:

`{{ <filename> }}`

The content will be automatically updated in the `index.html` file, which is the output file. The output file is read using the code:

```
with open('index.html', 'w') as output_file:
    output_file.write(
        template.render(
            <filename>=<filename>
        )
    )
    
 ```
This code should be in the `script.py` file

To open up the markdown file and read its content, add the following code: 

```
with open("<filename>") as markdown_file:
    <filename> = markdown(
        markdown_file.read())

```
In the terminal, type `explorer.exe index.html` and press `enter` to view the website on the browser.

To deactivate the virtual environment, type `deactivate` on the terminal and press `enter`.

## AUTHOR
[Melyn Atieno](https://github.com/MelynAtieno)



## MIT LICENSE
Copyright (c) [2023] [static-site-generator]

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
