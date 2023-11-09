from ctreport_selenium.ctreport_html import dashboard_view, detail_view, footer_view
from ctreport_selenium.ctreport_html.charts import status, priority, assertion, verification, timeline
from ctreport_selenium.ctreport_html.scripts import filter, search, footer, tooltip, toggle, detailmodal, imagemodal, \
    toastr
from ctreport_selenium.utility_classes import Severity, Status
import math


def head(tests, title):
    t = '''
        <title>{}</title>
    '''.format(title)
    content = '''
    <html>
    <head>
        ''' + t + '''
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<link rel="stylesheet" type="text/css" href="https://cdn.statically.io/gh/naveens33/ctreport-selenium/0d9f6e27/ctreport_selenium/ctreport_html/style.css" />
		<link rel="stylesheet" type="text/css" href="https://cdn.statically.io/gh/naveens33/ctreport-selenium/5bbcc32f/ctreport_html/font/MoonIcon.css" />
		<link rel = 'stylesheet' href = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css'>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel='stylesheet' href='https://use.fontawesome.com/releases/v5.7.0/css/all.css' integrity='sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ' crossorigin='anonymous'>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
		<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>
		<link href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css" rel="stylesheet">
		<!--<link rel = "icon" href =  "https://cdn.statically.io/gh/naveens33/ctreport-selenium/5bbcc32f/ctreport_html/resource/logo.png" type = "image/x-icon">--> 
		<script type = 'text/javascript'>
		    ''' + \
              status.chart(overall_test_status(tests)) + '''
            window.onload = function() {
                ''' + \
              timeline.chart(tests) + '''
                    ''' + \
              priority.chart(tests) + '''
                    ''' + \
              assertion.chart(assert_verify_count(tests, "assert")) + '''
                    ''' + \
              verification.chart(assert_verify_count(tests, "verify")) + \
              '''
            };
        </script>
		''' + toggle.content + '''
		''' + filter.content + '''
		''' + footer.content + '''
        ''' + search.content + '''
        ''' + tooltip.content + '''
        ''' + detailmodal.content(modal_details(tests)) + '''
        ''' + imagemodal.content + '''
        ''' + toastr.content + '''
		<style>
		span.extrasmall{
			font-size: 10px;
			}
		.table_show {
			display: table-row;
		}     
		.custom_show {
			display: block;
		}       
		.hide{
			display: none;
		}       
        </style>
    '''
    return content


def body(test_details, report_options, tests, status):
    logo_tag = '''
            <a class="navbar-brand disabled">
    						<img  class="img-fluid" src="{}" style="height: 25px;">
    					</a>
            '''.format(report_options["logo"])
    if report_options["logo"] == "":
        logo_tag = ''''''

    footer_tag = footer_view.content()
    if not report_options["show_reference"]:
        footer_tag = ''''''
    content = '''
    <body class="ash">
        <!--<button onclick='topFunction()' id='myBtn' title='Go to top'>Top</button>-->
        <!-- NAVBAR -->
        <nav class="navbar navbar-expand-lg navbar-light bg-white" style="padding:0px">
            <div class="container-fluid">
				<!-- logo -->
				<div class="Logo-Search" style="padding: 6px 0;">
					''' + logo_tag + '''
                    <div style="margin-right: auto;">
						<div class="badge badge-light" style="font-size: large; padding:8px; margin-top:5px;">
							<span >''' + test_details["test_execution_name"] + '''</span>
						</div>
					</div>
					<!-- Search & Client logo -->
					<div class="right-logos"> 
					   <div class="search-client" >
							<div id="graph" onclick="display_other_page()" class="cursor-pointer" style="display: none; padding-right:20px; margin-top:6px;" data-toggle="tooltip" data-placement="bottom" title="Click to toggle dashboard">
								<i class="fa fa-bar-chart" style="font-size:30px; color:#808080;"></i>
							</div>
							<div id="testdetails" class="cursor-pointer" style="padding-right:20px; margin-top:6px;" onclick="display_other_page()" data-toggle="tooltip" data-placement="bottom" title="Click to toggle test details">
								<i class="fas fa-tasks" style="font-size:30px; color:#808080;"></i>
							</div>
							<a class="navbar-brand disabled">
								
							</a>					
						</div>
					</div>
               </div> 
              </div>
        </nav>
		''' + dashboard_view.content(test_details, status, total_pass_asserts, total_pass_verify, total_fail_asserts,
                                     total_fail_verify) + '''
		''' + detail_view.content(status, tests, report_options["show_reference"]) + '''
	    <div id="myModal"></div>
	    <div id="imagemodal"></div>
	    ''' + footer_tag + '''
	</body>
	</html>
    '''
    return content


