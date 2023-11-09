def content(var):
    c = '''
    <script>
        function createmodal(id) {
           ''' + var + '''
            var content = '<table class="table table-bordered ">';
            var footer = ''
            if(Array.isArray(tests[id])){
                content += '<tbody>\
                            <tr class="table-secondary"><td>Expected</td></tr>\
                            <tr class="align-middle">';
                
                content += '<td>'+tests[id][0].join(", ")+'</td></tr>\
                            <tr class="table-secondary"><td>Actual</td></tr>\
                            <tr class="align-middle">';
                
                content += '<td>'+tests[id][1].join(", ")+'</td></tr>';
            }
            else{
                content += '<thead class="thead-light">\
                              <tr>\
                                <th class="align-middle text-sm-center">Status</th>\
                                <th class="align-middle text-sm-center">Key</th>\
                                <th class="align-middle text-sm-center">Expected</th>\
                                <th class="align-middle text-sm-center">Actual</th>\
                              </tr>\
                            </thead>\
                            <tbody>';
                            
                for(var key in tests[id]) {
                    status =''
                    key_='<td>'+key+'</td>'
                    expected='<td>'+tests[id][key][0]+'</td>';
                    actual='<td>'+tests[id][key][1]+'</td>';
                    if (tests[id][key][2]=='true'){
                        status='<i class="fa fa-check-circle align-middle text-sm-center" style="color:#00AF00; font-size: 18px;"></i>';
                    }
                    else{
                        status='<i class="fa-times-circle fa align-middle text-sm-center" style="color:#F7464A; font-size: 18px;"></i>';
                        if (tests[id][key][0]=="null"){
                            key_ = '<td style="background-color:rgb(247, 131, 134,0.3);">'+key+'</td>'
                            expected='<td></td>';
                        }
                        else if(tests[id][key][1]=="null"){
                            actual='<td style="color:#F7464A;">\
                            <i class="fas fa-ban"   data-toggle="tooltip" data-placement="right" data-original-title="Key missing in actual data"></i>\
                            </td>';
                        }
                        else{
                            actual='<td style="background-color: #ffffb2">'+tests[id][key][1]+'</td>';
                        }
                    }
                    content += '<tr class="align-middle text-sm-center">\
                            <td>\
                            '+status+'\
                            </td>\
                            '+key_+'\
                            '+expected+'\
                            '+actual+'\
                          </tr>';
                footer = '<div class="row">\
                            <div class="col-2"><i class="fas fa-square-full border border-secondary" style="color: #ffffb2"></i></div>\
                            <div class="col-10">\Actual is not same as Expected</div>\
                            </div>\
                            <div class="row">\
                            <div class="col-2"><i class="fas fa-square-full border border-secondary" style="color:rgb(247, 131, 134,0.3);"></i></div>\
                            <div class="col-10">New key found in actual</div>\
                            </div>\
                            <div class="row">\
                            <div class="col-2"><i class="fas fa-ban" style="color:#F7464A;"></i></div>\
                            <div class="col-10">Key missing in actual data</div>\
                        </div>\';
                }  
            }
            content += '</tbody>\
            </table>';
            
            var header = "Expected vs Actual";
            
            var html = '<div id="modalWindow" class="modal" data-keyboard="false" data-backdrop="static">';
            html += '<div class="modal-dialog modal-dialog-scrollable ">\
            <div class="modal-content">\
            <div class="modal-header">\
            <button type="button" id="closeModal" class="btn btn-danger" data-dismiss="modal" onclick=deletemodal("modalWindow") style="margin:auto 1rem auto auto; font-size: smaller;">Close</button>\
            </div>\
            <div class="modal-body">'
            +content+'\
            </div>\
            <div class="modal-footer small">'\
            +footer+'\
            </div>\
            </div>\
            </div>\
            </div>';
            $("#myModal").html(html);
            $("#modalWindow").modal();
        }
        function deletemodal(id) {
            var element = document.getElementById(id);
            element.parentNode.removeChild(element);
        };
    </script>
    '''
    return c
