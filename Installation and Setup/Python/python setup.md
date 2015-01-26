Python Installation Requirements

1. Install python 2.7.8 
2. Download and run ez_setup.py  (from https://pypi.python.org/pypi/setuptools) (documentation https://pythonhosted.org/setuptools/easy_install.html)
3. Make sure to set the system paths. System Properties >> Advanced >> Environment Variables
Don't delete anything.  
User variables under PATH should include:
%APPDATA%\Python\Scripts;.;C:\Python\Scripts;
and under PYPATH:
;C:\Python27;C:\Python27\Scripts
System variables under PATH should include:
C:\Python27;C:\Python27\Scripts;C:\Python27\Tools\Scripts;
4. easy_install pip (python installs python)
5. easy_install selenium (project site http://docs.seleniumhq.org/projects/webdriver/)
6. easy _install pillow (project site https://pillow.readthedocs.org/ source on git )
7. easy_install beautifulsoup4 (project site http://www.crummy.com/software/BeautifulSoup/)
8. easy_install lxml (additional parser for beautiful soup)
9. easy_install html5parser (additional parser for beautiful soup)


