content = '''
    <script>
    function myFunction() {
        var input, search_term,tbody,tr,span,test_id,test_name;
        var div1,div2,li1,span1,test_id1,test_name1;
        input = document.getElementById("myInput");
        search_term = input.value.toUpperCase();
        //console.log("search_term: "+search_term);
        tbody=document.getElementById("search1");
        tr=tbody.getElementsByTagName("tr");
        div1=document.querySelectorAll("div#search2>div");
        //console.log("no of div2: "+div2.length);
        for (i = 0; i < tr.length-1; i++) {
            span=tr[i].querySelectorAll("td span:nth-child(1)");
            if(span)
            {
                id=span[0].textContent;
                test_name=span[1].textContent;
                if((test_name.toUpperCase().indexOf(search_term)>-1)
                ||(id.toUpperCase().indexOf(search_term)>-1)){
                    //console.log(test_name);
                    tr[i].style.display = "";
                }
                else{
                    tr[i].style.display = "none";
                }
            }
        }
        for (i = 0; i < div1.length; i++) {
            span=div1[i].querySelectorAll("ul>li:nth-child(1) span");
            if(span)
            {
                id=span[0].innerHTML.split(" ")[0];
                test_name=span[0].innerHTML;
                if((test_name.toUpperCase().indexOf(search_term)>-1)
                ||(id.toUpperCase().indexOf(search_term)>-1)){
                    div1[i].style.display = "";
                }
                else{
                    div1[i].style.display = "none";
                }
            }
        }
    }
    </script>
    '''
