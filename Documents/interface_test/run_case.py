# -*- coding: utf-8 -*-
"""执行用例并生成报告"""
import time, os
import unittest
import shutil
from Branch import HTMLTestReportCN, send_ding
from config import globalparam
from config.readyaml import Getyaml

test_dir = "./testcase"
discover = unittest.defaultTestLoader.discover(test_dir, pattern="case_shop*.py")

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    filename = globalparam.report_path + "\\" + "result.html"
    fp = open(filename, 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title=u'接口自动化测试报告',
        # description='详细测试用例结果',    #不传默认为空
        tester=u"QA"  # 测试人员名字，不传默认为QA
    )
    results = runner.run(discover)
    cases = "总用例数：{0}".format(results.testsRun)
    case_fail = "失败用例数：{0}".format(len(results.failures) + len(results.errors))
    case_results = []
    if len(results.failures) == 0 and len(results.errors) == 0:
        case_results.append("无")
    else:
        for case, reason in results.failures + results.errors:
            case_title = Getyaml().get_datas(str(case))
            case_results.append(case_title)
    send_ding.Send_dingding(cases, case_fail, case_results)
    fp.close()
    shutil.copy(globalparam.report_path + "\\" + "result.html", globalparam.report_path + "\\" + now + "result.html")

