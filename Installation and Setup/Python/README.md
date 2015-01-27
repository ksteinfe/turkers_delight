# Installing Python and Requied Modules
The instructions shown here will guide you through the installation of Python and all the required modules that we'll be using for this class.

## Python
1. [Download](https://www.python.org/download/releases/2.7.8/) and install python 2.7.8 
 * By default, Python should install to **C:\Python27**, which we will refer to below as your "Python Installation Directory". If you choose to install to a different location, please adjust the following instructions accordingly. 
2. Set the system paths, which will let our computer know where to find the Python executeable file so that we may easily run Python from the command line.
  * Open the Environment Variables Dialog
    * Right-Click on "My Computer" or "This PC" and select **Properties**
    * The following dialog will appear. Click on "Advanced System Settings" as shown below.
    * ![system_settings](https://github.com/ksteinfe/turkers_delight/blob/master/Installation%20and%20Setup/Python/img/system_settings.png)
    * Now we'll see the Advanced System Properties dialog. Click on "Environment Variables" as shown below.
    * ![system_properties](https://github.com/ksteinfe/turkers_delight/blob/master/Installation%20and%20Setup/Python/img/system_properties.png)
    * Finally, we've arrived at the Environment Variables dialog shown below. This dialog show us a number of variables, typically paths or locations of important files or folders, used by various pieces of software on your computer. Mucking around in here could break software that you already have installed that rely on these variables, so **be careful** and don't delete anything that is already here! There are two types of variables shown, System Variables and User Variables. We should only mess with the latter, user variables. Each variable may contain multiple paths separated by semicolons. Notice the variable on my computer named PYTHONPATH, shown below, includes "C:\Windows" followed by a semicolon, follwed by "C:\Windows\System32\...". That's two paths associated with the variable PYTHONPATH. To edit an existing variable, select it and then click "Edit" (marked below in red). To create a new variable, just click "New..." (marked below in blue).
    * ![environment_variables](https://github.com/ksteinfe/turkers_delight/blob/master/Installation%20and%20Setup/Python/img/environment_variables.png)
    * After clicking "Edit" or "New", the Edit System Variable dialog will appear (as seen below). Variable strings can be quite long and the available space to edit in the dialog box is limited, so I sometimes copy-paste the entire value into Notepad or something simliar to do my edits, such that I don't miss a semicolon. As you edit, be sure to separate all paths (both new and exsisting) with semicolons.
    *![edit_user_variable](https://github.com/ksteinfe/turkers_delight/blob/master/Installation%20and%20Setup/Python/img/edit_user_variable.png)
  * User variables under PATH should include:**C:\Python27;C:\Python27\Scripts;C:\Python27\Tools\Scripts;**
  * and under PYTHONPATH:**C:\Python27;C:\Python27\Scripts;**

## Module Installers
1. [Download](https://pypi.python.org/pypi/setuptools) and run ez_setup, the documentation for which may be found [here](https://pythonhosted.org/setuptools/easy_install.html)
2. easy_install pip (python installs python)
 
## Dependencies
1. easy_install selenium (project site http://docs.seleniumhq.org/projects/webdriver/)
2. easy_install pillow (project site https://pillow.readthedocs.org/ source on git )
3. easy_install beautifulsoup4 (project site http://www.crummy.com/software/BeautifulSoup/)
4. easy_install lxml (additional parser for beautiful soup)
5. easy_install html5parser (additional parser for beautiful soup)