def assert_verify_count(tests, type):
    a_pass_ = 0
    a_fail_ = 0
    v_pass_ = [0, 0, 0]
    v_fail_ = [0, 0, 0]
    for test in tests:
        for log in test._logs:
            if log["type"] == "assert" and log["status"] == Status.PASS:
                a_pass_ += 1
            elif log["type"] == "assert" and log["status"] == Status.FAIL:
                a_fail_ += 1
            elif log["type"] == "verify" and log["status"] == Status.PASS:
                if log["severity"] == Severity.BLOCKER:
                    v_pass_[0] += 1
                elif log["severity"] == Severity.CRITICAL:
                    v_pass_[1] += 1
                else:
                    v_pass_[2] += 1
            elif log["type"] == "verify" and log["status"] == Status.FAIL:
                if log["severity"] == Severity.BLOCKER:
                    v_fail_[0] += 1
                elif log["severity"] == Severity.CRITICAL:
                    v_fail_[1] += 1
                else:
                    v_fail_[2] += 1
    global total_pass_asserts
    total_pass_asserts = a_pass_
    global total_fail_asserts
    total_fail_asserts = a_fail_
    global total_pass_verify
    total_pass_verify = sum(v_pass_)
    global total_fail_verify
    total_fail_verify = sum(v_fail_)
    if type == "assert":
        return (a_pass_, a_fail_)
    else:
        return (v_pass_, v_fail_)


def overall_test_status(tests):
    pass_ = 0
    fail_ = 0
    skip_ = 0
    broken_ = 0
    for test in tests:
        if test._result == Status.PASS:
            pass_ += 1
        elif test._result == Status.FAIL:
            fail_ += 1
        elif test._result == Status.SKIP:
            skip_ += 1
        else:
            broken_ += 1
    total_test = pass_ + fail_ + skip_ + broken_
    pass_percentage = math.floor((pass_ / total_test if total_test else 0) * 100)
    return (pass_, fail_, skip_, broken_, total_test, pass_percentage)


def modal_details(tests):
    v_a = {}
    for test in tests:
        for log in test._logs:
            if log["type"] == "verify" or log["type"] == "assert":
                if log["data-type"] == "list" or log["data-type"] == "tuple":
                    v_a[log["id"]] = log["merge"]
                elif log["data-type"] == "dict":
                    v_a[log["id"]] = log["merge"]
    return "var tests = " + str(v_a)


def generate(report_options, test_details, tests, report_directory_path, filename):
    head_part = head(tests, report_options["title"])
    body_part = body(test_details, report_options, tests, overall_test_status(tests))
    f = open(report_directory_path + filename + "_Report.html", 'w',encoding="utf-8")
    f.write(head_part + body_part)
    f.close()
    import os
    os.makedirs(report_directory_path.split("reports")[0] + "reports/dailyreport/",exist_ok=True)
    f1 = open(os.path.abspath(report_directory_path.split("reports")[0] + "reports/dailyreport")+"\\"+ filename + "_Report.html", 'w',
              encoding="utf-8")
    f1.write(head_part + body_part)
    f1.close()
