content = '''
    <script>
    function showFooter(){
            footer=document.getElementById("footer");
            w3RemoveClass(footer, "hide");
            w3AddClass(footer, "show");
            var elmnt = document.getElementById("reference");
            elmnt.scrollIntoView();	
        }
        function hideFooter(){
            footer=document.getElementById("footer");
            w3RemoveClass(footer, "show");
            w3AddClass(footer, "hide");
        }
        function expandFooter(frm){
            footer=document.getElementById("footer");
            h5=document.getElementById("reference");
            i=h5.querySelector("i");
            if(frm=="info")
            {
                showFooter();
                w3RemoveClass(i, "fas fa-caret-right");
                w3AddClass(i, "fas fa-caret-down");
            }
            else{
                if (i.className.includes("fas fa-caret-right")){
                    showFooter();
                    w3RemoveClass(i, "fas fa-caret-right");
                    w3AddClass(i, "fas fa-caret-down");
                }
                else{
                    hideFooter();
                    w3RemoveClass(i, "fas fa-caret-down");
                    w3AddClass(i, "fas fa-caret-right");
                }
            }

        }
        function expandFunction(id){
            div = document.getElementById(id);
            i = div.querySelector("#expand")
            if (i.className.includes("fas fa-caret-square-down"))
            {
                w3RemoveClass(i, "fas fa-caret-square-down");
                w3AddClass(i, "fas fa-caret-square-up");
            }
            else{
                    w3RemoveClass(i, "fas fa-caret-square-up");
                    w3AddClass(i, "fas fa-caret-square-down");
            }
        }
    </script>
    '''
