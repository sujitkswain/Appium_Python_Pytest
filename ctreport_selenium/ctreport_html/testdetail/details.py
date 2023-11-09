from ctreport_selenium.ctreport_html.properties import status, priority, severity
from ctreport_selenium.utility_classes import Status, Severity


def screenshot_section(test):
    c = ''''''
    for log in test._logs:
        if log["type"] == "screenshot":
            c += '''<a id="{}"> 
                        <i class="fas fa-image pl-2 pointer" style="font-size:30px; color:#aaa;" onclick="createimagemodal('{}','{}')"></i>
                    </a>
            '''.format(log["id"], log["path"], log["path"])
        elif log["type"] == "error":
            if log["screenshot"] is not None:
                c += '''
                    <a id="{}"> 
                        <i class="fas fa-image pl-2 pointer" style="font-size:30px; color:#cb3434;" onclick="createimagemodal('{}','{}')"></i>
                    </a>
                '''.format(log["id"], log["screenshot"], log["screenshot"])
        elif log["type"] == "verify" or log["type"] == "assert":
            if log["screenshot"] is not None:
                c += '''
                     <a id="{}" > 
                         <i  class="fas fa-image pl-2 pointer" style="font-size:30px; color:#cb3434;" onclick="createimagemodal('{}','{}')"></i>
                     </a>
                 '''.format(log["id"], log["screenshot"], log["screenshot"])
    return c


