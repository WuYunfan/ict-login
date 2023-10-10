# What is this?
This is a simple python script for ICT (http://www.ict.ac.cn) network login.

```
git clone https://github.com/wuyunfan/ict-login
cd ict-login
pip install ./selenium-3.4.3-py2.py3-none-any.whl --user
```

Replace `账号` with your ict login username and `密码` with your password in `login.py`.

# login
Please unset http_proxy and https_proxy before running the scripts.

The phantomjs executable file is provided for CentOS7 system. Other systems should download the corresponding phantomjs file.

After completing the script, 'result.png' is generated to show the screenshot of the browser.


```
python login.py
```
# logout
```
python logout.py
```
