from ctreport_selenium.utility_classes import Status, Priority, Severity

status = {
    Status.PASS: ("fa fa-check-circle", "color:#00AF00; font-size: 18px;"),
    Status.FAIL: ("fa fa-times-circle", "color:#F7464A; font-size: 18px;"),
    Status.SKIP: ("fa fa-minus-circle", "color:#1E90FF; font-size: 18px;"),
    Status.BROKEN: ("fa fa-exclamation-circle", "color:#aaa; font-size: 18px;")
}

priority = {
    Priority.HIGH: ("fas fa-angle-double-up p-high", "color: #cb3434; font-size: 18px;"),
    Priority.MEDIUM: ("fas fa-equals", "color: #ff9900; font-size: 18px;"),
    Priority.LOW: ("fas fa-angle-double-down", "color: #0099ff; font-size: 18px;"),
}

severity = {
    Severity.BLOCKER: ("fas fa-minus-circle", "color:#a22a2a;"),
    Severity.CRITICAL: ("fa fa-exclamation-triangle", "color:#cb3434;"),
    Severity.MAJOR: ("fa fa-exclamation-circle", "color:#ff9900;"),
    Severity.MINOR: ("far fa-circle", "color:#0099ff;"),
}

info_ = {
    "class": "fas fa-info-circle text-info",
}