def table_content(logs):
    c = ''''''
    for log in logs:
        if log["type"] == "log":
            c += '''
                <tr class="border-bottom">
                    <td class="text-sm-center" style="width: 10%;"><i class="{}" style="{}"></i></td>
                    <td style="width: 10%;">Log</td>
                    <td style="width: 70%;">{}</td>
                    <td style="width: 10%;"><span  class="extrasmall">{}</span></td>
                </tr>                
                '''.format(status[Status.PASS][0], status[Status.PASS][1], log["message"], log["start-time"])
        elif log["type"] == "screenshot":
            type_ = '''
                        <a href="#{}" data-toggle="popover" data-trigger="hover" data-content="{}" data-original-title="" title="">Screenshot</a>
                        '''.format(log["id"],log["path"])
            c += '''
                <tr class="border-bottom">
                    <td class="text-sm-center" style="width: 10%;"><i class="{}" style="{}"></i></td>
                    <td style="width: 10%;">
                    {}
                    </td>
                    <td style="width: 70%;">{}
                    </td>
                    <td style="width: 10%;"><span  class="extrasmall">{}</span></td>
                </tr>                
            '''.format(status[Status.PASS][0], status[Status.PASS][1], type_, log["message"],
                       log["start-time"])
        elif log["type"] == "error":
            type_ = '''
            <a href="#{}" data-toggle="popover" data-trigger="hover" data-content="{}" data-original-title="" title="">Error</a>
            '''
            screenshot_path = log["screenshot"]
            err = ''''''
            if log["error"] is not None:
                err= '''
                <span class="extrasmall">{}</span> 
                '''.format(log["error"] )
            if screenshot_path is None:
                type_ = "Error"
            else:
                type_.format(screenshot_path, screenshot_path)
            c += '''
                <tr class="border-bottom">
                    <td class="text-sm-center" style="width: 10%;"><i class="{}" style="{}"></i></td>
                    <td style="width: 10%;">
                    {}
                    </td>
                    <td style="width: 70%;">{} 
                        <br>
                       {}
                    </td>
                    <td style="width: 10%;"><span  class="extrasmall">{}</span></td>
                </tr>                
            '''.format(status[Status.FAIL][0], status[Status.FAIL][1], type_, log["message"], err,
                       log["start-time"])
        elif log["type"] == "broken":
            c += '''
                <tr class="border-bottom">
                    <td class="text-sm-center" style="width: 10%;"><i class="{}" style="{}"></i></td>
                    <td style="width: 10%;">Broken</td>
                    <td style="width: 70%; color:#F7464A;">{}</td>
                    <td style="width: 10%; "><span  class="extrasmall">{}</span></td>
                </tr>                
                '''.format(status[Status.BROKEN][0], status[Status.BROKEN][1], log["error"][:500], log["start-time"])
        elif log["type"] == "skipped":
            c += '''
                <tr class="border-bottom">
                    <td class="text-sm-center" style="width: 10%;"><i class="{}" style="{}"></i></td>
                    <td style="width: 10%;">Skipped</td>
                    <td style="width: 70%; color:#1E90FF;">{}</td>
                    <td style="width: 10%; "></td>
                </tr>                
                '''.format(status[Status.SKIP][0], status[Status.SKIP][1], log["message"], log["start-time"])
        elif log["type"] == "verify":
            message_ = ''''''
            if log["message"] is not None:
                message_ = '''
                    <span>{}</span>
                    &nbsp;
                    <br/>
                '''.format(log["message"])
            type_ = '''
                        <a href="#{}" data-toggle="popover" data-trigger="hover" data-content="{}" data-original-title="" title="" style="text-decoration:none">{}</a>
                    '''
            screenshot_path = log["screenshot"]
            if screenshot_path is None:
                type_ = "Verification"
            else:
                type_ = type_.format(log["id"], screenshot_path, "Verification")
            if log["data-type"] is not "others":
                e_a_content = '''
                    <td style="width: 70%">
                        '''+message_ + '''
                        <i class="{} pointer" onclick="expandFooter('info')" style="{}"></i>
                        Expected: 
                        &nbsp;
                        <i class="fas fa-ellipsis-h pointer" onclick="createmodal('{}')"></i>
                        &nbsp;
                        Actual: 
                        &nbsp;
                        <i class="fas fa-ellipsis-h pointer" onclick="createmodal('{}')"></i>
                        &nbsp;
                        <br/>
                        '''.format(severity[log["severity"]][0], severity[log["severity"]][1], log["id"], log["id"])+ '''
                    </td>
                '''
            else:
                e_a_content = '''
                           <td style="width: 70%">
                           '''+message_ + '''
                               <i class="{} pointer" onclick="expandFooter('info')" style="{}"></i>
                               Expected: {}    Actual: {}
                               <br>
                                '''.format(severity[log["severity"]][0], severity[log["severity"]][1], log["expected"],
                                           log["actual"])+ '''
                           </td>
                       '''
            c += '''
                    <tr class="border-bottom">
                        <td class="text-sm-center" style="width: 10%"><i class="{}" style="{}"></i></td>
                        <td style="width: 10%">{}</td>
                        {}
                        <td style="width: 10%"><span class="extrasmall">{}</span></td>
                    </tr>             
                   '''.format(status[log["status"]][0], status[log["status"]][1], type_, e_a_content, log["start-time"])
        elif log["type"] == "assert":
            message_ = ''''''
            if log["message"] is not None:
                message_ = '''
                               <span>{}</span>
                               &nbsp;
                                <br/>
                           '''.format(log["message"])
            type_ = '''
                        <a href="#{}" data-toggle="popover" data-trigger="hover" data-content="{}" data-original-title="" title="" style="text-decoration:none">{}</a>
                    '''
            screenshot_path = log["screenshot"]
            if screenshot_path is None:
                type_ = "Assertion"
            else:
                type_ = type_.format(log["id"], screenshot_path, "Assertion")
            if log["data-type"] is not "others":
                e_a_content = '''
                    <td style="width: 70%">
                        '''+message_ + '''
                        <i class="{} pointer" onclick="expandFooter('info')" style="{}"></i>
                        Expected: 
                        &nbsp;
                        <i class="fas fa-ellipsis-h pointer" onclick="createmodal('{}')"></i>
                        &nbsp;
                        Actual: 
                        &nbsp;
                        <i class="fas fa-ellipsis-h pointer" onclick="createmodal('{}')"></i>
                        '''.format(severity[Severity.BLOCKER][0], severity[Severity.BLOCKER][1], log["id"], log["id"]) + '''
                        </td>
                    '''
            else:
                e_a_content = '''
                           <td style="width: 70%">
                           '''+message_ + '''
                               <i class="{} pointer" onclick="expandFooter('info')" style="{}"></i>
                               Expected: {}    Actual: {}
                               <br>
                               '''.format(severity[Severity.BLOCKER][0], severity[Severity.BLOCKER][1], log["expected"],
                                          log["actual"]) + '''
                           </td>
                       '''
            c += '''
                    <tr class="border-bottom">
                        <td class="text-sm-center" style="width: 10%"><i class="{}" style="{}"></i></td>
                        <td style="width: 10%">{}</td>
                        {}
                        <td style="width: 10%"><span class="extrasmall">{}</span></td>
                    </tr>             
                   '''.format(status[log["status"]][0], status[log["status"]][1], type_, e_a_content, log["start-time"])
    return c


