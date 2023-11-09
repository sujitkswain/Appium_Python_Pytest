"""
    Priority: Applies to test case
    ------------------------------
    High - Test case on most important features of the application
    Medium - Test case on features of the application which is next to High priority test cases
    Low - Test case on features of the application which is considered to be executed rarely

    Status: Test status after execution
    ------------------------------
     Pass - Test case is passed without any verification/assertion/fatal errors
     Fail - Test case is failed due to verification/assertion errors
     Skip - Test case skipped due to blocker or critical issue in dependencies
     Broken - Test case stopped due to fatal errors

     Severity: Applies to verification and assertion statements
     ------------------------------
    Blocker - The system or functionality is currently unavailable to continue working on the application because of this incident
    Critical - Essential functionality is not functioningand no acceptable workaround
    Major - Essential functionality is not functioning unless acceptable workaround is implemented
    Minor - Minor inconvenience in the functionality and application remains operational
"""


class Priority(object):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Severity(object):
    BLOCKER = "blocker"
    CRITICAL = "critical"
    MAJOR = "major"
    MINOR = "minor"


class Status(object):
    PASS = "passed"
    FAIL = "failed"
    SKIP = "skipped"
    BROKEN = "broken"
