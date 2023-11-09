from ctreport_selenium.utility_classes import Status, Priority


def chart(tests):
    pass_ = [0, 0, 0]
    fail_ = [0, 0, 0]
    skip_ = [0, 0, 0]
    broken_ = [0, 0, 0]
    for test in tests:
        if test._result == Status.PASS:
            if test._priority == Priority.HIGH:
                pass_[0] += 1
            elif test._priority == Priority.MEDIUM:
                pass_[1] += 1
            else:
                pass_[2] += 1
        elif test._result == Status.FAIL:
            if test._priority == Priority.HIGH:
                fail_[0] += 1
            elif test._priority == Priority.MEDIUM:
                fail_[1] += 1
            else:
                fail_[2] += 1
        elif test._result == Status.SKIP:
            if test._priority == Priority.HIGH:
                skip_[0] += 1
            elif test._priority == Priority.MEDIUM:
                skip_[1] += 1
            else:
                skip_[2] += 1
        else:
            if test._priority == Priority.HIGH:
                broken_[0] += 1
            elif test._priority == Priority.MEDIUM:
                broken_[1] += 1
            else:
                broken_[2] += 1

    content = '''
        var prioritychart=new Chart(document.getElementById("prioritychart"), {
        type: 'bar',
        data: {
            labels: ["High", "Medium", "Low"],
            datasets: [{
                label: "Passed",
                backgroundColor: "#00AF00",
                data: ''' + str(pass_) + '''
            }, {
                label: "Failed",
                backgroundColor: "#F7464A",
                data: ''' + str(fail_) + '''
            },{
                label: "Skipped",
                backgroundColor: "#1E90FF",
                data: ''' + str(skip_) + '''
            },{
                label: "Broken",
                backgroundColor: "#aaa",
                data: ''' + str(broken_) + '''
            }
            ]
        },
        options: {
            title: {
                fontSize:20,
                display: false,
                text: 'Group under Priority'
            },
            legend: {
                position:'bottom'
            },
            scales: {
                xAxes: [{
                    barThickness : 25,
                    barPercentage: 169,			
                }],
                yAxes: [{
                    display: true,
                    ticks: {
                        display: false,
                        maxTicksLimit: 6,
                        precision:0,
                    }
                }],
            }
        }
    });
    '''
    return content