def section(tests):
    index = 0
    c = ''''''
    for test in tests:
        section_head = '''
        <li class="list-group-item font-weight-bold" style="background-color:rgb(0,0,0,0.1); display: flex; justify-content: space-between;">
            <span>{} {}</span>
            <i id="expand" class="fas fa-caret-square-down pointer" style=" font-size:x-large;" data-toggle="collapse" data-target="#moredetails{}" onclick='expandFunction("{}")'></i>
        </li>
        '''.format(test._id, test._name, index, test._id)

        more_details = '''
        <li id="moredetails{}" class="list-group-item small panel-collapse collapse">
            <div class="row">
                <div class="col-5">
                    <div class="row">
                        <div class="col-3">Status</div>
                        <div class="col-9">
                        <i class="{}" style="{} font-size: 13px;"></i>
                        {}</div>
                    </div>
                    <div class="row">
                        <div class="col-3">Priority</div>
                        <div class="col-9">
                        <i class="{}" style="{} font-size: 13px;"></i>
                        {}</div>
                    </div>
                </div>
                <div class="col-7">
                <div class="row">
                        <div class="col-3">Start-time</div>
                        <div class="col-9">{}</div>
                    </div>
                    <div class="row">
                        <div class="col-3">End-time</div>
                        <div class="col-9">{}</div>
                    </div>
                    <div class="row">
                        <div class="col-3">Duration</div>
                        <div class="col-9">{}(H:MM:SS)</div>
                    </div>
                </div>
            </div>
            <div>
            <span>Description</span>
            <p>{}</p>
            </div>
        </li>
        '''.format(index, status[test._result][0], status[test._result][1], test._result.capitalize(),
                   priority[test._priority][0],
                   priority[test._priority][1], test._priority.capitalize(), test._start_time, test._end_time,
                   test._duration, test._description)

        test_steps = '''
        <li class="list-group-item">
            <table class="table medium table-borderless table-hover">
                <thead class="small border-bottom">
                    <tr>
                        <th class="text-sm-center" >STATUS</th>
                        <th>TYPE</th>
                        <th>DETAILS</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody class="small">
                    ''' + table_content(test._logs) + '''
                </tbody>
            </table>
            ''' + screenshot_section(test) + '''
        </li>
        '''.format()

        c += '''
        <div id="''' + test._id + '''" class="filterDiv1 ''' + test._result + '''" style="padding-bottom: 20px;"> 
            <ul class="list-group">
                ''' + section_head + '''
                ''' + more_details + '''
                ''' + test_steps + '''
            </ul>
        </div>         
        '''
        index += 1
    return c


def content(tests):
    c = '''
        <div class="col-sm-12 col-lg-7">
            <div id="search2">
                ''' + section(tests) + '''
            </div>
        </div>
    '''
    return c
