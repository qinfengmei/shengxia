# interface-test
## 使用说明<br>
1.python安装所需的模块：requests、xlrd、pyyaml、pymysql，下载requirements.txt在cmd下运行pip install -r requirements.txt自动安装<br>
<br>
2.修改config/config.ini的project_path为项目路径如F:\interface-test；environment_path为环境地址<br>
<br>
3.测试用例写在test_data/case_liguo.xlsx，自己可以新建一个case_xx.xlsx写自己的用例数据，写法参照之前用例<br>
<br>
4.当前测试接口依赖cookie的umbrella_token进行请求，如接口请求不成功可能是umbrella_token已失效需修改Public/requests.py的参数<br>
<br>
5.运行run_case.py会执行测试用例并生成测试报告和日志<br>


## 编写步骤<br>
1.使用抓包工具获取接口，并用postman等接口工具进行请求，保证接口能调通<br>
<br>
2.在Excel录入用例数据(用例id、模块名、用例名、请求参数、数据库信息和SQL、请求地址、请求方式、期望值、实际值)<br>
<br>
3.编写用例(testcase目录)，命名规范xxx_case.py，主要考虑怎么样去获取期望值(从Excel中等)和实际值(数据库、接口响应)进行断言校验<br>

## 框架结构<br>
![no view](http://cdn1.showjoy.com/shop/interface/20190412/ALT9FDI329CDGINHL3S21555037334029.jpg)<br>
<br>
1.Branch文件夹：HTMLTestReportCN.py为测试报告模板，log.py日志模块在执行过程中输出日志，operate_db.py操作数据库模块，operate_excel.py用于获取Excel数据；<br>
<br>
2.Public文件夹：expect.py对Excel中的期望值进行处理，requests.py对请求进行二次封装，select_request.py选择请求方式处理；<br>
<br>
3.config文件夹用例管理路径,config.ini为项目的主路径和环境地址,globalparam.py为日志文件、测试用例读取和存储的路径，read_config.py读取config.ini，readyaml.py读取yaml文件；<br>
<br>
4.report文件夹下存放日志和测试报告;<br>
<br>
5.testCase文件夹写了测试用例,用unittest单元测试框架管理用例;<br>
<br>
6.testdata文件下是测试用例数据;<br>
<br>
7.运行run_ddt_case.py执行用例生成报告。<br>

## 脚本构建<br>
1.用例都写好之后代码更新到gitlab上(需个人电脑上安装git)：http://git.showjoy.net/showjoy-autotest/interface_test<br>
<br>
2.自动化构建工具使用Jenkins，可自动构建或手动构建执行，构建时Jenkins从gitlab上拉取最新代码<br>
<br>
3.构建开始/完成钉钉机器人在群里发送消息通知。<br>
<br>
![no view](http://cdn1.showjoy.com/shop/interface/20190412/Z74GL5DAC86P9VXWWXZ91555037428613.jpg)<br>

## 相关资料<br>
Git教程：https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/<br>
<br>
Jenkins教程：https://jenkins.io/zh/doc/tutorials/<br>
