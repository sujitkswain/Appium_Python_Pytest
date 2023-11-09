def content():
    c = '''
    <footer class="footer">
        <div class="bg-light pl-4 p-2">
            <span id="reference">
            <i class="fas fa-caret-right pr-1 pointer" onclick="expandFooter('foot')" style="font-size:20px"></i>
            Reference</span>
        </div>
        <section class="pading test_details">
            <div class="row">
                <div class=" col-sm-4 col-md col-sm-4  col-12 col">						
                    <div id="footer" class="row hide"> 
                        <div class="col-4 border-right">						
                            <p class="pt2">Status: Test status after execution</p> 
                            <div class="row">	
                                <div class="col-3 align-self-center">
                                <p>
                                    <i class="fa fa-check-circle" style="color:#00AF00;"></i>
                                Pass
                                </p>
                                </div>
                                <div class="col-9">
                                    <p class="mb10">Test case is passed without any verification/assertion/fatal errors</p>
                                </div>
                            </div>
                            <div class="row">	
                                <div class="col-3 align-self-center">
                                <p>
                                    <i class="fa fa-times-circle failicon" style="color:#F7464A;"></i>
                                Fail
                                </p>
                                </div>
                                <div class="col-9">
                                    <p class="mb10">Test case is failed due to verification/assertion errors</p>
                                </div>
                            </div>
                            <div class="row">	
                                <div class="col-3 align-self-center">
                                <p>
                                    <i class="fa fa-minus-circle skipicon" style="color:#1E90FF;"></i>
                                Skip
                                </p>
                                </div>
                                <div class="col-9">
                                    <p class="mb10">Test case skipped due to blocker or critical issue in dependencies</p>
                                </div>
                            </div>
                            <div class="row">	
                                <div class="col-3 align-self-center">
                                <p>
                                    <i class="fa fa-exclamation-circle brokenicon" style="color:#aaa"></i>
                                Broken
                                </p>
                                </div>
                                <div class="col-9">
                                    <p class="mb10">Test case stopped due to fatal errors</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-4 border-right">						
                            <p class="pt2">Priority: Applies to test case</p> 
                            <div class="row">	
                                <div class="col-3 align-self-center">
                                <p>
                                    <i class="fas fa-angle-double-up p-high" style="color: #cb3434"></i>
                                High
                                </p>
                                </div>
                                <div class="col-9">
                                    <p class="mb10">Test case on the most important features of the application</p>
                                </div>
                            </div>
                            <div class="row">	
                                <div class="col-3 align-self-center">
                                <p>
                                    <i class="fas fa-equals" style="color: #ff9900"></i>
                                Medium
                                </p>
                                </div>
                                <div class="col-9">
                                    <p class="mb10">Test case on features of the application which is next to High priority test cases</p>
                                </div>
                            </div>
                            <div class="row">	
                                <div class="col-3 align-self-center">
                                <p>
                                    <i class="fas fa-angle-double-down" style="color: #0099ff"></i>
                                Low
                                </p>
                                </div>
                                <div class="col-9">
                                    <p class="mb10">Test case on features of the application which is considered to be executed rarely</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-4">
                        <p class="pt2">Severity: Applies to verification and assertion statements</p>
                        <p class="pt2"><mark>Note: All assertions are treated as Blocker severity</mark></p> 
                            <div class="row">	
                                <div class="col-3 align-self-center">
                                <p>
                                    <i class="fas fa-minus-circle" style="color:#a22a2a;"></i>
                                Blocker
                                </p>
                                </div>
                                <div class="col-9">
                                    <p class="mb10"> The system or functionality is currently unavailable to continue working on the application because of this incident</p>
                                </div>
                            </div>
                            <div class="row">	
                                <div class="col-3 align-self-center">
                                <p>
                                <i class="fa fa-exclamation-triangle" style="color:#cb3434;"></i>
                                Critical
                                </p>
                                </div>
                                <div class="col-9">
                                    <p class="mb10">Essential functionality is not functioning and no acceptable workaround</p>
                                </div>
                            </div>
                            <div class="row">	
                                <div class="col-3 align-self-center">
                                <p>
                                <i class="fa fa-exclamation-circle" style="color:#ff9900;"></i>
                                Major
                                </p>
                                </div>
                                <div class="col-9">
                                    <p class="mb10">Essential functionality is not functioning unless acceptable workaround is implemented</p>
                                </div>
                            </div>
                            <div class="row">	
                                <div class="col-3 align-self-center">
                                <p>
                                    <i class="far fa-circle" style="color:#0099ff;"></i>
                                Minor
                                </p>
                                </div>
                                <div class="col-9">
                                    <p class="mb10">Minor inconvenience in the functionality and application remains operational</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        </footer>
        <br/>
    '''
    return c
