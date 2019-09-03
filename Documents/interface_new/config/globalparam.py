# -*- coding: utf-8 -*-
import os
from config.readconfig import ReadConfig

#管理路径
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path, 'config.ini'))
# Project parameter setting
prj_path = read_config.getValue('projectConfig', 'project_path')
app_path = read_config.getValue('projectConfig', 'app_path')
appserver_path = read_config.getValue('projectConfig', 'appserver_path')
cms_path = read_config.getValue('projectConfig', 'cms_path')
# Log path
log_path = os.path.join(prj_path, 'report', 'log')
# Screenshot file path
img_path = os.path.join(prj_path, 'report', 'image')
#Test report path
report_path = os.path.join(prj_path, 'report', 'test_report')
#yaml path
yaml_path = os.path.join(prj_path, 'config', 'readyaml')
# Test data path
data_path = os.path.join(prj_path, '', 'testdata')
