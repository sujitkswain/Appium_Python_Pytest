content = '''
    <script>
        function filterSelection(c) {
            toast_message(c)
            var x, i;
            x = document.getElementsByClassName("filterDiv");
            x1 = document.getElementsByClassName("filterDiv1");
            x2 = document.getElementsByClassName("NoTest");
            if (c == "all") {
                y = document.getElementsByClassName("passicon");
                w3RemoveClass(y[0], "fa fa-check");
                w3AddClass(y[0], "fa fa-check-circle");
                y = document.getElementsByClassName("failicon");
                w3RemoveClass(y[0], "fa fa-times");
                w3AddClass(y[0], "fa fa-times-circle");
                y = document.getElementsByClassName("skipicon");
                w3RemoveClass(y[0], "fa fa-minus");
                w3AddClass(y[0], "fa fa-minus-circle");
                y = document.getElementsByClassName("brokenicon");
                w3RemoveClass(y[0], "fa fa-exclamation");
                w3AddClass(y[0], "fa fa-exclamation-circle");
                for (i = 0; i < x.length; i++) { 
                    if (x[i].className.indexOf(c) > -1 || x1[i].className.indexOf(c) > -1){}
                    else
                     {
                        w3RemoveClass(x[i], "hide");
                        w3RemoveClass(x1[i], "hide");
                     }
                }
                w3RemoveClass(x2[0], "table_show");
				w3AddClass(x2[0], "hide");
            }
            if(c=="passed"){
                y = document.getElementsByClassName("passicon");
                w3RemoveClass(y[0], "fa fa-check-circle");
                w3AddClass(y[0], "fa fa-check");
                y = document.getElementsByClassName("failicon");
                w3RemoveClass(y[0], "fa fa-times");
                w3AddClass(y[0], "fa fa-times-circle");
                y = document.getElementsByClassName("skipicon");
                w3RemoveClass(y[0], "fa fa-minus");
                w3AddClass(y[0], "fa fa-minus-circle");
                y = document.getElementsByClassName("brokenicon");
                w3RemoveClass(y[0], "fa fa-exclamation");
                w3AddClass(y[0], "fa fa-exclamation-circle");
                no_of_tr=0;
                for (i = 0; i < x.length; i++) { 
                    if (x[i].className.indexOf(c) > -1 || x1[i].className.indexOf(c) > -1)
                     {
                     no_of_tr++;
                        w3RemoveClass(x[i], "hide");
                        w3AddClass(x[i], "table_show");
                        w3RemoveClass(x1[i], "hide");
                        w3AddClass(x1[i], "custom_show");
                     }
                    else
                     {
                         w3RemoveClass(x[i], "table_show");
                         w3AddClass(x[i], "hide");
                         w3RemoveClass(x1[i], "custom_show");
                         w3AddClass(x1[i], "hide");
                     }
                }
                if(no_of_tr==0)
				{
					w3RemoveClass(x2[0], "hide");
						 w3AddClass(x2[0], "table_show");
				}
				else{
					w3RemoveClass(x2[0], "table_show");
						 w3AddClass(x2[0], "hide");
				
				}
            }
            if(c=="failed"){
                y = document.getElementsByClassName("passicon");
                w3RemoveClass(y[0], "fa fa-check");
                w3AddClass(y[0], "fa fa-check-circle");
                y = document.getElementsByClassName("failicon");
                w3RemoveClass(y[0], "fa fa-times-circle");
                w3AddClass(y[0], "fa fa-times");
                y = document.getElementsByClassName("skipicon");
                w3RemoveClass(y[0], "fa fa-minus");
                w3AddClass(y[0], "fa fa-minus-circle");
                y = document.getElementsByClassName("brokenicon");
                w3RemoveClass(y[0], "fa fa-exclamation");
                w3AddClass(y[0], "fa fa-exclamation-circle");
                no_of_tr=0;
                for (i = 0; i < x.length; i++) { 
                
                if (x[i].className.indexOf(c) > -1 || x1[i].className.indexOf(c) > -1)
                 {
                 no_of_tr++;
                     w3RemoveClass(x[i], "hide");
                     w3AddClass(x[i], "table_show");
                     w3RemoveClass(x1[i], "hide");
                     w3AddClass(x1[i], "custom_show");

                 }
                else
                 {
                    w3RemoveClass(x[i], "table_show");
                    w3AddClass(x[i], "hide");
                    w3RemoveClass(x1[i], "custom_show");
                    w3AddClass(x1[i], "hide");                    
                 }
                }
                if(no_of_tr==0)
				{
					w3RemoveClass(x2[0], "hide");
						 w3AddClass(x2[0], "table_show");
				}
				else{
					w3RemoveClass(x2[0], "table_show");
						 w3AddClass(x2[0], "hide");
				
				}
                }
                if(c=="skipped"){
                y = document.getElementsByClassName("passicon");
                w3RemoveClass(y[0], "fa fa-check");
                w3AddClass(y[0], "fa fa-check-circle");
                y = document.getElementsByClassName("failicon");	
                w3RemoveClass(y[0], "fa fa-times");
                w3AddClass(y[0], "fa fa-times-circle");
                y = document.getElementsByClassName("skipicon");
                w3RemoveClass(y[0], "fa fa-minus-circle");
                w3AddClass(y[0], "fa fa-minus");
                y = document.getElementsByClassName("brokenicon");
                w3RemoveClass(y[0], "fa fa-exclamation");
                w3AddClass(y[0], "fa fa-exclamation-circle");
                no_of_tr=0;
                for (i = 0; i < x.length; i++) { 
                
                    if (x[i].className.indexOf(c) > -1 || x1[i].className.indexOf(c) > -1)
                     {
                     no_of_tr++;
                         w3RemoveClass(x[i], "hide");
                         w3AddClass(x[i], "table_show");
                         w3RemoveClass(x1[i], "hide");
                         w3AddClass(x1[i], "custom_show");
                     }
                    else
                     {
                        w3RemoveClass(x[i], "table_show");
                        w3AddClass(x[i], "hide");
                        w3RemoveClass(x1[i], "custom_show");
                        w3AddClass(x1[i], "hide");
                     }
                }
                if(no_of_tr==0)
				{
					w3RemoveClass(x2[0], "hide");
						 w3AddClass(x2[0], "table_show");
				}
				else{
					w3RemoveClass(x2[0], "table_show");
						 w3AddClass(x2[0], "hide");
				
				}
            }
            if(c=="broken"){
                y = document.getElementsByClassName("passicon");
                w3RemoveClass(y[0], "fa fa-check");
                w3AddClass(y[0], "fa fa-check-circle");
                y = document.getElementsByClassName("failicon");	
                w3RemoveClass(y[0], "fa fa-times");
                w3AddClass(y[0], "fa fa-times-circle");
                y = document.getElementsByClassName("skipicon");
                w3RemoveClass(y[0], "fa fa-minus");
                w3AddClass(y[0], "fa fa-minus-circle");
                y = document.getElementsByClassName("brokenicon");
                w3RemoveClass(y[0], "fa fa-exclamation-circle");
                w3AddClass(y[0], "fa fa-exclamation");
                no_of_tr=0;
                for (i = 0; i < x.length; i++) { 
                    if (x[i].className.indexOf(c) > -1 || x1[i].className.indexOf(c) > -1)
                     {
                     no_of_tr++;
                        w3RemoveClass(x[i], "hide");
                        w3AddClass(x[i], "table_show");
                        w3RemoveClass(x1[i], "hide");
                        w3AddClass(x1[i], "custom_show");
                     }
                    else
                     {
                        w3RemoveClass(x[i], "table_show");
                        w3AddClass(x[i], "hide");
                        w3RemoveClass(x1[i], "custom_show");
                        w3AddClass(x1[i], "hide");
                     }
                }
                if(no_of_tr==0)
				{
					w3RemoveClass(x2[0], "hide");
						 w3AddClass(x2[0], "table_show");
				}
				else{
					w3RemoveClass(x2[0], "table_show");
						 w3AddClass(x2[0], "hide");
				
				}
            }
        }
        
        function w3AddClass(element, name) {
            var i, arr1, arr2;
            arr1 = element.className.split(" ");
            arr2 = name.split(" ");
            for (i = 0; i < arr2.length; i++) {
                if (arr1.indexOf(arr2[i]) == -1) {
                    element.className += " " + arr2[i];
                }
            }
        }
        
        function w3RemoveClass(element, name) {
            var i, arr1, arr2;
            arr1 = element.className.split(" ");
            arr2 = name.split(" ");
            for (i = 0; i < arr2.length; i++) {
                while (arr1.indexOf(arr2[i]) > -1) {
                  arr1.splice(arr1.indexOf(arr2[i]), 1);     
                }
            }
            element.className = arr1.join(" ");
        }
    </script>
    '''
